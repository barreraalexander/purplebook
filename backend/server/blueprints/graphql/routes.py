from flask import Blueprint
from server.schemas.book import schema as BookSchema
import json
# from 
graphql = Blueprint('graphql', __name__,
    url_prefix="/graphql")


@graphql.route('/test')
def test():
    return {'hey' : 'hi'}, 200



@graphql.route('/book_ep/<string:query>', methods=['POST', 'GET'])
def book_ep(_query):
    if request.method == "POST":
        post_request = jsonify(request.data)
        schema_data = json.dump(schema.execute(post_request['query']).data)
        # account for if post request failures 
        return schema_data


    return {'hey' : 'hi'}, 200

# @graphql.route('/book_ep/<string:query>', methods=['POST', 'GET'])
# def book_ep(_query):
#     if request.method == "POST":
#         post_request = jsonify(request.data)
#         schema_data = json.dump(schema.execute(post_request['query']).data)
#         # account for if post request failures 
#         return schema_data


#     return {'hey' : 'hi'}, 200




# @api.route('/gql/<string:query>', methods=['POST', 'GET'])
# def booker(_query):
#     post_request = jsonify(request.data)
#     # post_request = json.loads(request.data)
#     # schema_data = schema.execute(post_request)
#     # d
#     schema_data = json.dump(schema.execute(post_request['query']).data)

#     return (schema_data)
#     # return schema.execute()
#     pass

# # json looks like this for post request:

# {
#     "query" : "{ hello(age:99) }"
# }
