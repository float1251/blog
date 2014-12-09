#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'float1251'
SITENAME = "float's memo"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

THEME = "dev-random"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
        ('twitter', 'https://twitter.com/float1251'),
        ('github', 'https://github.com/float1251'),
    )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY=True

ARTICLE_EXCLUDES=["drafts"]

SLUGIFY_SOURCE="basename"

ARTICLE_URL="{category}/{date:%Y}/{date:%m}/{slug}.html"
ARTICLE_SAVE_AS="{category}/{date:%Y}/{date:%m}/{slug}.html"
