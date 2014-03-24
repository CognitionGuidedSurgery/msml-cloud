__author__ = 'weigla'


from flask import *
from flaskext.gravatar import Gravatar
from .model import *
from .views import *
from .vals import Config
import msmlweb.vals
from .admin import admin


app = Flask("msmlweb")
app.config.from_object(Config)
db.app = app
db.init_app(app)
admin.init_app(app)

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

AuthView.register(app)
FilesView.register(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')