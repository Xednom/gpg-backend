DEBUG = False

ALLOWED_HOSTS = ["gpgstaging.pythonanywhere.com"]

CORS_ALLOWED_ORIGINS = ["https://gpg-staging.vercel.app"]

MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

INSTALLED_APPS += (
    "debug_toolbar",
)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

DEBUG_TOOLBAR_PANELS = (
    # Defaults
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "gpgstaging$default",
        "USER": "gpgstaging",
        "PASSWORD": "fishmond22",
        "HOST": "gpgstaging.mysql.pythonanywhere-services.com",
        "PORT": "3306",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# for management command;
# see https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = (
    os.path.join(BASE_DIR, 'staticfiles')
)

HTTP_PROTOCOL = "https://"

# SSL/TLS SETTINGS FOR DJANGO
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SECURE_SSL_HOST = True
SECURE_HSTS_SECONDS = 1000000
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

SECURE_REFERRER_POLICY = "same-origin"

ADMIN_EMAIL = ["lightwizard20@gmail.com", "xednom@gmail.com"]