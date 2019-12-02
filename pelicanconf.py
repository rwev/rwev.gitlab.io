#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
import os

sys.path.append(os.curdir)
from tundra.tundraconf import *

# TEMPLATE
OWNER = "rwev"
AUTHOR = OWNER
SITENAME = "rwev.dev"

SITEURL = "localhost:8000"

USER_LOGO_URL = "assets/images/valknut-nord7.png"
TAGLINE = "Pragmatic. Principled. Purposeful."

DISPLAY_PAGES_ON_MENU = True
DISPLAY_LINKS_ON_MENU = True

LINK_ITEMS = (
    ("github", "https://github.com/rwev"),
    ("gitlab", "https://gitlab.com/rwev"),
    ("coyote.life", "http://coyote.life")
)

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

# PLUGINS
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "filetime_from_git",
    "autopages",
    "similar_posts",
    "neighbors",
    "section_number",
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

# photos
PHOTO_LIBRARY = "./content/assets/images"
PHOTO_EXIF_COPYRIGHT_AUTHOR = "rwev"
