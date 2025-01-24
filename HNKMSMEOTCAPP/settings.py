"""
Django settings for HNKMSMEOTCAPP project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url  


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Initialise environment variables

#Your DEBUG setting should correctly evaluate to False in production:
DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ALLOWED_HOSTS = [
    'hnkmsm-eotc-lv-production.up.railway.app',  # Replace with your actual Railway app domain
    'localhost',
    '127.0.0.1', 
]
#CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = [
    'https://hnkmsm-eotc-lv-production.up.railway.app',  # Replace with your actual Railway app domain
]
#CROSS_ALLOWED_ORIGEN
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',  
    'http://127.0.0.1:8000',
    'https://hnkmsm-eotc-lv-production.up.railway.app',
]

#Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
CSRF_COOKIE_SECURE = True

#Set this to True to avoid transmitting the session cookie over HTTP accidentally.
SESSION_COOKIE_SECURE= True

# Application definition
INSTALLED_APPS = [
    # Built-in Django apps
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'corsheaders',
    'ckeditor',
    
    # Third-party
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    

    
    # local
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'projectVote.apps.ProjectvoteConfig',
    'services.apps.ServicesConfig',
    'schools.apps.SchoolsConfig',
    'members.apps.MembersConfig',
    'events.apps.EventsConfig',
    'multimedia.apps.MultimediaConfig',
    'blog.apps.BlogConfig',
    'marriage.apps.MarriageConfig',
    'payments.apps.PaymentsConfig',
    'shopProducts.apps.ShopProductsConfig',
    'massaging.apps.MassagingConfig'
    
]
SITE_ID = 1

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HNKMSMEOTCAPP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR/ 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # Add your context processor
                'pages.context_processors.cart_and_notifications',
            ],
        },
    },
]

WSGI_APPLICATION = 'HNKMSMEOTCAPP.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': os.environ['PASSWORD'],
        'HOST': 'autorack.proxy.rlwy.net',
        'PORT': 56986,
    }
}

AUTHENTICATION_BACKENDS = (
# Needed to login by username in Django admin, even w/o `allauth`
'django.contrib.auth.backends.ModelBackend',
# `allauth`-specific auth methods, such as login by e-mail
'allauth.account.auth_backends.AuthenticationBackend',
)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# AUTHENTICATION SETTINGS
AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'pages:homepage'

## django-allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'email' # Default: 'username'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1 # Default: 3
ACCOUNT_EMAIL_REQUIRED = True # Default: False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # Default: 'optional'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5 # Default: 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300 # Default 300
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login' # Default: '/'
ACCOUNT_USERNAME_REQUIRED = False # Default: True

#create a custom SignupForm class
ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'

# AUTHENTICATION SETTINGS
AUTH_USER_MODEL = 'users.CustomUser'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@gmail.com'  # Your Gmail account
# EMAIL_HOST_PASSWORD = 'your-app-password'  # App password or account password
# DEFAULT_FROM_EMAIL = 'your-email@gmail.com'

# EMAIL
SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD =  os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = 'temf2006@gmail.com'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_TZ = True

TIME_ZONE = 'UTC'  # or your desired timezone


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]
STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
WHITENOISE_MANIFEST_STRICT = False




# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')#BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

STRIPE_SECRET_KEY = os.environ['STRIPE_SECRET_KEY']
STRIPE_PUBLISHABLE_KEY = os.environ['STRIPE_PUBLISHABLE_KEY']
STRIPE_WEBHOOK_SECRET = os.environ['STRIPE_WEBHOOK_SECRET']
STRIPE_ENDPOINT_SECRET = os.environ['STRIPE_ENDPOINT_SECRET']

#Error Logging: You could add logging handlers to capture errors in production:
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# BOTTOM OF settings.py

#if os.environ.get('ENVIRONMENT') != 'production':
#  from .local_settings import *
