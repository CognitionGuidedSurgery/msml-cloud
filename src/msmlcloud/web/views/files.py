
__author__ = 'Alexander Weigl'

from ..model import *
from ..vals import STORAGE_DIR
from ..helper import logger

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from flask import  *
from flask_classy import  FlaskView, route
from flask_login import login_required

def allowed_file(filename):
    return True# return filename.endswith("zip")

class FilesView(FlaskView):
    def index(self):
        logger.info(get_flashed_messages())
        logger.info(get_flashed_messages(True))
        return render_template("list.html",
            file_entries = FileEntry.query.all()
        )

    @route("upload", methods = ["POST", "GET"])
    @login_required
    def upload(self):
        logger.info("upload msml file")
        logger.info(list(request.form.keys()))
        logger.info(list(request.files.keys()))

        name        = request.form.get('name', None)
        description = request.form.get('description', None)
        file = request.files.get('content', None)

        logger.info(file)

        logger.info("%s, %s, %s" %(name, description, file))

        if file and name and allowed_file(file.filename):
            assert isinstance(file, FileStorage)
            filename = secure_filename(file.filename)
            file.save(str(STORAGE_DIR / filename))
            fe = FileEntry(name = name, description = description)
            add_file_entry(fe)
            flash("File added.", "success")
        else:
            flash("Could not upload file: %s, %s" % (file, name), "error")

        return redirect("/files")


    @login_required
    def detail(self, name):
        return render_template("Files_detail.html", file = FileEntry.query.get(name))

    @login_required
    def add(self):
        return render_template("add_entry.html")