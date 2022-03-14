import environ

env = environ.Env(
    DEBUG=(bool, True),
    CACHE_URL=(str, "dummycache://"),
    SECRET_KEY=(str, r"a/qX:bn<hDcmm>Y<ow!PbX+B<%-StL)t[G\L_VZ1&p@$!zCVD"),
    ALLOWED_HOSTS=(list, []),
    DATABASE_URL=(str, "sqlite://:memory:"),
)

DEBUG = env.bool("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
SECRET_KEY = env("SECRET_KEY")
DATABASES = {
    "default": env.db(),
}

INSTALLED_APPS = [
    "service",
]
