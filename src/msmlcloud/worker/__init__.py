__author__ = 'weigla'

import sys
# requires msml source file
sys.path.insert(0, "../msml/src")

from celery import Celery
from .config import *
from msml.run import *
from StringIO import StringIO
from path import path
import shutil

REPOSITORY = path("storage")
WORKING_DIR = path("evaluate")

app = Celery(CELERY_NAME,
             backend=CELERY_RESULT_BACKEND,
             broker=BROKER_URL)
#
## for testing
@app.task
def hello(): return "Hello World"


@app.task
def add(i, j): return i + j

#
from .backend import *
#
##
def get_repo_file(filename):
    if filename.endswith(".zip"):
        f = filename
    else:
        f = "%s.zip" % filename
    return REPOSITORY / f


def get_working_folder(filename):
    return path(WORKING_DIR / filename.namebase)


def populate_from_repo(filename):
    if not get_repo_file(filename).exists():
        raise Exception()

    fldr = get_working_folder(filename)
    if fldr.exists():
        shutil.rmtree(fldr)

    fldr.mkdir()
    shutil.unpack_archive(filename, fldr, 'zip')
    return fldr


def msml_remote_frontend(file, exporter):
    fldr = populate_from_repo(file)
    msmlfile = fldr.files('.msml.xml')
    msml = CloudApp(files=msmlfile, exporter=exporter)
    capture = StringIO()
    a, sys.stdout = sys.stdout, capture
    msml.execution()
    sys.stdout = a
    return capture.getvalue()


def upload_zip(filename, filecontent):
    p = REPOSITORY / filename
    with open(p, 'wb') as h:
        h.write(filecontent)