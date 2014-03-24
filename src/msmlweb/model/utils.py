__author__ = 'weigla'

from .shared import db
from .definitions import *

def initialize(app):
    db.drop_all()
    db.create_all()

    user = User("weigl", "spamling@web.de", "123")

    fe = FileEntry()
    fe.author = user.id
    fe.uploaded = datetime.now()
    fe.last_run= datetime.now()
    fe.name="Test file #1"
    fe.asset = "liver.zip"
    fe.state="error"
    fe.description="test debug entry"

    db.session.add(user)
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

