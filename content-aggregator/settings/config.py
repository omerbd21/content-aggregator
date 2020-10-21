import configparser

config = configparser.ConfigParser()
config.read('settings/config.ini')

HTTP_PREFIX = config.get('WEB', 'PREFIX')
