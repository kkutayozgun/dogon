
import os
import environ
from django.utils.translation import ugettext_lazy as _

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

ROOT_DIR = environ.Path(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default='^+1+w^dq2awfpmbpef!9&mie%3-mt^_wctgdl9f#3nd)6yrk*v')

DEBUG = env.bool("DEBUG", False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party Apps:
    'ckeditor',

    # Project Apps
    'page',
    'seotr',
    'seoen',
]

DATABASES = {
    'default': env.db('DB_URL', default='sqlite:///db.sqlite3')
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dogon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'page.context_processors.categories_processor',
                'page.context_processors.googleapikey_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'dogon.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


LANGUAGE_CODE = env('LANGUAGE_CODE', default="tr")

TIME_ZONE = env('TIME_ZONE', default='Europe/Istanbul')

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'), )

STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')

MEDIA_ROOT = os.path.join(BASE_DIR,'public/media')

MEDIA_URL = '/media/'


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

LANGUAGES = (
    ('tr', _('Türkçe')),
    ('en', _('İngilizce')),
)

LANGUAGE_SESSION_KEY = 'language'

ADMIN_URL = env('ADMIN_URL', default="admin/")

GOOGLE_API_KEY = env('GOOGLE_API_KEY', default='')