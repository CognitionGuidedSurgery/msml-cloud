__author__ = 'Alexander Weigl'
from path import path

UPLOAD_FOLDER = path("uploads").abspath()
DATABASE_FILE = path("msmlweb.db").abspath()
STORAGE_DIR = path("storage").abspath()

class Config(object):
    UPLOAD_FOLDER = UPLOAD_FOLDER
    SECRET_KEY = "fdfsdafksdaöhaöhsdaöfsdahföiosdhaf"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % DATABASE_FILE