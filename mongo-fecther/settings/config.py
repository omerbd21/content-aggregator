import configparser
import os

config = configparser.ConfigParser()

config.read('settings/config.ini')

ALIAS = config.get('DATABASE', 'ALIAS')
DB_HOST = os.environ.get('MONGO')

WEBSITE_COLLECTION = config.get('COLLECTIONS', 'WEBSITE')