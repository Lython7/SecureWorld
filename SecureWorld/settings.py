"""
Django settings for SecureWorld project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i0@fl69b8fd&f&fztccvjqf=8vtvv-6$0pa#weosis$7y@3g7a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'xadmin',
    'crispy_forms',
    'reversion',
    'DjangoUeditor',

    'index',
    'uprofile',
]

AUTH_USER_MODEL='uprofile.Uprofile'


# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',# 标准username验证登录
#     'uprofile.authentication.EmailAuthBackend',# 邮箱作为用户名登录
#     'uprofile.authentication.CellphoneAuthBackend',# 手机号作为用户登录
# )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SecureWorld.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'SecureWorld.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

MySQLconfig = eval((os.getenv('mysql_config', None)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': MySQLconfig['USER'],
        'PASSWORD': MySQLconfig['PASSWD'],
        'HOST': MySQLconfig['HOST'],
        'PORT': MySQLconfig['PORT'],
        'NAME': 'SecureWorld',
    },
}

# CACHE_BACKEND = 'db://mycache'
# CACHE_TIME = 60 * 10
#
# SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 # 一周
# # SESSION_COOKIE_AGE = 30 # 30s
# SESSION_SAVE_EVERY_REQUEST = True
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True # 关闭浏览器，则COOKIE失效

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans' # 中文

TIME_ZONE = 'Asia/Shanghai' # 上海时区

USE_I18N = True

USE_L10N = False

USE_TZ = False # 选择Fasle使修改TIME_ZONE的时区生效。


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]


STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static') # 部署时需要使用

# 文件、图片上传路径
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# USE_L10N = False

DATETIME_FORMAT = 'Y-m-d H:i:s'

DATE_FORMAT = 'Y-m-d'