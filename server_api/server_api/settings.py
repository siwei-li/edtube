import os
from pathlib import Path

import environ
from pythonjsonlogger import jsonlogger

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env()

# import json
# from six.moves.urllib import request
# from cryptography.x509 import load_pem_x509_certificate
# from cryptography.hazmat.backends import default_backend

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env('DEBUG')

IP_PROD = env('IP_PROD')
ALLOWED_HOSTS = [IP_PROD,'127.0.0.1']

# Application definition
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'EXCEPTION_HANDLER': 'requestlogs.views.exception_handler',

}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usr_auth0',
    'video',
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'requestlogs.middleware.RequestLogsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
]

ROOT_URLCONF = 'server_api.urls'

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

# import logging
# from django.utils.timezone import now
# class CustomisedJSONFormatter(jsonlogger.JsonFormatter):
#     def json_record(self, message: str, extra: dict, record: logging.LogRecord):
#         extra['name'] = record.name
#         extra['filename'] = record.filename
#         extra['funcName'] = record.funcName
#         extra['msecs'] = record.msecs
#         if record.exc_info:
#             extra['exc_info'] = self.formatException(record.exc_info)
#
#         return {
#             'message': message,
#             'timestamp': now(),
#             'level': record.levelname,
#             'context': extra
#         }

LOG_ROOT = os.path.join(BASE_DIR, 'logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'requestlogs_to_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/requestlogs.log',
            # 'filename': os.path.join(LOG_ROOT, 'requestlogs.log'),
            'formatter': 'json_formatted'
        },
    },
    'loggers': {
        'requestlogs': {
            'handlers': ['requestlogs_to_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    'formatters': {
        'json_formatted': {'()':jsonlogger.JsonFormatter},
    },
}

WSGI_APPLICATION = 'server_api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'edtube',
#         'USER': 'root',
#         'HOST': '127.0.0.1',
#     }
# }
DATABASES = {
    'default': env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#===================AUTH0=============================
AUTH0_DOMAIN = 'edtube.us.auth0.com'
API_IDENTIFIER = 'https://edtube'
PUBLIC_KEY = None
JWT_ISSUER = 'https://edtube.us.auth0.com/'

# if AUTH0_DOMAIN:
#     jsonurl = request.urlopen('https://' + AUTH0_DOMAIN + '/.well-known/jwks.json')
#     jwks = json.loads(jsonurl.read().decode('utf-8'))
#     cert = '-----BEGIN CERTIFICATE-----\n' + jwks['keys'][0]['x5c'][0] + '\n-----END CERTIFICATE-----'
#     certificate = load_pem_x509_certificate(cert.encode('utf-8'), default_backend())
#     PUBLIC_KEY = certificate.public_key()
#     JWT_ISSUER = 'https://' + AUTH0_DOMAIN + '/'

JWT_AUTH = {
    'JWT_PAYLOAD_GET_USERNAME_HANDLER':
        'utils.auth.utils.jwt_get_username_from_payload_handler',
    'JWT_DECODE_HANDLER':
        'utils.auth.utils.jwt_decode_token',
    'JWT_PUBLIC_KEY': PUBLIC_KEY,
    'JWT_ALGORITHM': 'RS256',
    'JWT_AUDIENCE': API_IDENTIFIER,
    'JWT_ISSUER': JWT_ISSUER,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'https://localhost:8080',
    'https://edtube.netlify.app',

)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)
SECURE_SSL_REDIRECT = False
