from pathlib import Path

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^cdjre+d8%r$##xm*9kg2juy*3x(!lvyd#c0en)ki_u*9b#_vb"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
