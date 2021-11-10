import graphene as gp
from server import db, bcrypt
from server.schemas.book import Book
from secrets import token_hex

class User(gp.ObjectType):
    id = gp.ID(required=True)
    name = gp.String()
    email = gp.String()
    password = gp.String()
    verified = gp.Int()
    books = gp.List(Book)


class Query(gp.ObjectType):
    user = gp.Field(User)
    user_by_id = gp.Field(User, id=gp.ID(required=True))
    user_by_email = gp.Field(User, email=gp.String(required=True))
    allusers = gp.List(User)

    def resolve_user_by_id(root, info, id):
        cursor = db.connection.cursor()
        statement = "select * from users where id = '{}'".format(id)
        cursor.execute(statement)
        record = cursor.fetchone()
        return record

    def resolve_user_by_email(root, info, email):
        cursor = db.connection.cursor()
        statement = "select * from users where email = '{}'".format(email)
        cursor.execute(statement)
        record = cursor.fetchone()
        return record

    def resolve_allusers(root, info):
        cursor = db.connection.cursor()
        statement = "select * from users"
        cursor.execute(statement)
        records = cursor.fetchall()
        return records


class CreateUser(gp.Mutation):
    class Arguments:
        name = gp.String()
        email = gp.String()
        password = gp.String()

    Output = User

    def mutate(root, info, name, email,
                password):
        insert_statement = """ INSERT INTO users
            (id, name, email, password)
        VALUES
            (%s, %s, %s, %s)
        """

        # crypt_pass = bcrypt.generate_password_hash(password)
        crypt_pass = bcrypt.generate_password_hash(password).decode('utf8')
        new_token = token_hex(8)

        insertions = (new_token, name,
                email, crypt_pass)

        cursor = db.connection.cursor()
        cursor.execute(insert_statement, insertions)
        db.connection.commit()

        check_statement = "select * from users where id = '{}'".format(new_token)
        cursor.execute(check_statement)
        new_record = cursor.fetchone()
   
        return new_record

class UpdateUser(gp.Mutation):
    class Arguments:
        id = gp.ID(required=True)
        name = gp.String(default_value=False)
        email = gp.String(default_value=False)
        books = gp.List(gp.String,default_value=False)

    Output = User

    def mutate(root, info, id,
            name, email, books):

        statement = "select * from users where id = '{}'".format(id)

        cursor = db.connection.cursor()
        cursor.execute(statement)
        record = cursor.fetchone()

        print (record)
        if name:
            record['name'] = name

        if email:
            record['email'] = email

        if email:
            record['books'] = books

        update_statement = """ UPDATE users
        SET
            name = %s,
            email = %s,
            books = %s,
            moddate = CURRENT_TIMESTAMP()
        WHERE id = %s
        """

        updates = (
            record['name'], record['email'],
            record['books'], record['id']
        )


        cursor.execute(update_statement, updates)
        db.connection.commit()
        return record

class DeleteUser(gp.Mutation):
    class Arguments:
        id = gp.ID(required=True)

    Output = User

    def mutate(root, info, id):
        cursor = db.connection.cursor()
        statement = "select * from users where id = '{}'".format(id)
        cursor.execute(statement)
        record = cursor.fetchone()

        delete_statement = "DELETE FROM users WHERE id = '{}' ".format(id)

        cursor = db.connection.cursor()
        cursor.execute(delete_statement)
        db.connection.commit()
        return record

class AddBook(gp.Mutation):
    class Arguments:
        id = gp.ID(required=True)
        book_id = gp.ID(required=True)

    def mutate(root, info, id, book_id):
        pass


class VerifyUser(gp.Mutation):
    class Arguments:
        id = gp.ID(required=True)

    Output = User

    def mutate(root, info, id):
        pass

class Mutation(gp.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class User_DB:
    mtype = 'user'
    tablename = 'users'

    @classmethod
    def table_statement(cls):
        statement = (f"""
        CREATE TABLE {cls.tablename}(
            id varchar(30) PRIMARY KEY,
            name varchar(30),
            email varchar(30) NOT NULL UNIQUE,
            password varchar(100) NOT NULL,
            verified int DEFAULT 0,
            books text,
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            moddate datetime DEFAULT CURRENT_TIMESTAMP()
        )    
        """)

        return statement

schema = gp.Schema(
    query=Query,
    mutation=Mutation,
    auto_camelcase=False
)