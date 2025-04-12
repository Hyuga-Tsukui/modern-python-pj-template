"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
from typing import TypedDict

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class AppEnvironmentSettings(BaseSettings):
    """
    Settings for the Django application.
    """

    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: SecretStr


try:
    app_env_settings = AppEnvironmentSettings()  # pyright: ignore[reportCallIssue]
except Exception as e:
    raise RuntimeError("Failed to load environment settings. Please check your environment variables.") from e


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-k+&v^6f&rgr0yi#1c6@q_d@so&%f^2%ziw5tr89zf*3@f%%wg#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS: list[str] = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"


class TemplateOptions(TypedDict, total=False):
    """
    TypedDict for template options.
    """

    context_processors: list[str]


class TemplateSettings(TypedDict):
    """
    TypedDict for template settings.
    """

    BACKEND: str
    DIRS: list[str]
    APP_DIRS: bool
    OPTIONS: TemplateOptions


TEMPLATES: list[TemplateSettings] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


class DatabaseOptions(TypedDict):
    """
    TypedDict for database options.
    """

    ENGINE: str
    NAME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int


class DatabaseSettings(TypedDict):
    """
    TypedDict for database settings.
    """

    default: DatabaseOptions


DATABASES: DatabaseSettings = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "USER": app_env_settings.MYSQL_USER,
        "HOST": app_env_settings.MYSQL_HOST,
        "PORT": app_env_settings.MYSQL_PORT,
        "NAME": app_env_settings.MYSQL_DATABASE,
        "PASSWORD": app_env_settings.MYSQL_PASSWORD.get_secret_value(),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
