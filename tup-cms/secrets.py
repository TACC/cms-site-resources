# TACC CMS Per-Site Resources - Configuration

# In a project-specific configuration file like this, edit existing configuration values from `cms-site-template:/taccsite_cms/default_secrets.py` that must change to suit this project.

# Until this custom configuration is automatically applied, to use it one must copy the content of it and append it to `cms-site-template:/taccsite_cms/secrets.py`

# TUP CONFIGURATION

########################
# DJANGO SETTINGS
########################

_LDAP_ENABLED = False

########################
# DJANGO CMS SETTINGS
########################

_CMS_TEMPLATES = (
    ('tup-cms/templates/fullwidth.html', 'Fullwidth')
)

########################
# GOOGLE ANALYTICS
########################

_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-96034853-2"
_GOOGLE_ANALYTICS_PRELOAD = True

########################
# BRANDING.
########################

_BRANDING = [_TACC_BRANDING, _UTEXAS_BRANDING]

########################
# LOGOS.
########################

_PORTAL_LOGO = [
    "tup",
    "tup-cms/img/org_logos/tacc-logo.svg",
    "",
    "/",
    "_self",
    "TACC Logo",
    "anonymous",
    "True"
]

_LOGO = _PORTAL_LOGO

########################
# PORTAL
########################

_PORTAL = False
