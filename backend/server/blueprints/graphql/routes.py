from flask import Blueprint, request
from server.schemas.book import schema as BookSchema
from server.blueprints.graphql import RES_DICTS
import json

graphql = Blueprint('graphql', __name__,
    url_prefix="/graphql")

@graphql.route('/test')
def test():
    return {'hey' : 'hi'}, 200



@graphql.route('/book_ep', methods=['POST', 'GET'])
def book_ep():
    if request.method == "POST":
        data = json.loads(request.data)
        element = BookSchema.execute(data['query'])
        print ('ELEMENT')
        print (element)
        if element.errors:
            print (element.errors)
            return RES_DICTS['error']
        
    return element.data, 200

# @graphql.route('/book_ep', methods=['POST', 'GET'])
# def book_ep():
#     if request.method == "POST":
#         data = json.loads(request.data)
#         element = BookSchema.execute(data['query'])
#         print ('ELEMENT')
#         print (element)
#         if element.errors:
#             print (element.errors)
#             return RES_DICTS['error']
        
#     return element.data, 200
