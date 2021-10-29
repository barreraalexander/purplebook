from flask import Blueprint, request
from server.schemas.book import schema as BookSchema


auth = Blueprint("auth", __name__,
    url_prefix="/auth")

@auth.route("/login", methods=['POST'])
def authorize_login():
    if request.method=="POST":
        print ('posted')
        return (request.data)
        # return {'status' : 'good'}, 400
    return {'status' : 'bad'}, 200

@auth.route("/register")
def authorize_register():
    return {'status' : 'good'}, 400
    # pass


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
