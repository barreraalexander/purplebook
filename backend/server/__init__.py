from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server import models
from server.database import engine
from server.routers.strawberry_book import gql as Book_Router
# from server.routers import auth, graphql, user

models.Base.metadata.create_all(bind=engine)

def create_app():
    origins = []

    app = FastAPI()

    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=origins,
    #     allow_methods=['*'],
    #     allow_headers=['*']
    # )

    app.include_router(Book_Router, prefix="/graphql")

    # app.include_router(user.router)
    # app.include_router(auth.router)
    # app.include_router(graphql.router)
    return app
