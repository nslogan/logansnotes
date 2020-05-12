#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# ---

# Set to help with plugin development
# LOAD_CONTENT_CACHE = False

# Add the plugin
PLUGIN_PATHS = ['plugins']
PLUGINS = ['lazyload']

# ---

AUTHOR = 'Logan Smith'
SITENAME = "Logan's Notes"
THEME = 'theme'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

PATH = 'content'
OUTPUT_PATH = 'site'
ARTICLE_PATHS = ['posts']

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

DRAFT_URL = 'drafts/posts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/posts/{slug}.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# None of these are supported by my site / template yet
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
FEED_SAVE_AS = ''

DEFAULT_METADATA = {
	'status': 'draft',
}

MENUITEMS = []

# Social widget
SOCIAL = [
	('GitHub','fab fa-github','https://github.com/nslogan/'),
	('LinkedIn','fab fa-linkedin-in','https://www.linkedin.com/in/logangsmith/'),
	('Twitter','fab fa-twitter','https://twitter.com/logangsmith'),
	('Instagram','fab fa-instagram','https://www.instagram.com/logangeoffsmith/'),
	('Strava','fab fa-strava','https://www.strava.com/athletes/31027767'),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

AUTHOR_SAVE_AS = ''

# https://python-markdown.github.io/extensions/smarty/
# https://python-markdown.github.io/extensions/md_in_html/
MARKDOWN = {
	'extension_configs': {
		'markdown.extensions.codehilite': {'css_class': 'highlight'},
		'markdown.extensions.extra': {},
		'markdown.extensions.meta': {},
		'markdown.extensions.smarty': {},
		'markdown.extensions.toc': {},
		'markdown_checklist.extension' : {},
		'markdown_captions' : {},
	},
	'output_format': 'html5',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
