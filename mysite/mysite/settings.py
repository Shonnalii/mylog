########################################################
# Copyright (c) 2015 -- All rights reserved.
# Author: Haikent <hites.regar@shopclues.com>
# URL: http://www.haikent.com
#
# This file is part of the ShopClues Master catalogue project.
#
#############################################################

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$m-^q%n)l5gx1srdj8cr9dws2v)_*do!q3zfe1&=1!gwz)_yz7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#change this after production

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangotoolbox',
    'permission_backend_nonrel',
    'bootstrap3',
    'mathfilters',
    'polls',
]


# AUTHENTICATION_BACKENDS = (
    # 'mongoengine.django.auth.MongoEngineBackend',
    # 'django.contrib.auth.backends.ModelBackend'
# )

AUTHENTICATION_BACKENDS = (
        'permission_backend_nonrel.backends.NonrelPermissionBackend',
        )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/'],
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

WSGI_APPLICATION = 'catalog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DB_HOST = '180.179.172.154'
# DB_PORT = 27017
# DB_DATABASE = 'spmaster_live'
# DB_USERNAME = 'mongo'
# DB_PASSWORD = 'mongo@123'

DATABASES = {
   'default' : {
      'ENGINE' : 'django_mongodb_engine',
      'NAME' : 'admin',
      'HOST':'localhost', #'180.179.172.154',
      'PORT':27017,
      'OPTIONS' : {
            'socketTimeoutMS' : 5000,
            'connect':False,
        }
   },
   'cluesEye' : {
      'ENGINE' : 'django_mongodb_engine',
      'NAME' : 'cluesEye',
      #'USER': 'mongo',
      #'PASSWORD': 'mongo@123',
      'HOST':'localhost', #'180.179.172.154',
      'PORT':27017,
      'OPTIONS' : {
            'socketTimeoutMS' : 5000,
            'connect':False,
        }
   }
}
SITE_ID = '4d421623b0207acdc500001d'
# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'mastercatalog',
        # 'USER': 'root',
        # 'PASSWORD': 'haikent',
        # 'HOST': 'localhost',
        # 'PORT': '',
    # }
# }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'



###############################################################################




SP_SEARCH_IMG_API_BASE_URL = 'http://180.179.184.253:8080/rest/product/'
SP_SEARCH_IMG_API_USER = 'WF_ID_SHOPCLUES'
SP_SEARCH_IMG_API_PASS = 'gfuguyJvfFHGGHJG'


SP_API_URL = 'http://soa10.shopclues.com/v1/'
SP_AUTH_URL = 'http://auth4.shopclues.com/'

SOLRAPI = "http://api.shopclues.com/api/v11/similar_products?key=d42121c70dda5edfgd1df6633fdb36c0"
SEO_URL_BASE = "http://www.shopclues.com/"
IMAGE_URL = "http://cdn.shopclues.com/"


#shopclues local fqa data base ..........

SOA=  {
# "username":"19@sc.com",
# "password":"e10adc3949ba59abbe56e057f20f883e",
# "client_id":"10945358",
# "client_secret":"KM1LCWRT8E6P",
# "grant_type":"password"
"username":"shopcluesqa@gmail.com",
"password":"e10adc3949ba59abbe56e057f20f883e",
"client_id":"10945358",
"client_secret":"KM1LCWRT8E6P",
"grant_type":"password"
}

# local pc database
# MYSQLDBM = {
#            "host":'127.0.0.1',#"192.168.20.171",
#            "user":"root",#"production",
#            "password":"haikent",#"Pr0D#c@qa",
#            "database":"shopclue_cart"
#           }
#
# MYSQLDBS = {
#            "host":'127.0.0.1',#"192.168.20.171",
#            "user":"root",#"production",
#            "password":"haikent",#"Pr0D#c@qa",
#            "database":"shopclue_cart"
#           }
# MYSQLDBS_ANA = {
#                 "host":'127.0.0.1',#"192.168.20.171",
#                 "user":"root",#"production",
#                 "password":"haikent",#"Pr0D#c@qa",
#                 "database":"analytics"
#                 }
#
#
# MYSQLDBM_ANA = {
#                 "host":'127.0.0.1',#"192.168.20.171",
#                 "user":"root",#"production",
#                 "password":"haikent",#"Pr0D#c@qa",
#                 "database":"analytics"
#                 }


#local shopclues database
MYSQLDBM = {
           "host":"192.168.20.171",
           "user":"production",
           "password":"Pr0D#c@qa",
           "database":"shopclue_cart"
          }

MYSQLDBS = {
           "host":"192.168.20.171",
           "user":"production",
           "password":"Pr0D#c@qa",
           "database":"shopclue_cart"
          }
#
MYSQLMISC = {
           "host":"192.168.20.171",
           "user":"production",
           "password":"Pr0D#c@qa",
           "database":"shopclue_cart"
          }


MYSQLDBS_ANA = {
                "host":"192.168.20.171",
                "user":"production",
                "password":"Pr0D#c@qa",
                "database":"analytics"
                }


MYSQLDBM_ANA = {
                "host":"192.168.20.171",
                "user":"production",
                "password":"Pr0D#c@qa",
                "database":"analytics"
                }




CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "catalog.routing.channel_routing",
    },
}

SEVER_HOST_FLAG = "local"

# IT
# MYSQLMISC = {
#  'host' : 'qadbp1',
#  'database' : 'shopclue_cart',
#  'user' : 'misc_user',
#  'password' : 'M!sc@us3r'
#  }

#fqa database
# MYSQLDB = {
#            "host":'192.168.100.140',#"192.168.20.171",
#            "user":"test_user",#"production",
#            "password":"test@user",#"Pr0D#c@qa",
#            "database":"shopclue_cart"
#           }


################################################################################

