__author__ = 'weigla'

from enum import Enum
from datetime import datetime

import hashlib

SALT = "%s"

class ExecutableState(Enum):
    RUNNING = "r"
    ERROR = "e"
    PAUSED ="P"
    STOPPED = "S"
    PENDING = "p"


class User(object):
    def __init__(self, name = None, email = None, password_clear = None, password_salted = None):
        self.name = name
        self.email = email
        if password_clear:
            self.salted_password = hash_password(password_clear)
        else:
            self.salted_password = password_salted

    def __repr__(self):
        return "msmlweb.sqlmodel.User(%s,%s,%s)" %(self.name, self.email, self.salted_password)

class FileEntry(object):
    def __init__(self, **kwargs):
        self.user_name = "weigl"
        self.date = datetime.now()
        self.last_run = ""
        self.state = ExecutableState.STOPPED
        self.name = ""
        self.size = ""
        self.content = ""

        self.__dict__.update(kwargs)



##
# functions
def hash_password(password, salt = True):
    if salt:
        password = SALT % password
    return password
    #TODO return hashlib.sha512(password.encode("ascii"))

def user_exists(users, name, password):
    def check(user):
        p =  user.name == name and  \
               user.salted_password == hash_password(password)
        print((user.name, name))
        print((user.salted_password, hash_password(password)))
        print(p)
        return p

    res =  list(filter(check, users))
    print(res)
    return None if len(res) == 0 else res[0]
