__author__ = 'weigla'

from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from msmlcloud.web.model import User, FileEntry, db
admin = Admin(name="web-admin")


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(FileEntry, db.session))
