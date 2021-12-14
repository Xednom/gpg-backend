"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    "grappelli",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

LOCAL_APPS = [
    "apps.authentication",
    "apps.core",
    "apps.gpg",
    "apps.account",
    "apps.accounting",
    "apps.timesheet",
    "apps.due_diligence",
    "apps.newsfeed",
    "apps.operational_cost",
    "apps.resolution",
    "apps.task_designation",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "djoser",
    "rest_framework",
    "django_filters",
    "anymail",
    "post_office",
    "django_extensions",
    "django_crontab",
    "djmoney",
    "import_export",
    "rangefilter",
    "django_bleach",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Manila"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/config/staticfiles/"

AUTH_USER_MODEL = "authentication.User"

SITE_ID = 1

DJOSER = {
    "SEND_CONFIRMATION_EMAIL": True,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "users/reset_password_confirm/{uid}/{token}",
    "ACTIVATION_URL": "auth/users/activation/{uid}/{token}",
    # TODO: set SEND_ACTIVATION_EMAIL to true when the new fix has arrived
    # currently when updating a user the system sends an activation link to
    # the registered email
    # "SEND_ACTIVATION_EMAIL": True,
    "HIDE_USERS": True,
    "SERIALIZERS": {
        "user_create": "apps.authentication.serializers.UserRegistrationSerializer",
        "user": "apps.authentication.serializers.UserListSerializer",
        "current_user": "apps.authentication.serializers.CurrentUserSerializer",
    },
    "EMAIL": {
        "confirmation": "apps.authentication.views.GpgConfirmationEmail",
        "password_reset": "apps.authentication.views.GpgPasswordResetEmail",
    },
}

POST_OFFICE = {
    "BACKENDS": {"default": "anymail.backends.sendinblue.EmailBackend"},
    "DEFAULT_PRIORITY": "now",
}

GRAPPELLI_ADMIN_TITLE = "G.P.G Corp. Management System"

# Email sender credentials
ANYMAIL_SENDINBLUE_API_KEY = env.str("ANYMAIL_SENDINBLUE_API_KEY")
EMAIL_BACKEND = "post_office.EmailBackend"
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
# SERVER_EMAIL = "xednom@gmail.com"

EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = 587
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True


# Which HTML tags are allowed
BLEACH_ALLOWED_TAGS = [
    "p",
    "b",
    "i",
    "u",
    "em",
    "a",
    "ol",
    "strong",
    "blockquote",
    "span",
    "code",
    "address",
    "article",
    "aside",
    "footer",
    "header",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hgroup",
    "main",
    "nav",
    "section",
    "dd",
    "div",
    "dl",
    "dt",
    "figcaption",
    "figure",
    "hr",
    "main",
    "pre",
    "a",
    "abbr",
    "b",
    "bdi",
    "bdo",
    "br",
    "cite",
    "code",
    "data",
    "dfn",
    "kbd",
    "mark",
    "q",
    "rb",
    "rp",
    "rt",
    "rtc",
    "ruby",
    "s",
    "samp",
    "small",
    "sub",
    "sup",
    "time",
    "u",
    "var",
    "wbr",
    "caption",
    "col",
    "colgroup",
    "table",
    "tbody",
    "td",
    "tfoot",
    "th",
    "thead",
    "tr",
    "img",
]

# Which HTML attributes are allowed
BLEACH_ALLOWED_ATTRIBUTES = ["href", "title", "style"]

# Which CSS properties are allowed in 'style' attributes (assuming
# style is an allowed attribute)
BLEACH_ALLOWED_STYLES = [
    "font-family",
    "font-size",
    "font-weight",
    "text-decoration",
    "font-variant",
    "color",
]

BLEACH_ALLOWED_PROTOCOLS = ["http", "https", "data"]

# Strip unknown tags if True, replace with HTML escaped characters if
# False
BLEACH_STRIP_TAGS = True

# Strip comments, or leave them in.
BLEACH_STRIP_COMMENTS = False

MEDIA_ROOT = "media"
MEDIA_URL = env.str("MEDIA_URL", "http://127.0.0.1:8000/media/")

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = "delete"

PAYPAL_API_KEY_CLIENT_ID_SANDBOX = env.str("PAYPAL_API_KEY_CLIENT_ID_SANDBOX")
PAYPAL_API_KEY_SECRET_SANDBOX = env.str("PAYPAL_API_KEY_SECRET_SANDBOX")
PAYPAL_API_KEY_CLIENT_LIVE = env.str("PAYPAL_API_KEY_CLIENT_LIVE")
PAYPAL_API_KEY_SECRET = env.str("PAYPAL_API_KEY_SECRET")

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
