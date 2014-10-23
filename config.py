import os

SRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI="mysql://root:123456@localhost/flaskblog"

#: cache settings
# find options on http://pythonhosted.org/Flask-Cache/
CACHE_TYPE = 'simple'


