import graphene as gp

class Book(gp.ObjectType):
    id = gp.ID(required=True)
    user_id = gp.ID(required=True)
    title = gp.String()
    description  = gp.String()
    urls = gp.List(gp.String)
    pass
    # id = gp.ID(required=True)

class Book_DB:
    mtype = 'book'
    tablename = 'books'

    @classmethod
    def table_statement(cls):
        statement = (f"""
        CREATE TABLE {cls.tablename}(
            _id varchar(30) PRIMARY KEY,
            user_id varchar(30),
            description text,
            
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            moddate datetime DEFAULT CURRENT_TIMESTAMP()
        )
        """)
        return statement