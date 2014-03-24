__author__ = 'weigla'

from werkzeug.local import LocalProxy
import flask

def get_logger():
    return flask.current_app.logger

logger = LocalProxy(get_logger)
