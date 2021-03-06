"""
Django settings for karya project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Root does not have to be hard coded every time due to this variable
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__)) + '/'

ADMINS = (
     ('Raghav Behl', 'raghavbehl@gmail.com'),
)

MANAGERS = ADMINS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder', 
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-479*!_ixurs_5ksiej@v4b04c9di6#-j&_7xg=iw828lf%)1l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'assignment',
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

ROOT_URLCONF = 'karya.urls'

WSGI_APPLICATION = 'karya.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'ddis0m82ofdiu3', 
        'USER': 'gofofjebpdlnis',
        'PASSWORD': 'imjL0EYgMaKjnTC3PTc6VEKCI2',
        'HOST': 'ec2-54-204-35-114.compute-1.amazonaws.com',
    }
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = PROJECT_ROOT + 'media/'

# URL that handles the media served from MEDIA_ROOT. 
#MEDIA_URL = '/media/'

AWS_STORAGE_BUCKET_NAME = "karya"
DEFAULT_FILE_STORAGE = 'karya.s3utils.MediaRootS3BotoStorage'
MEDIA_URL = "https://s3.amazonaws.com/karya/" 
AWS_ACCESS_KEY_ID = "AKIAJXCNJ2MPEP4LXYQA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_PRELOAD_METADATA = True 

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = PROJECT_ROOT + 'static/'
STATIC_URL = '/static/'

# URL to use if the authentication system requires a user to log in.
LOGIN_URL = '/login'

# Default URL to redirect to after a user logs in.
LOGIN_REDIRECT_URL = '/charts/apple'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)
