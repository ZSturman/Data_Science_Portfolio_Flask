
class Config(object):
    DEBUG = False
    TESTING = False
    
    EMAIL_ADDRESS = "zasturman@gmail.com"
    EMAIL_PASSWORD = "fuelczosdhmdqfzw"
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False

class DevelopmentConfig(Config):
    DEBUG = True