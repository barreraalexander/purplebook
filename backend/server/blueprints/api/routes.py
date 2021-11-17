from server import db, bcrypt
from server.blueprints.graphql import RES_DICTS 
from server.schemas.book import Book_DB, schema as BookSchema
from server.schemas.user import User_DB, schema as UserSchema
from server.models.user import Auth_Model
from flask import Blueprint, request

api = Blueprint('api', __name__,
    url_prefix="/api")


@api.route('/test')
def test():
    return {'hey' : 'hi'}, 200

@api.route('/create_tables')
def create_tables():
    statement = Book_DB.table_statement()
    cur = db.connection.cursor()

    try:
        cur.execute(statement)
        db.connection.commit()
    except Exception as err:
        cur.close()
        print (err)
        return {'bad' : 'bad'}, 200


    return {'hey' : 'hi'}, 400

