"""
Django settings for gtb project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import django_heroku
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a1o)%kmvx(8npji-p26z@i3-a^qed(p9h-4*wz8thub4=r#k@&'
GOOGLE_RECAPTCHA_SECRET_KEY = '6LfRUtwZAAAAADMZVtT8gvTOoflEfEP0g6d7GJb2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False



ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gtb.urls'

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

TEMPLATE_CONTENT_PROCESSOR=(
    "django.core.content_processors.auth",
    "django.core.content_processors.debug",
    "django.core.content_processors.i18n",
    "django.core.content_processors.media",
    "django.core.content_processors.request",
)

WSGI_APPLICATION = 'gtb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newhotel',
        'USER':'root',
        'PASS': '',
        'HOST':'localhost',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')

STATIC_URL = '/static/'



BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = (os.path.join(BASE_DIR, "website/static"), )

MEDIA_ROOT = (BASE_DIR)

MEDIA_URL = '/media/'

CKEDITOR_CONFIGS = {'default': {'toolbar_Full': [['Styles', 'Format', 'Bold', 'Italic', 'Underline',
                                                  'Strike', 'SpellChecker', 'Undo', 'Redo'], ['Link',
                                                'Unlink', 'Anchor'],['Image', 'Iframe', 'Table', 'HorizontalRule'],
                                                 ['TextColor', 'BGColor'],['Smiley', 'SpecialChar'], ['Source'],
                                                 ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
                                                 ['NumberedList','BulletedList'],['Indent','Outdent'],['Maximize'],
                                                 ],'extraPlugins': 'justify,liststyle,indent',},}


LOGIN_URL="loginpage"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "royalcontinentalhotell@gmail.com"
EMAIL_HOST_PASSWORD = "anjuhaanda123"
EMAIL_PORT = "465"
EMAIL_USE_SSL = True

django_heroku.settings(locals())