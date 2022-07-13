import strawberry
from strawberry.fastapi import GraphQLRouter
from server.schemas.strawberry_book import Book
import typing
from datetime import datetime
from server.database import get_session
from server import models
from fastapi import status, HTTPException

@strawberry.type
class User:
    id: strawberry.ID
    name: str
    email: str
    password: str
    verified: typing.Optional[int] = 0
    upldate: typing.Optional[datetime] = None
    moddate: typing.Optional[datetime] = None


@strawberry.type
class Query:
    user: User

    def resolve_user_by_id(id:str) -> User:
        db = get_session()
        user = db.query(models.User).filter(models.User.id==id).first()

        return user

    user_by_id: User = strawberry.field(resolver=resolve_user_by_id)


    def resolve_allusers() -> typing.List[User]:
        db = get_session()
        users = db.query(models.User).all()

        return users

    all_users: typing.List[User] = strawberry.field(resolver=resolve_allusers)


@strawberry.type
class Mutation:
    
    @strawberry.mutation
    def add_user(self,
        name: str,
        email: str,
        password: str,
        verified: int=0
        ) -> User:
        
        db = get_session()
        new_user = models.User(name=name, email=email, password=password, verified=verified)

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user


    @strawberry.mutation
    def delete_user(self,
        id: str    
        ) -> User:
        
        db = get_session()
        user_query = db.query(models.User).filter(models.User.id==id)
        user = user_query.first()

        if (not user):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user was not found")

        user_query.delete(synchronize_session=False)
        db.commit()

        return user


    @strawberry.mutation
    def update_user(self,
        id: str,
        name: str="",
        email: str="",
        password: str="",        
        ) -> User:

        db = get_session()

        user_query = db.query(models.User).filter(models.User.id==id)
        user = user_query.first()

        if (not user):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work session was not found")

        if (name):
            user.name = name

        if (email):
            user.email = email

        if (password):
            user.password = password

        
        user.moddate = datetime.utcnow()

        db.commit()
        db.refresh(user)        

        return user




schema = strawberry.Schema(
        query=Query,
        mutation=Mutation
        # config=StrawberryConfig(auto_camel_case=False)
    )

gql = GraphQLRouter(schema)