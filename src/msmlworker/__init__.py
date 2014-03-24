__author__ = 'weigla'

from celery import Celery
from .config import *

app = Celery("msmlworker",
                 broker=BROKER_URL)

@app.task
def hello():
    return 'Hello World'


if __name__ == "__main__":
    pass




