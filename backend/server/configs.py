import json
from os import path

RUN_OPTIONS = {
    'LOCAL' : '/etc/purplebook_config.json' ,
    'SERVER' : '/etc/purplebook_config_aws.json',
    'MOBILE' : '~/etc/mobile_config.json',
}

RUNNING = RUN_OPTIONS['LOCAL']

with open(RUNNING) as config_file:
    config = json.load(config_file)

class Config:
    SECRET_KEY = config.get('SECRET_KEY')

    MYSQL_USER = config.get('MYSQL_USER')
    MYSQL_PASSWORD = config.get('MYSQL_PASSWORD')
    MYSQL_HOST = config.get('MYSQL_HOST')
    MYSQL_DB = config.get('MYSQL_DB')
    MYSQL_CURSORCLASS = "DictCursor"
