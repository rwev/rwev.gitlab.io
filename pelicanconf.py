#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "rwev"
SITENAME = "Delma"
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
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

MENUITEMS = (
    ("Home", "home.html"),
    ("About", "about.html"),
    ("Writings", "writings.html"),
    ("Projects", "projects.html"),
    ("Contact", "contact.html"),
    # ("Resume", "")
)

DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = True
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
