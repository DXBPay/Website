
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPOSITORY_ROOT = os.path.dirname(BASE_DIR)



SECRET_KEY = 'd+-fe!8fdo##g^pb6$j=#x$en1yey+&*f1!c=p%0@j-(94avsv'

DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','dxbpay.cc','www.dxbpay.cc']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'simple_history',
    'django_tables2',
    'django_ajax',
    'django_filters',
    'crispy_forms',
    'django_crontab',
    'django_user_agents',
    'ckeditor',
    'ckeditor_uploader',
    
    'themesettings',
    'company',
    'auditable',
    'trade_perms',
    'modules',
    'locations',
    'trade_admin_auth',
    'trade_master',
    'trade_auth',
    'cryptotoken',
    'support',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'globalexperts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'globalexperts.wsgi.application'



LOCAL_DEV=False
STAGE =True
if LOCAL_DEV:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',   
            'PORT': '3306',
        }
    }
if STAGE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'databasename',
            'USER': 'username',
            'PASSWORD': 'passwd',
            'HOST': 'localhost',   
            'PORT': '3306',
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(REPOSITORY_ROOT, 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(REPOSITORY_ROOT, 'media/')

COMMON_ENCRYPTION_KEY='asdjk@15r32r1234asdsaeqwe314SEFT'
COMMON_16_BYTE_IV_FOR_AES='IVIVIVIVIVIVIVIV'

#MAIL Credential
EMAIL_USER = '2Okq9PD/vPBE34j63PKFAPmPkswnpJWZxzit7mCa+vc='
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_US = '2Okq9PD/vPBE34j63PKFAPmPkswnpJWZxzia='
EMAIL_PASSWORD = 'UAtklr/vYPi7EqGQRiKAPReBFfMxVv0Ciqi0acV8nzebP64/uYKhOBqTztRROdr+Bctw/J0z71kFEkgMw=='
EMAIL_USE_TLS = True
EMAIL_USE_SSL=False

DOMAIN_URL='www.dxbpay.cc'

from globalexperts.globalexperts_default_settings import *
from globalexperts.globalexperts_third_party_apps_settings import *
