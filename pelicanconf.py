#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "rwev"
SITENAME = "sieben"
SITEURL = ""

PATH = "content"
THEME = "./theme"

TIMEZONE = "America/Denver"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
DISPLAY_LINKS_ON_MENU = True
LINKS_MENU_TITLE = "links"
LINKS = (
    ("GitHub", "https://github.com/rwev"),
    ("GitLab", "https://gitlab.com/rwev"),
)

# Social widget
DISPLAY_SOCIAL_ON_MENU = True
SOCIAL_MENU_TITLE = "social"
SOCIAL = (
   #  ("You can add links in your config file", "#"),
   #  ("Another social link", "#"),
)

ARCHIVES = "archives"
HOME = "home"

CATEGORY = "category"
TAG = "tag"

ATOM="atom"
RSS="rss"

DEFAULT_DATE_FORMAT="%Y.%m.%d"# big

CATEGORY_FEED_ATOM="{slug}.atom"
CATEGORY_FEED_RSS="{slug}.rss"

DISPLAY_CATEGORIES_ON_MENU = True
CATEGORIES_MENU_TITLE = "categories"
TAGS_MENU_TITLE = "tags"

DISPLAY_PAGES_ON_MENU = True
PAGES_MENU_TITLE = "pages"
# MENUITEMS = (
   # ("Home", "home.html"),
   # ("About", "about.html"),
   # ("Writings", "writings.html"),
   # ("Projects", "projects.html"),
   # ("Contact", "contact.html"),
   #  ("Resume", "")
# )

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

VERTSEPCHARS = " // "


