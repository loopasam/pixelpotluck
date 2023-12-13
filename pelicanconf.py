AUTHOR = 'loopasam'
SITENAME = 'Pixel Potluck'
SITEURL = ''

ARTICLE_URL = 'recipes/{slug}/'
ARTICLE_SAVE_AS = 'recipes/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'

TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

PATH = 'content'


# STATIC_PATHS = ['images', 'themes/simple-pixelpotluck/static']

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'English'

THEME = "themes/simple-pixelpotluck"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True