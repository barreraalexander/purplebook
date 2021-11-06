from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

from flask_graphql import GraphQLView



from server.db import DB
from server.configs import Config

login_manager = LoginManager()
login_manager.login_view = "auth.authorize_login"
login_manager.login_message_category = "info"

bcrypt = Bcrypt()
db = DB()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from server.blueprints.api.routes import api
    from server.blueprints.graphql.routes import graphql
    from server.blueprints.auth.routes import auth

    app.register_blueprint(api)
    app.register_blueprint(graphql)
    app.register_blueprint(auth)

    return app