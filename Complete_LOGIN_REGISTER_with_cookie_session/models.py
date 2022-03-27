__author__ = 'e.azizi'


from peewee import *

AuthenticationDB = MySQLDatabase("authenticationdb", host="localhost", port=3306, user="root", passwd="")



class AuthenticationModel(Model):
    class Meta:
        database = AuthenticationDB


class User(AuthenticationModel):
    username = CharField(unique=True)
    password = CharField()
    salt = CharField()


AuthenticationDB.connect()

AuthenticationDB.create_table(User,safe=True)