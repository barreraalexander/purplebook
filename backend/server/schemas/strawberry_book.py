import strawberry
from fastapi import status, HTTPException
from strawberry.fastapi import GraphQLRouter
from server.database import get_session
from server import models
import typing
from datetime import datetime


@strawberry.type
class Book:
    id: strawberry.ID
    title: str 
    urls: typing.Optional[typing.List[str]]
    background_gradient: typing.Optional[typing.List[str]]
    upldate: typing.Optional[datetime] = None
    moddate: typing.Optional[datetime] = None
    

@strawberry.type
class Query:
    book: Book

    def resolve_book_by_id(id:str) -> Book:
        db = get_session()
        book = db.query(models.Book).filter(models.Book.id==id).first()
        if (book.urls):
            book.urls = book.urls.split(',')
        else:
            book.urls = []

        if (book.background_gradient):
            book.background_gradient = book.background_gradient.split(',')
        else:
            book.background_gradient = []

        return book
    
    book_by_id: Book = strawberry.field(resolver=resolve_book_by_id)


    def resolve_allbooks() -> typing.List[Book]:
        db = get_session()
        books = db.query(models.Book).all()

        for book in books:
            if (book.urls):
                book.urls = book.urls.split(',')
            else:
                book.urls = []

            if (book.background_gradient):
                book.background_gradient = book.background_gradient.split(',')
            else:
                book.background_gradient = []

        return books

    all_books: typing.List[Book] = strawberry.field(resolver=resolve_allbooks)


@strawberry.type
class Mutation:

    @strawberry.mutation
    def add_book(self,
        title: str,
        urls: str="",
        background_gradient: str=""
        ) -> Book:

        db = get_session()
        new_book = models.Book(title=title, urls=urls)        


        db.add(new_book)
        db.commit()

        db.refresh(new_book)

        return new_book

    @strawberry.mutation
    def delete_book(self,
        id: str,
        ) -> Book:

        db = get_session()
        book_query = db.query(models.Book).filter(models.Book.id==id)
        book = book_query.first()

        if (not book):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book was not found")

        book_query.delete(synchronize_session=False)
        db.commit()

        return book

    @strawberry.mutation
    def update_book(self,
        id: str,
        title: str="",
        urls: str="",
        background_gradient: str="",
        ) -> Book:
        
        db = get_session()
        book_query = db.query(models.Book).filter(models.Book.id==id)
        book = book_query.first()

        if (not book):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work session was not found")

        if (title):
            book.title = title

        if (urls):
            book.urls = urls

        if (background_gradient):
            book.background_gradient = background_gradient

        book.moddate = datetime.utcnow()

        db.commit()
        db.refresh(book)

        return book


schema = strawberry.Schema(query=Query, mutation=Mutation)
gql = GraphQLRouter(schema)