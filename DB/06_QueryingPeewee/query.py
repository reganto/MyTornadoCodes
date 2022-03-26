__author__ = 'admin'
from peewee import *
#from pwiz import *
import pwiz
from datetime import *
import playhouse.reflection


my_sql = MySQLDatabase("queryingdb",host="localhost",user="testuser",passwd="")
my_sql.connect()

class BaseModel(Model):
    class Meta:
        database = my_sql


class User(BaseModel):
    userid = IntegerField()
    username = CharField(unique=True,primary_key=True)
    class Meta:
        order_by = ('username',)

my_sql.create_table(User,safe=True)

#User.insert(username='abed',userid=1).execute()
#User.insert(username='emad').execute()
#User.insert(username='mahdi').execute()
#User.insert(username='amahd').execute()

#query = User.delete().where(User.id > 1)
#query.execute()

#m = (User.select().where(User.id>2).order_by(User.username.desc()))
#for n in m:
 #   print(n.username)

#m = User.select(User,fn.Count(User.userid).alias('ct'))
#q = m.order_by(SQL('ct'))
#print(m)
#for n in m:
 #   print(n.username)
#print(User.select().count())
#m = SQL("select * from user").
#print(m)
#for n in m:
 #   print(n.username)




