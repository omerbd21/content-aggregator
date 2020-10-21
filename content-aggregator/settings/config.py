import configparser

config = configparser.ConfigParser()


HTTP_PREFIX = config.get('WEB', 'PREFIX')
