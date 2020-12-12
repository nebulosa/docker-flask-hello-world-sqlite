import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #flask-sqlalchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #per environment settings
    APP_ENVIRONMENT = os.environ.get('APP_ENVIRONMENT', 'development')

    if   APP_ENVIRONMENT == 'development':
        DEBUG   = True
        TESTING = True #disable recaptcha
    elif APP_ENVIRONMENT == 'production' :
        DEBUG  = False
