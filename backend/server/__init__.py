from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server import models

from server.database import engine
from server.routers import auth, graphql, user

# from flask_graphql import GraphQLView



# from server.db import DB
# from server.configs import Config

# login_manager = LoginManager()
# login_manager.login_view = "auth.authorize_user"
# login_manager.login_message_category = "info"

# bcrypt = Bcrypt()
# db = DB()

def create_app():
    origins = []

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=['*'],
        allow_headers=['*']
    )

    # app.include_router(user.router)
    # app.include_router(auth.router)
    # app.include_router(graphql.router)
    return app

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     bcrypt.init_app(app)
#     db.init_app(app)
#     login_manager.init_app(app)

#     from server.blueprints.api.routes import api
#     from server.blueprints.graphql.routes import graphql
#     from server.blueprints.auth.routes import auth

#     app.register_blueprint(api)
#     app.register_blueprint(graphql)
#     app.register_blueprint(auth)

#     return app