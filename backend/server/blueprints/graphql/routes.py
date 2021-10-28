from flask import Blueprint

graphql = Blueprint('graphql', __name__,
    url_prefix="/graphql")


@graphql.route('/test')
def test():
    return {'hey' : 'hi'}, 200