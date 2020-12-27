from pathlib import Path

import environ

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

# AUTH_USER_MODEL = 'usr_auth0.User'
# =========================================
ALLOWED_HOSTS = []

# Application definition
# SESSION_ENGINE='utils.auth.django_jwt_cookie'
# JWT_USER_FIELDS= ['email', 'slug']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usr_auth0',
    'social_django',
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',

    ),
}

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
    # 'utils.auth.django_jwt_cookie.jwt_session_middleware'
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
    # 'utils.auth.BaseOAuth.Auth0',
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

# =================???SOCIAL_AUTH======================================

# LOGIN_URL = '/login/auth0'
# LOGIN_REDIRECT_URL = '/api/private'
# LOGOUT_REDIRECT_URL = '/api/public'
#
# SOCIAL_AUTH_TRAILING_SLASH = False  # Remove trailing slash from routes
# SOCIAL_AUTH_AUTH0_DOMAIN = 'edtube.us.auth0.com'
# SOCIAL_AUTH_AUTH0_KEY = env.str('SOCIAL_AUTH_AUTH0_KEY')
# SOCIAL_AUTH_AUTH0_SECRET = env.str('SOCIAL_AUTH_AUTH0_SECRET')
#
# SOCIAL_AUTH_AUTH0_SCOPE = [
#     'openid',
#     'profile',
#     'email'
# ]

# ======================================================
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

# ===============AUTH0============================
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
        # 'utils.auth.BaseOAuth.jwt_get_username_from_payload_handler',
    'JWT_DECODE_HANDLER':
        'utils.auth.utils.jwt_decode_token',
        # 'utils.auth.BaseOAuth.jwt_decode_token',
    'JWT_PUBLIC_KEY': PUBLIC_KEY,
    'JWT_ALGORITHM': 'RS256',
    'JWT_AUDIENCE': API_IDENTIFIER,
    'JWT_ISSUER': JWT_ISSUER,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
)
CORS_ALLOW_HEADERS = ['Authorization', ]

SECURE_SSL_REDIRECT = False
