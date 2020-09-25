import os
import logging
from flask_bcrypt import Bcrypt

BASEDIR = os.path.abspath(os.path.dirname(__file__))
ENV = os.environ.get('ENV', 'dev')

# JWT Secret Key
SECRET_KEY = os.environ['SECRET_KEY']

# IMGUR Credentials
IMGUR_CLIENT_ID = os.environ['IMGUR_CLIENT_ID']
IMGUR_CLIENT_SECRET = os.environ['IMGUR_CLIENT_ID']

# DB Credentials
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["DB_NAME"]
SQL_CONNECTION_NAME = os.environ["SQL_CONNECTION_NAME"]


def create_engine_url(env):
    if env == 'dev':
        return 'sqlite:///' + os.path.join(BASEDIR, 'local.db') + '?check_same_thread=False'
    if env == 'test':
        return f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@127.0.0.1/{DB_NAME}"
    if env == 'prod':
        return f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?unix_socket=/cloudsql/{SQL_CONNECTION_NAME}"


DB_ENGINE_URL = create_engine_url(ENV)

# BCRYPT
BCRYPT = Bcrypt()

# Images directory
IMAGE_DIR = os.path.join(BASEDIR, 'images')
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)


# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

# Webpush configs

VAPID_PRIVATE_KEY = "HD1mPArkGyojcsSX4IIU8rhr4t5pXtrJlOmD3DUyHmg"

VAPID_CLAIMS = {
    "sub": "mailto:domain@example.com"
}


class Config:
    WTF_CSRF_CHECK_DEFAULT = False
    WTF_CSRF_ENABLED = False
    DEBUG = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_ENGINE_URL


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = DB_ENGINE_URL


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DB_ENGINE_URL


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
