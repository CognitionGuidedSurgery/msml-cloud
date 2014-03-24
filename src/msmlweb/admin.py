__author__ = 'weigla'

from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView

admin = Admin(name="msmlweb-admin")


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

from .model import User, FileEntry, db
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(FileEntry, db.session))
