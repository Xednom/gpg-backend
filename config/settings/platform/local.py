import datetime

DEBUG = True

CORS_ORIGIN_WHITELIST = ["http://localhost:3000", "http://127.0.0.1:3000"]

FRONTEND_DOMAIN = "localhost:3000"

HTTP_PROTOCOL = "http://"

INTERNAL_IPS = [
    "127.0.0.1"
]

CRONJOBS = [
    ('* * * * *', 'django.core.management.call_command', ['send_queued_mail']),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'; \
                            SET foreign_key_checks = 0",
        },
    }
}