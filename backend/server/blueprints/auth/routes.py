from flask import Blueprint, request
from flask_login import login_required, login_user
from server.schemas.book import schema as BookSchema

from server import db, bcrypt, login_manager
from server.blueprints.graphql import RES_DICTS 
from server.schemas.user import User_DB, schema as UserSchema
from server.models.user import Auth_Model


auth = Blueprint("auth", __name__,
    url_prefix="/auth")


@auth.route('/login', methods=['POST'])
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
        else:            
            mdict = res.data['user_by_email']
            if bcrypt.check_password_hash(mdict['password'], input_pass):                
                auth_model = Auth_Model(mdict)
                login_user(auth_model)
                return RES_DICTS['good']

    return RES_DICTS['error']

@auth.route("/register", methods=['POST'])
def authorize_register():
        input_email = request.form.get('email')
        input_pass = request.form.get('password')
        input_name = request.form.get('name')

        query  = """
            mutation register {
                create_user(email:"%s", name:"%s", password:"%s") {
                    id
                    name
                    email
                    password
                }
            }
        """ % (input_email, input_name, input_pass)
        
        res = UserSchema.execute(query)

        if res.errors:
            print (res.errors)
            return RES_DICTS['error']

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