from flask import Blueprint, request
from flask_login import login_required
from server.schemas.book import schema as BookSchema

from server import db, bcrypt, login_manager
from server.blueprints.graphql import RES_DICTS 
from server.schemas.user import User_DB, schema as UserSchema
from server.models.user import Auth_Model
from flask import Blueprint, request
from flask_login import logout_user, login_user

auth = Blueprint("auth", __name__,
    url_prefix="/auth")


@auth.route('/authorize_user', methods=['POST'])
def authorize_user():
    if request.method=='POST':
        input_email = request.form.get('email')
        input_pass = request.form.get('password')

        query  = """
            query auth {
                user_by_email(email:"%s") {
                    id
                    email
                    password
                }
            }
        """ % (input_email)
        
        res = UserSchema.execute(query)

        if res.errors:
            print (res.errors)
            return RES_DICTS['error']

        mdict = res.data['user_by_email']
        auth_model = Auth_Model(mdict)
        login_user(auth_model)
        return RES_DICTS['good']
    return RES_DICTS['error']

@auth.route("/register")
def authorize_register():
    return RES_DICTS['error']


@auth.route("/logout")
@login_required
def logout():
    try:
        logout_user()
        return RES_DICTS['good']

    except Exception as err:
        print (err)
        return RES_DICTS['error']