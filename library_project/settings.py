from pathlib import Path

import os
import dj_database_url
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5j5i)%l!a6i4wg=dz$fcy^i-8222p(35rmf_53-q435mb-zj#%'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# Application definition

INSTALLED_APPS = [
    'index',
    'dashboard',
    'library_app',
    'rest_framework',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'library_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'library_project.wsgi.application'

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    from dotenv import load_dotenv
    
    load_dotenv(os.path.join(BASE_DIR, '.env'))
except ImportError:
    
    pass

DATABASE_URL = os.environ.get('DATABASE_URL')

print(f"DEBUG: DATABASE_URL leída del entorno: {DATABASE_URL}")

if DATABASE_URL:
    DATABASES = {
        #'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=True,)
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


#DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'library-project-1-tkid.onrender.com', '.onrender.com']

CSRF_TRUSTED_ORIGINS = ['https://library-project-dp42.onrender.com', 'https://*.onrender.com']

# Configuración de CORS
CORS_ALLOWED_ORIGINS = [
    "https://library-project-dp42.onrender.com", 
    "https://library-project-1-tkid.onrender.com", 
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

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

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#AUTHENTICATION_EMAIL
AUTH_USER_MODEL = 'library_app.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}