import peewee

DB = peewee.PostgresqlDatabase(
        "ranko", 
        host="localhost", 
        port=5432, 
        user="testuser", 
        password="testuser"
)



class BaseModel(peewee.Model):
    class Meta:
        database = DB


class User(BaseModel):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    salt = peewee.CharField()


DB.connect()
DB.create_tables([User,], safe=True)

