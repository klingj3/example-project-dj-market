"""
Django settings for market project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/

For deployment see https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret'

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['ssd-farmers-live-klingj3.c9users.io',
                 'localhost',
                 '127.0.0.1',
                 '[::1]']


# APP CONFIGURATION
# ---
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

INSTALLED_APPS = [
    'crispy_forms',
]

LOCAL_APPS = [
    'market',
    'market.apps.board',
]

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + INSTALLED_APPS + LOCAL_APPS


# MIDDLEWARE CONFIGURATION
# ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# DEBUG
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# FIXTURE CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-FIXTURE_DIRS
#FIXTURE_DIRS = (
#    os.path.join(BASE_DIR, 'fixtures'),
#)


# DATABASE CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# GENERAL CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#use-i18n
USE_I18N = False

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#use-tz
USE_TZ = True


# TEMPLATE CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/1.11/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/1.11/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/1.11/ref/templates/api/#loader-types
            #'loaders': [
            #    'django.template.loaders.filesystem.Loader',
            #    'django.template.loaders.app_directories.Loader',
            #],
            # See: https://docs.djangoproject.com/en/1.11/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# STATIC FILE CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'cache')

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
# STATICFILES_DIRS = []

# See: https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# MEDIA CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#media-url
MEDIA_URL = '/media/'


# URL CONFIGURATION
# ---
ROOT_URLCONF = 'market.urls'

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#wsgi-application
WSGI_APPLICATION = 'market.wsgi.application'


# PASSWORD STORAGE SETTINGS
# ---
# See https://docs.djangoproject.com/en/1.11/topics/auth/passwords/#using-argon2-with-django
#PASSWORD_HASHERS = [
#    'django.contrib.auth.hashers.Argon2PasswordHasher',
#    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
#    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
#    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
#    'django.contrib.auth.hashers.BCryptPasswordHasher',
#]


# PASSWORD VALIDATION
# ---
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# AUTHENTICATION CONFIGURATION
# ---
#AUTHENTICATION_BACKENDS = [
#    'django.contrib.auth.backends.ModelBackend',
#    'allauth.account.auth_backends.AuthenticationBackend',
#]

# Some really nice defaults
#ACCOUNT_AUTHENTICATION_METHOD = 'username'
#ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

#ACCOUNT_ALLOW_REGISTRATION = True
#ACCOUNT_ADAPTER = 'market.users.adapters.AccountAdapter'
#SOCIALACCOUNT_ADAPTER = 'market.users.adapters.SocialAccountAdapter'

# Custom user app defaults
# Select the correct user model
#AUTH_USER_MODEL = 'users.User'
#LOGIN_REDIRECT_URL = 'users:redirect'
#LOGIN_URL = 'account_login'

# SLUGLIFIER
# AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

########## CELERY
#INSTALLED_APPS += ['market.taskapp.celery.CeleryConfig']
#CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='django://')
#if CELERY_BROKER_URL == 'django://':
#    CELERY_RESULT_BACKEND = 'redis://'
#else:
#    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
########## END CELERY


# django-compressor
# ---
INSTALLED_APPS += ['compressor']
# COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)
STATICFILES_FINDERS += ['compressor.finders.CompressorFinder']

# django-libsass
# ---
# See: https://github.com/torchbox/django-libsass
LIBSASS_SOURCE_COMMENTS = False
# LIBSASS_OUTPUT_STYLE = 'compressed'

# Location of root django.contrib.admin URL
ADMIN_URL = r'^admin/'

# Geoposition settings
INSTALLED_APPS += ['geoposition']
GEOPOSITION_GOOGLE_MAPS_API_KEY = os.environ['GEOPOSITION_GOOGLE_MAPS_API_KEY']

# django-registration settings
INSTALLED_APPS += ['registration']  # Note that this has to come after our local apps to avoid template issues
ACCOUNT_ACTIVATION_DAYS = 365
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'blahblah@fakeemail.biz'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 1025

LOGIN_REDIRECT_URL = 'board:list'
