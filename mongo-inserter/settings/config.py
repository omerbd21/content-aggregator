import configparser

config = configparser.ConfigParser()

config.read('settings/config.ini')

ALIAS = config.get('DATABASE', 'ALIAS')
WEBSITE_COLLECTION = config.get('COLLECTIONS', 'WEBSITE')
