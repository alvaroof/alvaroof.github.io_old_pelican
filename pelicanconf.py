# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3

from datetime import datetime

AUTHOR = 'Alvaro Ortiz'
SITENAME = 'Data-Gizmo'
HIDE_SITENAME = True
SITEURL = 'http://alvaroof.github.io'
#SITELOGO = 'images/my_site_logo.jpg'
#SITELOGO_SIZE = 80
#FAVICON = 'images/my_site_logo.jpg'
#AVATAR='images/avatar.jpg'
#ABOUT_ME="I am a Physicist recycled into Data Scientist"
PADDED_SINGLE_COLUMN_STYLE = False
BANNER = 'images/banner-2.jpg'
BANNER_SUBTITLE = 'This is my subtitle for my Banner'
BANNER_ALL_PAGES = False

PATH = "content"
OUTPUT_PATH = "output"
TIMEZONE = "Europe/Madrid"

BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "default" #check on https://pygments.org/demo/
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = 'flatly' # https://bootswatch.com/
BOOTSTRAP_FLUID = True
DISPLAY_BREADCRUMBS=True
DISPLAY_CATEGORY_IN_BREADCRUMBS=True
BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_ARTICLE_INFO_ON_INDEX=False
RELATED_POSTS_MAX = 5

MARKUP = ("md", "ipynb")
from pelican_jupyter import markup as nb_markup
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites', 'related_posts', 'series', nb_markup]
IGNORE_FILES = [".ipynb_checkpoints"]

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False

SOCIAL = (
    ("github", "https://github.com/alvaroof"),
    ("linkedin", "https://linkedin.com/in/alvaroof"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

#DISPLAY_TAGS_ON_SIDEBAR = False
#DISPLAY_TAGS_INLINE = False
#TAGS_URL='tags.html'
DISPLAY_CATEGORIES_ON_SIDEBAR=False
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
RECENT_POST_COUNT=5
DISPLAY_ARCHIVE_ON_SIDEBAR=False
DISPLAY_AUTHORS_ON_SIDEBAR=False

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

# # Tell Pelican to add files from 'extra' to the output dir
# STATIC_PATHS = [
#   'images',
#   'extra',
#   "extra/CNAME"
# ]

# # Tell Pelican to change the path to 'static/custom.css' in the output dir
# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'static/css/custom.css'},
#     'extra/custom.js': {'path': 'static/js/custom.js'},
#     "extra/CNAME": {"path": "CNAME"}
# }

# custom CSS and JS
# CUSTOM_CSS = 'static/css/custom.css'
# CUSTOM_JS = 'static/js/custom.js'

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
# FEED_ALL_ATOM
# FEED_ALL_RSS
# DISPLAY_PAGES_ON_MENU
# DISPLAY_CATEGORIES_ON_MENU
# MENUITEMS
# LINKS

# Analytics & Comments
# GOOGLE_ANALYTICS
# GOOGLE_ANALYTICS_UNIVERSAL
# GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY
# DISQUS_SITENAME
# PIWIK_URL
# PIWIK_SSL_URL
# PIWIK_SITE_ID
# TAG_CLOUD_MAX_ITEMS