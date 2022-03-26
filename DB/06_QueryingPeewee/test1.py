__author__ = 'admin'




from playhouse.migrate import *
import peewee


db = MySQLDatabase('people',host="localhost",user="testuser",passwd="")
migrator = MySQLMigrator(db)
n = input()
m = input()
t = CharField(default='g')
try:
      migrate(
               migrator.drop_column(n,m,t)
      )
except:
    print("repetitive column!!!")



