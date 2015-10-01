#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'\u53f0\u7063\u958b\u767c\u8005'
SITENAME = u'\u53f0\u7063\u958b\u767c\u8005\u6587\u6458'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Others'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# JINJA_EXTENSIONS = ['jinja2.ext.i18n']
# JINJA_FILTERS = {}
# MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']

PAGE_PATHS = ['pages']  # relative to PATH
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{lang}/{slug}'
PAGE_LANG_SAVE_AS = '{lang}/{slug}/index.html'
# PAGE_EXCLUDES = []

ARTICLE_PATHS = ['posts']  # relative to PATH
ARTICLE_URL = 'post/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'post/{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL = 'post/{date:%Y}/{date:%m}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = 'post/{date:%Y}/{date:%m}/{slug}-{lang}/index.html'
# ARTICLE_EXCLUDES = []

CATEGORIES_URL = 'category'
CATEGORIES_SAVE_AS = 'category/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'

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

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-bootstrap3'

