
import os
from pathlib import Path

from _socket import gethostname, gethostbyname

# from novel_api import load_env
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
# Load Secrets
# load_env.load_env()
# Load .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

ENVIRONMENT = os.environ.get("ENVIRONMENT")

if ENVIRONMENT in ["Production", "Staging", "Test"]:
    ALLOWED_HOSTS = [
        gethostname(),
        gethostbyname(gethostname()),
        os.environ.get("HTTPS_URL_1"),
        os.environ.get("HTTPS_URL_2")
    ]

    CORS_ALLOWED_ORIGINS = [
        os.environ.get("HTTPS_APP_URL_1"),
        os.environ.get("HTTPS_APP_URL_2"),
    ]

    CSRF_TRUSTED_ORIGINS = [
        os.environ.get("HTTPS_APP_URL_1"),
        os.environ.get("HTTPS_APP_URL_2")
    ]

elif ENVIRONMENT == "Development":
    ALLOWED_HOSTS = [
        gethostname(),
        gethostbyname(gethostname()),
        os.environ.get("HTTPS_URL_1"),
        os.environ.get("HTTPS_URL_2")
    ]

    CORS_ALLOWED_ORIGINS = [
        os.environ.get("HTTPS_APP_URL_1"),
        os.environ.get("HTTPS_APP_URL_2"),
        "http://localhost:3000"
    ]

    CSRF_TRUSTED_ORIGINS = [
        os.environ.get("HTTPS_APP_URL_1"),
        os.environ.get("HTTPS_APP_URL_2"),
        "http://localhost:3000"
    ]

else:
    ALLOWED_HOSTS = ["127.0.0.1"]

    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:3001",
    ]

    CSRF_TRUSTED_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:3001",
    ]

# Bỏ dấu / cuối mỗi url
APPEND_SLASH = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'novel_api',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'novel_api.urls'

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

WSGI_APPLICATION = 'novel_api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


if os.environ.get("LOCAL", "True").lower() == "true":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('PGDATABASE'),
            'USER': os.environ.get('PGUSER'),
            'PASSWORD': os.environ.get('PGPASSWORD'),
            'HOST': os.environ.get('PGHOST'),
            'PORT': os.environ.get('PGPORT', 5432),
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
