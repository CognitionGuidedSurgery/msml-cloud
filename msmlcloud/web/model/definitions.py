__author__ = 'Alexander Weigl'

from datetime import datetime

from msmlcloud.web.model.shared import db

SALT = "%s"


class User(db.Model, object):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=True)

    files = db.relationship("FileEntry", backref="author")

    def __init__(self, name=None, email=None,
                 password_clear=None, password_salted=None):
        self.name = name
        self.email = email
        if password_clear:
            self.password = (password_clear)
        else:
            self.password = password_salted

    def __repr__(self):
        return "web.model.User(%s,%s,%s)" % (
            self.name, self.email, self.password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class FileEntry(db.Model, object):
    __tablename__ = "files"

    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(1000))

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    uploaded = db.Column(db.DateTime)
    last_run = db.Column(db.DateTime)
    asset = db.Column(db.String(1000))
    state = db.Column(db.Enum('paused', 'error', 'pending', 'success',
                              name='filestates'))

    def __init__(self, **kwargs):
        uploaded = datetime.now()
        self.__dict__.update(kwargs)
