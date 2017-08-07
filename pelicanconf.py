#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'float1251'
SITENAME = "float1251's memo"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

THEME = "pelican-themes/Flex"

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
RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY=True

ARTICLE_EXCLUDES=["drafts"]

SLUGIFY_SOURCE="basename"

ARTICLE_URL="{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS="{date:%Y}/{date:%m}/{date:%d}/{slug}.html"

DATE_FORMATS = {
    "ja": "%Y年%m月%d日(%a)"    
}

STATIC_PATHS = ["images"]

#### 以下を入れないと、make htmlしたときにpagenationのファイルが作成できないErrorとなる  ##########
CATEGORY_URL            = 'category/{slug}/'
CATEGORY_SAVE_AS        = 'category/{slug}/index.html'
TAG_URL                 = 'tag/{slug}/'
TAG_SAVE_AS             = 'tag/{slug}/index.html'
##############################

PAGINATION_PATTERNS     = (
    (1, '{base_name}/',               '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Flexの設定
SITETITLE = "float1251's memo"
SITEDESCRIPTION = 'game programmer, web developer.'
MAIN_MENU = True
SITEURL = "http://float1251.github.io/blog/"
SITELOGO = SITEURL + 'images/me.jpeg'

MENUITEMS = (('Archives', SITEURL+'/archives.html'),
             ('Categories', SITEURL+'/categories.html'),
             ('Tags', SITEURL+'/tags.html'),)

LINKS = (('Archives', SITEURL+'/archives.html'),
             ('Categories', SITEURL+'/categories.html'),
             ('Tags', SITEURL+'/tags.html'),)
