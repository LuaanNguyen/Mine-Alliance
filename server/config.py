import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
