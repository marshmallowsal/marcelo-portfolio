"""
Django settings for portfolio project.
"""

import os
from pathlib import Path

# Allow developers to put EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, and any other
# secrets in a local *.env* file (one key=value per line) so they don't have to
# export them manually every time.  The file can live at the project root (same
# folder as manage.py) and is ignored by Git.

try:
    from dotenv import load_dotenv

    # Look for a .env in BASE_DIR or one directory above (to cover typical
    # layouts).  load_dotenv will silently ignore the file if it doesn't exist,
    # which is fine in CI / production where environment variables are injected
    # differently.
    _base_dir = Path(__file__).resolve().parent.parent
    load_dotenv(_base_dir / '.env')
    load_dotenv(_base_dir.parent / '.env', override=False)
except ModuleNotFoundError:
    # python-dotenv isn't installed – that's okay; we'll rely on the host
    # environment variables instead.  Add `python-dotenv` to requirements.txt
    # if you'd like the automatic .env loading feature.
    pass

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-marcelo-portfolio-development-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.railway.app',
    '.up.railway.app',
    'marceloasalinasportfolio.com',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'

# Database
# Using SQLite for both development and production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise configuration for static files
# Using basic storage to avoid issues with missing font files
STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings for production
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# --- Email Configuration -----------------------------------------------------
# Switch from console backend (development-only) to a real SMTP backend so the
# "Send me a message" form can deliver mail to your Gmail inbox. All sensitive
# credentials are read from environment variables so they never get committed
# to source control.

# Put the following two variables in your local environment (e.g. an `.env`
# file loaded via `source .env` or by your process manager in production):
#   export EMAIL_HOST_USER="marceloa.salinas2@gmail.com"
#   export EMAIL_HOST_PASSWORD="<YOUR_GENERATED_APP_PASSWORD>"
#
# The password MUST be a "App Password" generated from your Google account
# (requires 2-factor authentication to be enabled). Normal account passwords no
# longer work with Gmail SMTP.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Pull credentials from the environment. If they are missing we fallback to an
# empty string so Django will raise a helpful error at startup instead of
# silently failing at runtime.
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

# Mail sent from the portfolio will show this address in the "From" field. We
# reuse the same Gmail account but you could supply any address that Gmail
# allows you to send as.
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ----------------------------------------------------------------------------- 