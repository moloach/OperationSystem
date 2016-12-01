import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    FLASKY_MAIL_SUBJECT_PREFIX = '[]'
    FLASKY_MAIL_SENDER = ''
    FLASKY_ADMIN = os.environ.get('')