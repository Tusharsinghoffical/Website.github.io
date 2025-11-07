from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
# Make sure to override this in environment variables
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-l%y@vno^50mva&0r1qs34cgimeu_p197&s-g)88s)g!bimt99q')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', '*']

# Database
# Use PostgreSQL in production
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME', 'portfolio_db'),
#         'USER': os.environ.get('DB_USER', 'portfolio_user'),
#         'PASSWORD': os.environ.get('DB_PASSWORD', 'secure_password'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '5432'),
#     }
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Email configuration for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'tusharsinghoffical@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'cprzfpsrgpaxlixa')
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