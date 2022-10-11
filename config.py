import os

class Config(object):
    SECRET_KEY = 'background-eraser'
    UPLOAD_FOLDER = 'static\images'

class DevelopmentConfig(Config):
    DEBUG = True