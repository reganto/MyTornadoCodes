__author__ = 'admin'
#import query
#print(query.User.userid)
from playhouse.dataset import DataSet
from playhouse.migrate import *
import peewee
#import datatables
#from datatables import *
db = DataSet('mysql://root:@localhost/test2')



table = db['user']

#table.insert(username = 'ali',userid = 5,tel=22222,mobile=9111111)



m=input()
table1 = db[m]

'''
m = 'tbl1'
db = MySQLDatabase('test1',host="localhost",user="root",passwd="")
migrator = MySQLMigrator(db)
n=input()
t=CharField(default='g')
try:
      migrate(
               migrator.add_column(m,n,t)
      )
except :
    print("Error: redefine column!")
'''


#table1['one']='yes'
#s ='[{"one":"yes"}]'
#table1.insert('[{"one":"yes"}]')
#table1.thaw(s)



#n=input()
#h=input()
#table1.columns = [n,h]
#a={}
#a[n]=h
#peewee.dict_to_model(table1,a)

#print(a)
#table1.__dict__.items({n:h})
#table1.insert()
#table1._migrate_new_columns(n)
