from os import environ


TG_TOKEN = environ.get("TG_TOKEN", '')
ADMINS = environ.get("ADMINS", '').split(',')
DEBUG = environ.get('DEBUG', False).lower() == 'true'
DATABASE = environ.get('DATABASE', 'sqlite:///:memory:')

DOMAIN = environ.get('DOMAIN', None)
WEBHOOK_PATH = f'/webhook/{TG_TOKEN}'
WEBHOOK_URL = f'{DOMAIN}{WEBHOOK_PATH}'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = environ.get('PORT', 0)
