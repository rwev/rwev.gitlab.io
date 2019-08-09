#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

OWNER = "rwev"
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
SIMILAR_ARTICLES = "similar articles"

AUTHOR = "author"
CATEGORY = "category"
TAG = "tag"
TAGS = "tags"

PREVIOUS = "prev"
NEXT = "next"


DATE = "date" # posted on

ATOM="atom"
RSS="rss"

DEFAULT_DATE_FORMAT="%Y.%m.%d"# big

TAG_FEED_ATOM="tag.{slug}.atom"
TAG_FEED_RSS="tag.{slug}.rss"
CATEGORY_FEED_ATOM="category.{slug}.atom"
CATEGORY_FEED_RSS="category.{slug}.rss"

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

### PLUGINS ###
PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS=[
    "autopages",
    "similar_posts",
    "neighbors",
    "section_number",
    "encrypt_content"
]

# autopages
_AUTOPAGES = "./content/autopages"
AUTHOR_PAGE_PATH = "{0}/authors".format(_AUTOPAGES)
CATEGORY_PAGE_PATH = "{0}/categories".format(_AUTOPAGES)
TAG_PAGE_PATH = "{0}/tags".format(_AUTOPAGES)

# similar_posts
SIMILAR_POSTS_MAX_COUNT = 3

# encrypt_content
ENCRYPT_CONTENT={
    'title_prefix': '[Encrypted]',
    'summary': 'This content is password protected.'
}
