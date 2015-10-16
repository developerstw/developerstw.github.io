# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from gevent import monkey
monkey.patch_all(thread=False)

import os
import logging
import requests

from datetime import datetime
from bs4 import BeautifulSoup
from slugify import slugify

basedir = os.path.dirname(os.path.abspath(__file__))
basedir = os.path.dirname(basedir)


PNG_EXT = '.png'
JPG_EXT = '.jpg'
DEFAULT_IMAGE = 'default.png'

DATA_FILE = os.path.join(basedir, 'content', 'blog_urls.txt')
POST_OUTPUT_FOLDER = os.path.join(basedir, 'content', 'blogs')
IMAGE_OUTPUT_FOLDER = os.path.join(basedir, 'content', 'media', 'blog-images')
HTML_OUTPUT_FOLDER = os.path.join(basedir, 'data', 'homepages')

BLOG_TEMPLATE = """
{title}
{hashes}

:date: {year}-{month}-{day} {hour}:{minute:02d}
:tags:
:category: Blog
:status: published
:blog_url: {url}
:blog_author: {author}
:image_name: {image_name}
:comments: disabled

{summary}
"""

logger = logging.getLogger(__name__)


def to_unicode(s, encoding='utf-8'):
    if isinstance(s, unicode):
        return s

    return unicode(s, encoding)


def url_to_slug(url):
    u1 = slugify(url)
    if u1.startswith('https-'):
        return u1[6:]
    else:
        return u1[5:]


def fetch_url_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    r = requests.get(url, headers=headers)
    logger.debug("Guessed HTML encoding: %s", r.encoding)

    r.encoding = 'utf-8'
    return r


def build_blog_info(meta):
    info = BlogInfo()

    title = meta.get('og:title')
    if title is None:
        title = meta.get('title')
        if title:
            title = title.string.strip()

    if title is None:
        raise RuntimeError("No title available")

    info.title = to_unicode(title)

    url = meta.get('og:url')

    if url is None:
        url = meta.get('url')

    if url is None:
        raise RuntimeError("No url available")

    info.url = url

    author = meta.get('author')
    if author:
        info.author = to_unicode(author)

    image = meta.get("og:image")
    if image:
        if not image.startswith("http"):
            print("Image URL is relative: ", image)
            image = url + image
        info.image = image

    desc = meta.get("og:description")
    if desc is None:
        desc = meta.get("description")

    if desc:
        info.summary = to_unicode(desc)

    return info


def extract_meta_info(html_text, url):
    meta_data = {}
    meta_data['url'] = url
    soup = BeautifulSoup(html_text,  "html.parser")
    title = soup.head.title
    meta_data['title'] = title
    for meta in soup.findAll(name='meta'):
        print(meta.attrs)
        name = meta.get('name')
        if name is None:
            name = meta.get('property')

        if name is None:
            continue

        print("Meta found: %s" % name)
        content = meta.get('content')
        if content is None:
            continue
        meta_data[name] = content

    return meta_data


def read_blog_data():
    """ Reads the blog data from file.
    :return: the list of blog URLS
    """
    with open(DATA_FILE) as f:
        content = f.readlines()

    return content


def download_image(url, slug, referer_url):
    logger.debug("Downloading image from %s for blog: %s", url, slug)

    headers = {'referer': referer_url}
    try:
        r = requests.get(url, headers=headers)
    except:
        return DEFAULT_IMAGE

    mimetype = r.headers['Content-Type']

    if 'png' in mimetype:
        ext = PNG_EXT

    elif 'jpeg' in mimetype:
        ext = JPG_EXT

    else:
        raise RuntimeError("Unknown image type: " + mimetype)

    image_name = slug + ext
    out = os.path.join(IMAGE_OUTPUT_FOLDER, image_name)
    with open(out, 'w') as f:
        f.write(r.content)

    return image_name


def save_homepage(slug, text):
    """ Saves the content of retrieved homepage.

    :param slug:
    :param text:
    """
    filename = slug + '.html'
    out = os.path.join(HTML_OUTPUT_FOLDER, filename)

    with open(out, 'w') as f:
        f.write(text.encode('utf-8'))


class BlogInfo(object):

    def __init__(self):
        self.url = None
        self.image = None
        self.title = ''
        self.summary = ''
        self.author = '未知'

    def __repr__(self):
        s = []
        s.append('Blog[')
        s.append("url=")
        s.append(self.url)

        if self.title:
            s.append(", title='")
            s.append(self.title)
            s.append("'")

        if self.image:
            s.append(", image=")
            s.append(self.image)

        s.append("]")
        return ''.join(s)


class Extractor(object):

    def __init__(self, url):
        assert url is not None
        assert len(url.strip()) > 0
        url = url.strip()
        assert url.startswith('http')

        self.url = url
        self.slug = url_to_slug(self.url)
        self.image_name = 'default.png'
        self.response = None
        self.result = None

    def write_post_file(self):

        out = os.path.join(POST_OUTPUT_FOLDER, self.slug + '.rst')

        kwargs = dict()
        kwargs['author'] = self.result.author
        kwargs['title'] = self.result.title
        kwargs['hashes'] = '#' * (4 + len(self.result.title.encode('utf-8')))
        kwargs['url'] = self.result.url
        kwargs['summary'] = self.result.summary.strip()
        kwargs['image_name'] = self.image_name

        today = datetime.today()
        kwargs['year'] = today.year
        kwargs['month'] = today.month
        kwargs['day'] = today.day
        kwargs['hour'] = today.hour
        kwargs['minute'] = today.minute

        text = BLOG_TEMPLATE.strip().format(**kwargs)

        with open(out, 'w') as f:
            f.write(text.encode('utf-8'))

    def _run(self):
        self.response = fetch_url_data(self.url)
        html_text = self.response.text
        save_homepage(self.slug, html_text)
        meta = extract_meta_info(html_text, self.url)
        info = build_blog_info(meta)
        if info.image:
            self.image_name = download_image(info.image, self.slug, self.url)

        self.result = info
        self.write_post_file()


def main():
    logging.basicConfig(level=logging.DEBUG)

    urls = read_blog_data()
    for url in urls:
        url = url.strip()
        if len(url) == 0 or url.startswith('#'):
            continue
        ext = Extractor(url)
        ext._run()
        print(unicode(ext.result))

if __name__ == '__main__':
    main()
