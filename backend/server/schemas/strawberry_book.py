import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import Depends
from server.database import get_db, get_session
from server import models
from sqlalchemy.orm import Session
import typing
from datetime import datetime

@strawberry.type
class Book:
    id : str
    title: str
    urls: typing.Optional[str]
    background_gradient: typing.Optional[str]
    moddate: datetime
    upldate: datetime

@strawberry.type
class Query:
    book: Book

    def resolve_book_by_id(id:str) -> Book:
        db = get_session()
        book = db.query(models.Book).filter(models.Book.id==id).first()
        return book
    
    book_by_id = strawberry.field(resolver=resolve_book_by_id)


    def resolve_allbooks() -> typing.List[Book]:
        db = get_session()
        books = db.query(models.Book).all()
        return books

    all_books: typing.List[Book] = strawberry.field(resolver=resolve_allbooks)


schema = strawberry.Schema(Query)
gql = GraphQLRouter(schema)