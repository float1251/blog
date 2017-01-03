#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://float1251.github.io/blog'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_RSS = "feeds/rss.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME="floatsmemo"
#GOOGLE_ANALYTICS = ""


MAIN_MENU = True
MENUITEMS = (('Archives', SITEURL+'/archives.html'),
             ('Categories', SITEURL+'/categories.html'),
             ('Tags', SITEURL+'/tags.html'),)

LINKS = (('Archives', SITEURL+'/archives.html'),
             ('Categories', SITEURL+'/categories.html'),
             ('Tags', SITEURL+'/tags.html'),)
