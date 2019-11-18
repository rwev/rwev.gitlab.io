#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os.path as path

### GENERATION VARS

OWNER = "rwev"
SITENAME = "rwev"

SITEURL = "localhost:8000"
DEFAULT_METADATA = {
    "author": OWNER,
    "status": "draft",  # status: published,draft,hidden
}

USER_LOGO_URL = "assets/images/valknut-nord7.png"

TAGLINE = "Wolf in the wilderness before a dog in a cage."
# "Type 7. Dynamic generalist. Under-specialized, over-versatile. Robust in many environments. Variety is spice of life."

PATH = "content"
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["assets"]
ARTICLE_PATHS = ["articles/published"]
THEME = "tundra"

OUTPUT_PATH = "./public"  # for gitlab page

TIMEZONE = "America/Denver"

DEFAULT_LANG = "en"

### TEMPLATE VARS TODO cleanup

# Blogroll

BLOG = "blog"
DISPLAY_LINKS_ON_MENU = True
LINKS = "links"
LINK_ITEMS = (
    ("GitHub", "https://github.com/rwev"),
    ("GitLab", "https://gitlab.com/rwev"),
)

# Social widget
DISPLAY_SOCIAL_ON_MENU = False
SOCIAL = "social"
SOCIAL = ()

ARCHIVES = "archives"
HOME = "home"
SIMILAR_ARTICLES = "similar articles"

ARTICLES = "articles"

PAGE = "page"
PAGES = "pages"

AUTHOR = "author"
AUTHOR_S = "author(s)"

CATEGORY = "category"
CATEGORIES = "categories"

SUBCATEGORY = "subcategory"
SUBCATEGORIES = "subcategories"

GALLERY = "gallery"

TAG = "tag"
TAGS = "tags"

PREVIOUS = "prev"
NEXT = "next"

NEWER = "newer"
OLDER = "older"

POSTED = "posted"  # posted on
MODIFIED = "modified"

ATOM = "atom"
RSS = "rss"

DEFAULT_DATE_FORMAT = "%Y.%m.%d %H:%M"  # big

FEED_ALL_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM = "feeds/author.{slug}.atom.xml"
AUTHOR_FEED_RSS = "feeds/author.{slug}.rss.xml"

TAG_FEED_ATOM = "feeds/tag.{slug}.atom.xml"
TAG_FEED_RSS = "feeds/tag.{slug}.rss.xml"

CATEGORY_FEED_ATOM = "feeds/category.{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/category.{slug}.rss.xml"

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_PAGES_ON_MENU = True

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

VERTSEPCHARS = " // "

### PLUGINS ###
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "filetime_from_git",
    "autopages",
    "similar_posts",
    "neighbors",
    "section_number",
    #    "encrypt_content", TODO
    "more_categories",
    "gzip_cache",
    "photos",
    "summary",
    "clean_summary",
]

# autopages
_AUTOPAGES = path.join("content", "autopages")

AUTHOR_PAGE_PATH = path.join(_AUTOPAGES, "authors")
CATEGORY_PAGE_PATH = path.join(_AUTOPAGES, "categories")
TAG_PAGE_PATH = path.join(_AUTOPAGES, "tags")

# similar_posts
SIMILAR_POSTS_MAX_COUNT = 3

# encrypt_content
ENCRYPT_CONTENT = {
    "title_prefix": "[Encrypted]",
    "summary": "This content is password protected.",
}

# photos
PHOTO_LIBRARY = "./content/assets/images"

# 1.33~ width/height ratio
PHOTO_GALLERY = (2000, 1500, 95)  # width, height, quality % of max
PHOTO_ARTICLE = (760, 506, 95)
PHOTO_THUMB = (300, 225, 70)

PHOTO_SQUARE_THUMB = True
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = False

PHOTO_EXIF_KEEP = False
PHOTO_EXIF_REMOVE_GPS = True

PHOTO_EXIF_COPYRIGHT = "CC-BY-NC-ND"
PHOTO_EXIF_COPYRIGHT_AUTHOR = "Ryan William"

# summary
SUMMARY_MAX_LENGTH = 1000  # use whole summary
SUMMARY_USE_FIRST_PARAGRAPH = True
CLEAR_SUMMARY_MAXIMUM = 0
CLEAN_SUMMARY_MINIMUM_ONE = False
