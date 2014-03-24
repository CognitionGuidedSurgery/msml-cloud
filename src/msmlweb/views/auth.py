__author__ = 'Alexander Weigl'

from flask_classy import FlaskView, route
from flask import *

from ..helper import logger
from ..model import user_exists

class AuthView(FlaskView):
    def index(self):
        return render_template("AuthView_index.html")


    @route("login", methods=['POST'])
    def login(self):
        name =  request.form['name']
        password = request.form['password']
        user = user_exists(name, password)
        logger.info(user)

        if user:
            session['loggedin'] = True
            session['user'] = {
                'name': user.name,
                'email': user.email,
            }
            flash("Successfully login.", "success")
            return redirect("/")
        else:
            flash("not user found with name/password", "error")
            return redirect(url_for("AuthView:index"))

    def logout(self):
        session['loggedin'] = None
        session['user'] = None
        return redirect(url_for('index'))

    def signup(self):
        #TODO
        pass




