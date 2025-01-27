from datetime import timedelta

class config:
    SECRET_KEY = ''
    SQLALCHEMY_DATABSE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = ""
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)