"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'v(m+i+73+!)vg*xxoi+o-bfzs5jk3i2c84_7!5*4p6hu2wq-nl'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'v(m+i+73+!)vg*xxoi+o-bfzs5jk3i2c84_7!5*4p6hu2wq-nl')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'django_extensions',
    'portfolio',
    'accounts',
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

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['main/templates'],
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ #static 파일들이 현재 어디에 흩뿌려져 있는지 쓰는 곳
     os.path.join(BASE_DIR, 'portfolio', "static"),
     os.path.join(BASE_DIR, 'main', 'static' )
    
 ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static') #static 파일들을 최종적으로 모아두는 곳

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# #기본 로그인 페이지 url, login_required 장식자 등에 의해서 사용
# LOGIN_URL = '/accounts/login/'
# #로그인 완료후 next 인자 지정시 해당 url로 이동 / 없으면 본 url로 이동
# LOGIN_REDIRECT_URL = '/accounts/profile/'

# #로그아웃 후 next page 인자 지정되지 않고 LOGOUT_REDIRECT_URL이 None 일 경우
# #redirect 수행하지 않고, 'registration/logged_out.html' 템플릿 렌더링
# LOGOUT_REDIRECT_URL = None

# #인증에 사용할 커스텀 User 모델 지정, '앱이름.모델명'
# AUTH_USER_MODEL = 'auth.User'

# #email activation keys 가 유효한 날짜
# ACCOUNT_ACTIVATION_DAYS = 2
# # EMAIL_HOST = 'localhost'
# # DEFAULT_FROM_EMAIL = 'webmaster@localhost'
# # LOGIN_REDIRECT_URL = '/'