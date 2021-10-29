import graphene as gp

class User(gp.ObjectType):
    id = gp.ID(required=True)
    name = gp.String()
    email = gp.String()
    password = gp.String()
    verified = gp.Int()
    #correct version: books = gp.List(Book)
    books = gp.List(gp.String)

class Query(gp.ObjectType):
    pass

class User_DB:
    mtype = 'user'
    tablename = 'users'

    @classmethod
    def table_statement(cls):
        statement = (f"""
        CREATE TABLE {cls.tablename}(
            id varchar(30) PRIMARY KEY,
            name varchar(30),
            email varchar(30) NOT NULL,
            password varchar(30) NOT NULL,
            verified int DEFAULT 0,
            books text,
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            moddate datetime DEFAULT CURRENT_TIMESTAMP()
   
        )    
        """)

        return statement
