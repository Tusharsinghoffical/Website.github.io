from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
# Make sure to override this in environment variables
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-l%y@vno^50mva&0r1qs34cgimeu_p197&s-g)88s)g!bimt99q')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1', 
    'freelancemrsingh.com', 
    'www.freelancemrsingh.com',
    'codewithmrsingh.tech', 
    'www.codewithmrsingh.tech'
]

# Database
# Use PostgreSQL in production
# For MongoDB
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'portfolio_db',
        'CLIENT': {
            'host': 'mongodb+srv://tushar2002:Tushar@2002@cluster0.np3np8j.mongodb.net/?appName=Cluster0',
            'username': 'tushar2002',
            'password': 'Tushar@2002',
            'authMechanism': 'SCRAM-SHA-256',
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Enable WhiteNoise for serving static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Email configuration for production
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'tusharsinghoffical@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'Portfolio Contact <tusharsinghoffical@gmail.com>')
CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL', 'tusharsinghoffical@gmail.com')

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 31536000
SECURE_REDIRECT_EXEMPT = []
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Additional security for CSRF
CSRF_TRUSTED_ORIGINS = [
    'https://freelancemrsingh.com',
    'https://www.freelancemrsingh.com',
    'https://codewithmrsingh.tech',
    'https://www.codewithmrsingh.tech'
]

# Cache settings for production
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# Session settings for production
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'