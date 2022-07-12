import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
from server.schemas.strawberry_book import Book
import typing
from datetime import datetime
from database import get_session
from server import models

@strawberry.type
class User:
    id: strawberry.ID
    email: str
    password: str
    verified: int
    books: typing.Optional[typing.List[Book]]
    upldate: typing.Optional[datetime] = None
    moddate: typing.Optional[datetime] = None


@strawberry.type
class Query:
    user: User

    def resolve_user_by_id(id:str) -> User:
        db = get_session()
        user = db.query(models.User).filter(models.User.id==id).first()

        return user

    def resolve_allusers() -> typing.List[User]:
        db = get_session()
        # user = db.query(models.User).filter(models.User.id==id).first()
        users = db.query(models.User).all()

        return users


@strawberry.type
class Mutation:
    
    @strawberry.mutation
    def add_user(self) -> User:
        pass

    @strawberry.mutation
    def delete_user(self) -> User:
        pass

    @strawberry.mutation
    def update_user(self) -> User:
        pass




schema = strawberry.Schema(
        Query,
        # config=StrawberryConfig(auto_camel_case=False)
    )

gql = GraphQLRouter(schema)