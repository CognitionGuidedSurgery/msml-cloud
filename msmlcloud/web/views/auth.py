__author__ = 'Alexander Weigl'

from flask_classy import FlaskView, route
from flask import *

from ..helper import logger
from msmlcloud.web.model import user_exists

from flask_login import  login_user, logout_user


class AuthView(FlaskView):
    def index(self):
        return render_template("AuthView_index.html")


    @route("login", methods=['POST'])
    def login(self):
        name =  request.form['name']
        password = request.form['password']
        user = user_exists(name, password)

        if user:
            login_user(user, remember=True)
            #session['loggedin'] = True
            session['user'] = {
                'name': user.name,
                'email': user.email,
            }
            flash("Successfully login.", "success")
            logger.info(request.args.get("next") or url_for("index"))
            return redirect(request.args.get("next") or url_for("index"))
        else:
            flash("not user found with name/password", "error")
            return redirect(url_for("AuthView:index"))

    def logout(self):
        session['loggedin'] = None
        session['user'] = None
        logout_user()
        return redirect(url_for('index'))

    def signup(self):
        #TODO
        pass




