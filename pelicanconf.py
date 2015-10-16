#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)


AUTHOR = u'台灣開發者'
SITENAME = u'台灣開發者文摘'
SITEURL = 'http://localhost:8000'
PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh'

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'zh': '%Y年%m月%d日',
}
HTML_LANG = u'zh-tw'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Others'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# JINJA_EXTENSIONS = ['jinja2.ext.i18n']
# JINJA_FILTERS = {}
# MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']

INDEX_SAVE_AS = 'blog/index.html'

PAGE_PATHS = ['pages']  # relative to PATH
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{lang}/{slug}'
PAGE_LANG_SAVE_AS = '{lang}/{slug}/index.html'
# PAGE_EXCLUDES = []

ARTICLE_PATHS = ['blogs']  # relative to PATH
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}/index.html'
# ARTICLE_EXCLUDES = []

CATEGORIES_URL = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'

# do not need author pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# Tag cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 10

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''

ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SLUGIFY_SOURCE = 'basename'  # basename: filename, title: title metadata

# Blogroll
LINKS = (
         ('《程式人雜誌》', 'https://www.facebook.com/groups/programmerMagazine/'),
         ('《Python Taiwan》', 'https://www.facebook.com/groups/pythontw/'),
         ('《Backend 台灣》', 'https://www.facebook.com/groups/616369245163622/'),
         ('《Docker.Taipei》', 'https://www.facebook.com/groups/docker.taipei/'),
         )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

RELATIVE_URLS = False

STATIC_PATHS = ['static', 'media', ]
EXTRA_PATH_METADATA = {'static/CNAME': {'path': 'CNAME'},
                       'static/robots.txt': {'path': 'robots.txt'},
                       'media/favicon.ico': {'path': 'favicon.ico'},
                       'static/google45600e2c4169dd1a.html': {'path': 'google45600e2c4169dd1a.html'},
                       }

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'tags', 'search']

DEFAULT_PAGINATION = 6

#PAGINATION_PATTERNS = (
#    (1, '{base_name}/', '{base_name}/index.html'),
#    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
#)

DISPLAY_BREADCRUMBS = True

THEME = 'themes/pelican-bootstrap3'

BOOTSTRAP_THEMES = ['amelia', 'cerulean', 'cosmo', 'united', 'flatly']
BOOTSTRAP_THEME = BOOTSTRAP_THEMES[4]
BOOTSTRAP_FLUID = False
BOOTSTRAP_NAVBAR_INVERSE = False
FAVICON = 'favicon.ico'

BANNER = "media/banner.png"
BANNER_SUBTITLE = '歡迎加入<a href="https://www.facebook.com/groups/developers.tw"><span class="label label-success">《台灣開發者文摘》</span></a>'

USE_OPEN_GRAPH = True
OPEN_GRAPH_IMAGE = 'media/site-image.png'
OPEN_GRAPH_DESC = '專為台灣開發者成立的臉書社團，目的在提倡原創技術性文章分享, 只要是原創技術性文章都歡迎發表。'


CUSTOM_CSS = 'static/custom.css'


PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'cjk-auto-spacing', 'related_posts', ]
PLUGINS += ['thumbnailer', 'assets', ]



## Sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


## Thumbnailer
IMAGE_PATH = 'media/blog-images'
THUMBNAIL_DIR = 'thumbnails'
THUMBNAIL_KEEP_TREE = True
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_SIZES = {'small': '240x160'}
