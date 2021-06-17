# TACC CMS Per-Site Resources - Configuration

# In a project-specific configuration file like this, edit existing configuration values from `cms-site-template:/taccsite_cms/default_secrets.py` that must change to suit this project.

# Until this custom configuration is automatically applied, to use it one must copy the content of it and append it to `cms-site-template:/taccsite_cms/secrets.py`

# PROTX CONFIGURATION

########################
# DJANGO SETTINGS
########################

_LDAP_ENABLED = True

########################
# DJANGO CMS SETTINGS
########################

_CMS_TEMPLATES = (
    ('protx-cms/templates/fullwidth.html', 'Fullwidth')
)

########################
# GOOGLE ANALYTICS
########################

_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-125525035-##"
_GOOGLE_ANALYTICS_PRELOAD = True

########################
# BRANDING.
########################

_BRANDING = [_NSF_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING]

########################
# LOGOS.
########################

_PORTAL_LOGO = [
    "protx",
    "protx-cms/img/org_logos/protx-logo-temp.png",
    "",
    "/",
    "_self",
    "ProTX Logo",
    "anonymous",
    "True"
]

_LOGO = _PORTAL_LOGO

########################
# PORTAL
########################

_PORTAL = True
