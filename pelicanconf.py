from datetime import datetime

AUTHOR = 'Alvaro Ortiz'
SITENAME = 'Data-Gizmo'
SITEURL = 'http://alvaroof.github.io'
SITETITLE = "Data-Gizmo"
# SITESUBTITLE = "The minimalist Pelican theme"
# SITEDESCRIPTION = "Flex - The minimalist Pelican theme."
# SITELOGO = ''
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

# ROBOTS = "index, follow"

#THEME = "Flex"
#THEME = "pelican-blue"
THEME = "pelican-bootstrap3"

PATH = "content"
OUTPUT_PATH = "output"
TIMEZONE = "Europe/Madrid"

# DISABLE_URL_HASH = True

MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['i18n_subsites', nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
#MAIN_MENU = True
#HOME_HIDE_TAGS = True

SOCIAL = (
    ("github", "https://github.com/alvaroof"),
    ("linkedin", "https://linkedin.com/in/alvaroof"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

#DISQUS_SITENAME = "flex-pelican"
#ADD_THIS_ID = "ra-55adbb025d4f7e55"

#STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]

#EXTRA_PATH_METADATA = {
#    "extra/ads.txt": {"path": "ads.txt"},
#    "extra/CNAME": {"path": "CNAME"},
#}

# THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
# THEME_COLOR_ENABLE_USER_OVERRIDE = True

# USE_LESS = True

# pelican-blue
# SIDEBAR_DIGEST = 'Programmer and Web Developer'
# FAVICON = 'url-to-favicon'
# DISPLAY_PAGES_ON_MENU = True
# TWITTER_USERNAME = 'twitter-user-name'
# MENUITEMS = (('Blog', SITEURL),)