from flask_login import UserMixin
from server import login_manager, db

@login_manager.user_loader
def load_user(id):
    statement = "select * from users where id = '{}'".format(id)
    cursor = db.connection.cursor()
    cursor.execute(statement)
    record = cursor.fetchone()
    auth_model = Auth_Model(record)
    return auth_model


class Auth_Model(UserMixin):
    def __init__(self, mdict):
        self.id = mdict['id']
        self.email = mdict['email']
        self.password = mdict['password']
