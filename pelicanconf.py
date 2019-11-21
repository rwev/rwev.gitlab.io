#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import sys
import os

sys.path.append(os.curdir)
from tundra import *

# TEMPLATE
OWNER = "rwev"
AUTHOR = OWNER
SITENAME = "rwev.dev"

SITEURL = "localhost:8000"

USER_LOGO_URL = "assets/images/valknut-nord7.png"
TAGLINE = "Wild wolf before domesticated dog."

DISPLAY_PAGES_ON_MENU = False
# BUILD PROCESS
DEFAULT_METADATA = {
    "author": OWNER,
    "status": "draft",  # status: published, draft, hidden
}

PATH = "content"
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["assets"]
ARTICLE_PATHS = ["articles/published"]
OUTPUT_PATH = "./public"  # for gitlab page

TIMEZONE = "America/Denver"
DEFAULT_LANG = "en"

LINK_ITEMS = (
    ("GitHub", "https://github.com/rwev"),
    ("GitLab", "https://gitlab.com/rwev"),
)

# PLUGINS
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
AUTOPAGES_PATH = os.path.join("content", "autopages")

AUTHOR_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "authors")
CATEGORY_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "categories")
TAG_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "tags")


# encrypt_content
ENCRYPT_CONTENT = {
    "title_prefix": "[Encrypted]",
    "summary": "This content is password protected.",
}

# photos
PHOTO_LIBRARY = "./content/assets/images"
PHOTO_EXIF_COPYRIGHT_AUTHOR = "Ryan William"

