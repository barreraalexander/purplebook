from server.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=False)
    urls = Column(String, nullable=False, unique=False)
    background_gradient = Column(String, nullable=False, unique=False) 

    moddate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    upldate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    # owner_id = Column(Integer, primary_key=True)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    moddate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


