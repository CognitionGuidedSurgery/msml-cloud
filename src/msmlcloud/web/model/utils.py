__author__ = 'weigla'

from msmlcloud.web.model.shared import db
from msmlcloud.web.model.definitions import *

def initialize(app):
    db.drop_all()
    db.create_all()

    user = User("weigl", "spamling@web.de", "123")
    db.session.add(user)


    fe = FileEntry()
    fe.author = user
    fe.uploaded = datetime.now()
    fe.last_run= datetime.now()
    fe.name="Test file #1"
    fe.asset = "liver.zip"
    fe.state="error"
    fe.description="test debug entry"
    db.session.add(fe)

    fe = FileEntry()
    fe.author = user
    fe.uploaded = datetime.now()
    fe.last_run= datetime.now()
    fe.name="Test file #2"
    fe.asset = "liver.zip"
    fe.state="success"
    fe.description="test debug entry"
    db.session.add(fe)

    fe = FileEntry()
    fe.author = user
    fe.uploaded = datetime.now()
    fe.last_run= datetime.now()
    fe.name="Test file #3"
    fe.asset = "liver.zip"
    fe.state="paused"
    fe.description="test debug entry"
    db.session.add(fe)


    db.session.commit()


##
# functions
def hash_password(password, salt=True):
    if salt:
        password = SALT % password
    return password
    #TODO return hashlib.sha512(password.encode("ascii"))


def user_exists(name, password):
    user = User.query.filter_by(name=name, password=password).first()
    print("found %s" % user)
    return user

