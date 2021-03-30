DEBUG = False

if env.str("DATABASE_URL", ""):
    DATABASES = {
        "default": env.db(),  # noqa F821
    }

HTTP_PROTOCOL = "https://"
