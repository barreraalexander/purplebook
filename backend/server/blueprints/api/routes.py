from server import db, bcrypt, login_manager
from server.blueprints.graphql import RES_DICTS 
from server.schemas.book import Book_DB, schema as BookSchema
from server.schemas.user import User_DB, schema as UserSchema
from server.models.user import Auth_Model
from flask import Blueprint, request
from flask_login import logout_user, login_user
# from flask_login import login_user as authorize_user


api = Blueprint('api', __name__,
    url_prefix="/api")


@api.route('/test')
def test():
    return {'hey' : 'hi'}, 200

@api.route('/create_tables')
def create_tables():
    statement = Book_DB.table_statement()
    # statement = User_DB.table_statement()
    cur = db.connection.cursor()
    try:
        cur.execute(statement)
        db.connection.commit()
    except Exception as err:
        cur.close()
        print (err)
        return {'bad' : 'bad'}, 200


    return {'hey' : 'hi'}, 400

@api.route('/authorize_user', methods=['POST'])
def authorize_user():

    query = ""
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
        print (mdict)
        auth_model = Auth_Model(mdict)
        login_user(auth_model)
        return RES_DICTS['good']

 

    return RES_DICTS['error']