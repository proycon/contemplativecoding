# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Maarten van Gompel (proycon)'
SITENAME = "Contemplative Coding"
SITESUBTITLE = "Meditations on language & technology"
SITEURL = 'http://proycon.github.io'
TIMEZONE = "Europe/Amsterdam"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

GITHUB_URL = 'http://github.com/proycon/'
DISQUS_SITENAME = "proytechblog"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2013, 11, 12, 14, 1, 1)

THEME = "/home/proycon/work/contemplativecoding/theme"

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = [('About me', 'http://proycon.anaproy.nl'),
             ('My Code', 'http://github.com/proycon'),
             ('Publications', 'http://proycon.anaproy.nl/publications') ]


FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = sorted([
        ('The dot on the ceiling', 'http://tdotc.wordpress.com/'),
        ('Folgert Karsdorp', 'http://fbkarsdorp.github.io'),
        ('Jeroen Janssens', 'http://jeroenjanssens.com/'),
        ('Mnmlist', 'http://mnmlist.com/'),
        ('Zen Habits', 'http://zenhabits.net'),
        ('Pythonic Perambulations', 'http://jakevdp.github.io/'),
        ('LingPipe Blog','http://lingpipe-blog.com/')
])

SOCIAL = (('github', 'http://github.com/proycon'),
          ('twitter', 'http://twitter.com/proycon'),
          ('youtube','http://youtube.com/proycon'),
          ('facebook','http://facebook.com/proycon'))

PLUGIN_PATH = '/home/proycon/pelican-plugins'
PLUGINS = []

# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

# path-specific metadata
#EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
#    }

# static paths will be copied without parsing their contents
#STATIC_PATHS = [
#    'pictures',
#    'extra/robots.txt',
#    ]

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

GITHUB_USER = 'proycon'
GITHUB_REPO_COUNT = 4
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Sharing
TWITTER_USER = 'proycon'
#GOOGLE_PLUS_USER = 'proycon'
GOOGLE_PLUS_ONE = False
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'false'

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
