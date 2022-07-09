from flask_mysqldb import MySQL

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import json
from os import path

RUN_OPTIONS = {
    'LOCAL' : path.expanduser('~/etc/purplebook_config.json') ,
    'SERVER' : '/etc/purplebook_config_aws.json',
    'MOBILE' : path.expanduser('~/etc/mobile_config.json'),
}

RUNNING = RUN_OPTIONS['LOCAL']

with open(RUNNING) as config_file:
    config = json.load(config_file)


SQLALCHEMY_DATABASE_URL = 'postgresql://%s:%s@%s/%s' % (config.get("SQL_USER"), config.get("SQL_PASSWORD"), config.get("SQL_HOST"), config.get("SQL_DB"))

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal =  sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

def get_session():
    db = SessionLocal()
    return db



# class Config:
#     SECRET_KEY = config.get('SECRET_KEY')
#     MYSQL_USER = config.get('MYSQL_USER')
#     MYSQL_PASSWORD = config.get('MYSQL_PASSWORD')
#     MYSQL_HOST = config.get('MYSQL_HOST')
#     MYSQL_DB = config.get('MYSQL_DB')
#     MYSQL_CURSORCLASS = "DictCursor"

# class DB (MySQL):
#     def __init__(self, app=None):
#         super().__init__(app=app)