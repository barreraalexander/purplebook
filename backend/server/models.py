from server.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=False)
    urls = Column(String)
    background_gradient = Column(String) 

    moddate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    upldate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    def __str__(self):
        return f"""
        id: {self.id}
        title: {self.title}
        upldate: {self.upldate}
        moddate: {self.moddate}
        """

    # owner_id = Column(Integer, primary_key=True)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    verified = Column(Integer, nullable=False)
    books = Column(String)

    upldate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    moddate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


    def __str__(self):
        return f"""
        id: {self.id}
        email: {self.email}
        verified: {self.verified}
        books: {self.books}
        upldate: {self.upldate}
        moddate: {self.moddate}
        """