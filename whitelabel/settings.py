
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#DATA_DIR = BASE_DIR.parent / 'data' / 'web'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "8xxmq$kc3x2z*=*@f&0xk1^fgtb(p342)$gvafcrpp1=)jh@dl"

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = bool(int(os.getenv('DEBUG', 0)))

DEBUG = True


ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'whitelabel-solar.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'whitelabel'
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

ROOT_URLCONF = 'whitelabel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'home', 'templates/whitelabel/pages')],
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

WSGI_APPLICATION = 'whitelabel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mgl_base_dados',
#         'USER': 'usuario_mgl',
#         'PASSWORD': 'McqAdGu54NougOKPqxHvPjTNVUgYD8XI',  
#         'HOST': 'dpg-crutsju8ii6s738hnki0-a',
#         'PORT': '5432',
#         'CONN_MAX_AGE': 600,  # Conexões persistentes com o banco de dados
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Em produção (quando DEBUG é False), o Django coleta todos os arquivos estáticos aqui
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Diretório para salvar arquivos de mídia (uploads de usuários)
MEDIA_ROOT = os.path.join(BASE_DIR, '/data/web/media')

# Para permitir que o WhiteNoise sirva arquivos estáticos de forma otimizada
if not DEBUG:
    #STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Configurações adicionais de arquivo estático
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / 'home/static',
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'gouberg@gmail.com'
EMAIL_HOST_PASSWORD = 'mkfo pqfy reej jfyu'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER