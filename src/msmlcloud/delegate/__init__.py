__author__ = 'weigla'

doc = """
msml-delegate: pushes msml project into the working queue

Usage:
  msml-delegate upload <file/folder>
  msml-delegate result <uuid>
"""

import zipfile

import docopt

from msmlcloud.worker import *


def create_zip(folder, format="zip"):
    zfile = path(folder.name).abspath()
    #zfilehandle = zipfile.ZipFile(zfile, 'w')

    #for fl in folder.walkfiles():
    #    name = fl.relpathto(folder)
    #    zfilehandle.write(fl, name)
    #
    #zfilehandle.close()

    shutil.make_archive(zfile, format, folder, verbose=1, base_dir='/')
    return zfile


def do_upload(filename):
    pth = path(filename)

    if pth.isdir():
        pth = create_zip(pth)

    if not (pth.isfile() and zipfile.is_zipfile(pth)):
        raise Exception("not a zip file")


def main(options):
    if not options:
        options = docopt.docopt(doc)

    if options['upload']:
        do_upload(options['<file/folder>'])
    elif options['result']:
        get_results(options['<uuid>'])


if __name__ == '__main__': main()