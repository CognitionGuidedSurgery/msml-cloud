__author__ = 'weigla'


from flask import *
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from path import path
from .model import *

import os


UPLOAD_FOLDER = path("uploads").abspath()
storage_dir = path("storage").abspath()

app = Flask("msmlweb")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "fdfsdafksdaöhaöhsdaöfsdahföiosdhaf"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///msmlweb.db'
db.init_app(app)


## debug:
#len(db['users']) == 0 and \
#db['users'].append( User("weigl", "weigl@his", "123") )

def allowed_file(filename):
    return True# return filename.endswith("zip")

@app.route("/files/")
def list_msml_files():
    app.logger.info(get_flashed_messages())
    app.logger.info(get_flashed_messages(True))

    return render_template("list.html", file_entries=db['files'])


@app.route("/credentials")
def show_form_sign():
    return render_template("credentials.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if "signin" in request.form:
        name =  request.form['name']
        password = request.form['password']
        app.logger.info((name, password, db['users']))

        user = user_exists(db['users'], name, password)
        app.logger.info(user)

        if user:
            session['loggedin'] = True
            session['user'] = user.__dict__
            flash("Successfully login.", "success")
        else:
            flash("not user found with name/password", "error")
            return redirect("/credentials")

    elif "signup" in request.form:
        #TODO
        pass

    return redirect("/")

@app.route('/logout')
def logout():
    session['loggedin'] = None
    session['user'] = None
    return redirect(url_for('index'))


@app.route("/files/upload/", methods = ["POST", "GET"])
def upload_msml_file():
    app.logger.info("upload msml file")
    app.logger.info(list(request.form.keys()))
    app.logger.info(list(request.files.keys()))

    name        = request.form.get('name', None)
    description = request.form.get('description', None)
    file = request.files.get('content', None)

    app.logger.info(file)

    app.logger.info("%s, %s, %s" %(name, description, file))

    if file and name and allowed_file(file.filename):
        assert isinstance(file, FileStorage)
        filename = secure_filename(file.filename)
        file.save(str(storage_dir / filename))
        fe = FileEntry(name = name, description = description)
        add_file_entry(fe)
        flash("File added.", "success")
    else:
        flash("Could not upload file: %s, %s" % (file, name), "error")

    return redirect("/files")


@app.route("/files/detail/<name>")
def detail_msml(name):
    return render_template("list.html", file_entries=file_entries)


@app.route("/files/add")
def add_msml_file():
    return render_template("add_entry.html")


# controllers
#@app.route('/favicon.ico')
#def favicon():
#    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/")
def index():
    return render_template('index.html')