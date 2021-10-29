import graphene as gp

class Book(gp.ObjectType):
    id = gp.ID(required=True)
    user_id = gp.ID(required=True)
    title = gp.String()
    description  = gp.String()
    urls = gp.List(gp.String)
    moddate = gp.Date()
    upldate = gp.Date()

class Query(gp.ObjectType):
    book = gp.Field(Book)
    allbooks = gp.List(Book)

    def resolve_book(root, info):
        cursor = db.connection.cursor()
        elem_id = info.context['id']
        statement = "select * from books where _id = '{}'".format(elem_id)
        cursor.execute(statement)

        record= cursor.fetchone()
        mdict = {
            'id' : record['id'],
            'user_id' : record['user_id'],
            'title' : record['title'],
            'description' : record['description'],
            'urls' : record['urls'],
            'upldate' : record['upldate'],
            'moddate' : record['moddate']   
        }
        return Book(**mdict)

    def resolve_allbooks(root, info):
        cursor = db.connection.cursor()

        statement = "select * from books"
        cursor.execute(statement)

        all_records = cursor.fetchall()

        return all_records

class Mutation(gp.Mutation):
    class Arguments:
        id = gp.ID(required=True)
        user_id = gp.ID(required=True)
        title = gp.String()
        description  = gp.String()
        urls = gp.List(gp.String)
        moddate = gp.Date()
        upldate = gp.Date()
        # id = 

    ok = gp.Boolean()
    book = gp.Field(lambda : Book)

    def mutate(root, info):
        book = Book(id=id,
            user_id=user_id,
            title=title,
            description=description,
            urls=urls,
            moddate=moddate,
            upldate=upldate,
            )
        ok = True
        return Mutation(book=book, ok=ok)

class CreateBook(gp.ObjectType):
    new_book = Mutation.Field()


class Book_DB:
    mtype = 'book'
    tablename = 'books'

    @classmethod
    def table_statement(cls):
        statement = (f"""
        CREATE TABLE {cls.tablename}(
            id varchar(30) PRIMARY KEY,
            user_id varchar(30),
            description text,
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            moddate datetime DEFAULT CURRENT_TIMESTAMP()
        )
        """)
        return statement

schema = gp.Schema(query=Query,auto_camelcase=False, mutation=CreateBook)