from datetime import datetime
from scanner import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    isadmin = db.Column(db.Boolean, nullable=False, default=False)
    profile_image = db.Column(db.String(20), nullable=False, default='profile.jpg')
    password = db.Column(db.String(60), nullable=False)
    scan_available = db.Column(db.Integer, nullable=False, default=0)
    # audit = db.relationship('Audit', backref='Auditor', lazy=True, cascade="all, delete")

    def __repr__(self):
        return "User('{}', '{}', '{}', '{}')".format(self.username, self.email, self.profile_image, self.scan_available)

