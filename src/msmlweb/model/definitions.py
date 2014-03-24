__author__ = 'Alexander Weigl'

from .shared import db

from enum import Enum
from datetime import datetime

import hashlib
SALT = "%s"


class User(db.Model, object):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=True)

    def __init__(self, name=None, email=None,
                 password_clear=None, password_salted=None):
        self.name = name
        self.email = email
        if password_clear:
            self.password = (password_clear)
        else:
            self.password = password_salted

    def __repr__(self):
        return "msmlweb.model.User(%s,%s,%s)" % (
            self.name, self.email, self.password)


class FileEntry(db.Model, object):
    __tablename__ = "files"

    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(1000))
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    uploaded = db.Column(db.DateTime)
    last_run = db.Column(db.DateTime)
    asset = db.Column(db.String(1000))
    state = db.Column(db.Enum('paused', 'error', 'pending', 'success',
                              name='filestates'))

    def __init__(self, **kwargs):
        uploaded = datetime.now()
        self.__dict__.update(kwargs)
