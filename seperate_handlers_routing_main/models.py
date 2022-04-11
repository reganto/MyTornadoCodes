__author__ = 'Reganto'

from peewee import *

AuthenticationDB = MySQLDatabase("authenticationdb", host="localhost",
port=3306, user="root", passwd="540689")

class AuthenticationModel(Model):
    class meta:
        database = AuthenticationDB

class User(AuthenticationModel):
    id = PrimaryKeyField()
    username = CharField(unique=True)
    password = CharField()

AuthenticationDB.connect()
AuthenticationDB.create_tabales([User,], safe=True)
