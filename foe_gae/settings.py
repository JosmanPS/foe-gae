"""
Django settings for foe_gae project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.contrib import messages

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# REMOTE_CLOUD_SQL == false: Local MySQL
# REMOTE_CLOUD_SQL == true:  Remote Cloud SQL (test database)
REMOTE_CLOUD_SQL = False
PROD_S0A = False

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eeqlp06e6xs63ze6hpj#@z9$ah(ci*jji)0hy$b6jn6s=x^@8d'

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'foe',

    # Third-parties
    'crispy_forms',
    'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Registration settings
REGISTRATION_OPEN = True                # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'foepruebas@gmail.com'
EMAIL_HOST_PASSWORD = 'foe#2015'
EMAIL_PORT = 465

# Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

ROOT_URLCONF = 'foe_gae.urls'

WSGI_APPLICATION = 'foe_gae.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'


if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # No debugging in production
    DEBUG = False

    # Production, Cloud SQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/foe-platform:foe-db',
            'NAME': 'foe_db',
            'USER': 'root',
        }
    }

    IS_PROD = True
    
else:

    IS_PROD = False
    
    # Debugging in development
    DEBUG = True

    # Development: MySQL
    # - database:  score_group
    # - user:      score_group
    # - password:  score_group_password
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'NAME': 'foe_db',
            'USER': 'foe',
            'PASSWORD': 'foe_password',
        }
    }

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

LANGUAGES = (
    ('es', 'es'),
)

# MESSAGES
MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error'
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

CRISPY_FAIL_SILENTLY = not DEBUG

if IS_PROD:
    DEFAULT_FILE_STORAGE = 'foe_gae.storage.GoogleCloudStorage'
