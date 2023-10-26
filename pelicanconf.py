AUTHOR = 'loopasam'
SITENAME = 'Pixel Potluck'
SITEURL = ''

PATH = 'content'

# STATIC_PATHS = ['images', 'themes/simple-pixelpotluck/static']

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'English'

THEME = "themes/simple-pixelpotluck"

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 10

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

DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True