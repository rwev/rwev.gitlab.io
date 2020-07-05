#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
import os

sys.path.append(os.curdir)
from tundra.tundraconf import *

# TEMPLATE
OWNER = "rwev"
AUTHOR = OWNER
SITENAME = "~rwev"

SOURCE_CODE_URL = "https://gitlab.com/rwev/rwev.gitlab.io.git"
SITEURL = "localhost:8000"

TAGLINE = "pragmatic & principled"

DISPLAY_PAGES_ON_MENU = True
DISPLAY_LINKS_ON_MENU = True

LINK_ITEMS = (
    ("pgp", "F348 9370 83D4 EEB8", "/public_key.txt"),
    ("keybase", "rwev", "https://keybase.io/rwev"),
    ("gitlab", "rwev", "https://gitlab.com/rwev"),
    ("resume", "pdf", "https://gitlab.com/rwev/resume/raw/master/resume.pdf?inline=false"),
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
    'assets/extra/keybase.txt': {'path': 'keybase.txt'},
    'assets/extra/public_key.txt': {'path': 'public_key.txt'}
}

ARTICLE_PATHS = ["articles/published"]
OUTPUT_PATH = "./public"  # for gitlab page

TIMEZONE = "America/Denver"
DEFAULT_LANG = "en"

# PLUGINS
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "autopages",
    #    "css-html-js-minify",
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
    "summary",
    "webring"
]

# autopages
AUTOPAGES_PATH = os.path.join("content", "autopages")

AUTHOR_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "authors")
CATEGORY_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "categories")
TAG_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "tags")

# deadlinks
DEADLINK_OPTS = {
    'archive': True,
    'classes': [],  # TODO
    'labels': False,
    'timeout_duration_ms': 1000,
    'timeout_is_error': True,
}

# encrypt-content
ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted. Passcode required to view.'
}

# photos
PHOTO_LIBRARY = "./content/assets/images"
PHOTO_EXIF_COPYRIGHT_AUTHOR = "rwev"
PHOTO_ARTICLE = (1920, 1080, 90)

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

# webring

WEBRING_MAX_ARTICLES = 3
WEBRING_ARTICLES_PER_FEED = 1
WEBRING_SUMMARY_LENGTH = 128
WEBRING_CLEAN_SUMMARY_HTML = True
WEBRING_FEED_URLS = [
]
