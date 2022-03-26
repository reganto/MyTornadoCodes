from peewee import *
from datetime import *
from playhouse.pool import PooledMySQLDatabase

my_sql = PooledMySQLDatabase(
    'myd',max_connections=8,stale_timeout=300, threadlocals = True,user='root'
)
#my_sql = MySQLDatabase('myd',host='localhost',user='testuser',passwd='',threadlocals=True)
#my_sql = MySQLDatabase(None)
#my_sql.init('myd',host='localhost',user='testuser',passwd='')

class BaseModel(Model):
    class Meta:
        database = my_sql

class User(BaseModel):
    username = CharField(unique=True)



class Tweet(BaseModel):
    user = ForeignKeyField(User,related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.now())
    is_published = BooleanField(default=True)

class Friend(BaseModel):
    name = CharField()
    family = CharField()
    class Meta:
        indexes = (
            (('name','family'),True)
        )

class Friend1(BaseModel):
    name = CharField()
    family = CharField()
    class Meta:
        primary_key = CompositeKey('name','family')
import uuid
class Friend4(BaseModel):
    fid = IntegerField(uuid.uuid4())
    name = CharField()
    family = CharField()
    class Meta:
        primary_key = CompositeKey('name','family')
        auto_increment = True

my_sql.create_tables([User,Tweet,Friend,Friend1,Friend4],safe=True)

#my_sql.create_table(Friend4)

from playhouse.migrate import *

migrator = MySQLMigrator(my_sql)

title_field = CharField(default='')
status_field = IntegerField(null=True)
m = input()
def convertor():
    migrate(
        #migrator.add_column('user','test3',title_field),
        #migrator.add_column('tweet','status3',status_field),
        #migrator.drop_column('tweet','is_published'),
        #migrator.rename_column('user','test3',m)
    )

convertor()

'''
import pymysql
#import peewee
conn = pymysql.connect(host="localhost",  user="testuser", passwd="" , db="myd")
cur = conn.cursor()
cur1 = conn.cursor()
m = input()
s = input()
#cur.execute("SELECT COLUMN_NAME  FROM INFORMATION_SCHEMA.COLUMNS  WHERE table_name = %s AND table_schema = 'myd'  ",m)
cur1.execute("select table_name from information_schema.tables where table_schema=%s AND table_name LIKE %s",(m,"%"+s+"%"))
#print(cur)
for r in cur1:
       print(r[0])
cur.close()
cur1.close()
conn.close()
'''
