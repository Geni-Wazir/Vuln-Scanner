from scanner import app, db, bcrypt, admin, get_admin
from flask_admin.contrib.sqla import ModelView
from scanner.model import User

# app.app_context().push()
# db.create_all()


class ScannerAdminView(ModelView):
    def is_accessible(self):
        if current_user.email in admins_list:
            return True
        else:
            return False

admin.add_view(ScannerAdminView(User, db.session))

@app.route('/')
def hello_world():
    return 'hello world!'

