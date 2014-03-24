__author__ = 'weigla'

from .shared import db

def initialize(app):
    with app.test_request_context():
        db.drop_all()
        db.create_all()


##
# functions
def hash_password(password, salt=True):
    if salt:
        password = SALT % password
    return password
    #TODO return hashlib.sha512(password.encode("ascii"))


def user_exists(users, name, password):
    def check(user):
        p = user.name == name and \
            user.salted_password == hash_password(password)
        print((user.name, name))
        print((user.salted_password, hash_password(password)))
        print(p)
        return p

    res = list(filter(check, users))
    print(res)
    return None if len(res) == 0 else res[0]
