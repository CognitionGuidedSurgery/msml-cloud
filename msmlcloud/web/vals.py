# -*- encoding: utf-8 -*- 
__author__ = 'Alexander Weigl'
from path import path

UPLOAD_FOLDER = path("uploads").abspath()
DATABASE_FILE = path("web.db").abspath()
STORAGE_DIR = path("storage").abspath()

print(DATABASE_FILE)


class Config(object):
    UPLOAD_FOLDER = UPLOAD_FOLDER
    SECRET_KEY = "fdfsdafksdaöhaöhsdaöfsdahföiosdhaf"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % DATABASE_FILE

    DEBUG_TB_ENABLED	= True
    DEBUG = True
    #DEBUG_TB_HOSTS	Whitelist of hosts to display toolbar	any host
    DEBUG_TB_INTERCEPT_REDIRECTS = False #Should intercept redirects?	True
    #DEBUG_TB_PANELS	List of module/class names of panels	enable all built-in panels
    #DEBUG_TB_PROFILER_ENABLED	Enable the profiler on all requests	False, user-enabled
    #DEBUG_TB_TEMPLATE_EDITOR_ENABLED	Enable the template editor	Fa
