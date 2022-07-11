from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server import models
from server.database import engine
from server.schemas.strawberry_book import gql as Book_Router
from server.schemas.strawberry_user import gql as User_Router
from server.routers.graphql import router as GQL_Router



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

    app.include_router(User_Router, prefix="/user")
    app.include_router(Book_Router, prefix="/book")
    app.include_router(GQL_Router, prefix="/gql")
 
    return app
