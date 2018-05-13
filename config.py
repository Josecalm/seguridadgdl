import os
#comment q

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-shall-not-pass'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://pvsveqnlwbgkgu:d40e2a5d17cd9bb6ada3704e9fac72cf066bb9dd88f9d91e39b135328dd11826@ec2-54-83-1-94.compute-1.amazonaws.com:5432/devnegcng43thh'
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
