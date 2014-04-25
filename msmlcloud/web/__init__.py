__author__ = 'weigla'

from flaskext.gravatar import Gravatar
from flask_login import LoginManager

from .model import *
from .views import *
from .vals import Config
from .admin import admin


app = Flask("msmlcloud.web")
app.config.from_object(Config)
# databse
db.app = app
db.init_app(app)

# admin
admin.init_app(app)

# login manager
login_manager = LoginManager(app)
login_manager.login_view = "AuthView:index"



@login_manager.user_loader
def load_user(userid):
    user = User.query.get(userid)
    if not user:
        raise Exception("could not find any user with %s" %user)
    return user

if not vals.DATABASE_FILE.exists():
    initialize(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)

AuthView.register(app)
FilesView.register(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')