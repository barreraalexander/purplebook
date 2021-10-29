from flask import Blueprint
from server import db
from server.schemas.book import Book_DB
from server.schemas.user import User_DB

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


