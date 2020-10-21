import configparser
import os

parser = configparser.SafeConfigParser(os.environ)
parser.read('settings/config.ini')


config = configparser.ConfigParser()

config.read('settings/config.ini')

ALIAS = config.get('DATABASE', 'ALIAS')
DB_NAME = config.get('DATABASE', 'NAME')
DB_HOST = config.get('DATABASE', 'HOST')

USER = config.get('AUTHENTICATION', 'USER')
PASSWORD = config.get('AUTHENTICATION', 'PASSWORD')

WEBSITE_COLLECTION = config.get('COLLECTIONS', 'WEBSITE')
