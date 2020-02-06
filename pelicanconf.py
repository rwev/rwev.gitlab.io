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
    ("resume", "https://gitlab.com/rwev/resume/raw/master/resume.pdf?inline=false"),
    ("github", "https://github.com/rwev"),
    ("gitlab", "https://gitlab.com/rwev"),
    ("tesseract", "/assets/pages/tesseract.html"),
    ("map", "/assets/pages/leaflet-map.html")
)

# BUILD PROCESS
DEFAULT_METADATA = {
    "author": OWNER,
    "status": "draft",  # status: published, draft, hidden
}

PATH = "content"
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["assets"]

EXTRA_PATH_METADATA = {
    'assets/extra/robots.txt': {'path': 'robots.txt'},
    'assets/extra/favicon.ico': {'path': 'favicon.ico'}
}

ARTICLE_PATHS = ["articles/published"]
OUTPUT_PATH = "./public"  # for gitlab page

TIMEZONE = "America/Denver"
DEFAULT_LANG = "en"

# PLUGINS
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "autopages",
    "deadlinks",
    'encrypt_content',
    "filetime_from_git",
    "gzip_cache",
    "more_categories",
    "neighbors",
    "photos",
    "section_number",
    "similar_posts",
    "sitemap",
    "summary"
]

# autopages
AUTOPAGES_PATH = os.path.join("content", "autopages")

AUTHOR_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "authors")
CATEGORY_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "categories")
TAG_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "tags")

# deadlinks
DEADLINK_OPTS = {
    'archive':  True,
    'classes': [], # TODO
    'labels':   False,
    'timeout_duration_ms': 1000,
    'timeout_is_error':    True,
}

# encrypt-content
ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted. Passcode required to view.'
}

# photos
PHOTO_LIBRARY = "./content/assets/images"
PHOTO_EXIF_COPYRIGHT_AUTHOR = "rwev"

PHOTO_THUMB = (500, 500, 50) # bumper

# sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.9,
        "pages": 0.8,
        "indexes": 0.7,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

