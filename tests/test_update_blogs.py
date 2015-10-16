# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import os

from scripts import update_blogs as t


class TestUpdateBlogs(object):

    def test_read_blog_data(self):

        data = t.read_blog_data()
        assert len(data) > 0

    def test_url_to_slug(self):

        s1 = t.url_to_slug('https://samkuo.me')
        assert s1 == 'samkuo-me'

        s2 = t.url_to_slug('http://www.google.com')
        assert s2 == 'www-google-com'

    def test_fetch_url_data(self):
        info = t.fetch_url_data('https://samkuo.me')
        assert info is not None

    def test_build_blog_info_page1(self):
        curdir = os.path.dirname(__file__)
        page = os.path.join(curdir, 'page1.html')
        with open(page) as f:
            text = f.read()

        url = 'https://samkuo.me'
        meta = t.extract_meta_info(text, url)
        assert len(meta) > 0

        info = t.build_blog_info(meta)
        assert isinstance(info, t.BlogInfo)

        assert "我是山姆鍋" == info.title
        assert 'https://samkuo.me' == info.url

    def test_build_blog_info_page2(self):
        curdir = os.path.dirname(__file__)
        page = os.path.join(curdir, 'page3.html')
        with open(page) as f:
            text = f.read()

        url = 'http://blog.wu-boy.com/'
        meta = t.extract_meta_info(text, url)
        assert len(meta) > 0

        info = t.build_blog_info(meta)
        assert isinstance(info, t.BlogInfo)


        #assert "搞笑談軟工" == info.title
        assert 'http://blog.wu-boy.com' == info.url

    def test_extract_meta_info(self):
        curdir = os.path.dirname(__file__)
        page = os.path.join(curdir, 'page1.html')
        with open(page) as f:
            text = f.read()

        url = 'https://samkuo.me'
        meta = t.extract_meta_info(text, url)
        assert len(meta) > 0

    def test_extractor(self):
        url = 'https://samkuo.me'
        ext = t.Extractor(url)

        ext._run()

        assert ext.result is not None
