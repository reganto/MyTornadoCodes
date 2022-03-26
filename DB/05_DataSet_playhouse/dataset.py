

from peewee import *
from playhouse.dataset import *

db = DataSet('mysql://root:@localhost/datasettest')

table = db['student']

table.insert(name = 'reza')
table.insert(name = 'ali')
table.insert(name = 'hadi',family='ahmadi')
table.insert(age = 12)

students = db['student'].all()

#for s in students:
#    print(s['name'])


#table.update(name='ali',age=20,columns=['name'])
#table.delete(name='ali')


#with db.transaction() as txn:
 #   table.insert(name = "reza")

  #  with db.transaction() as nested_txn:
   #     table.update(name="reza",street="61metri",columns=['name'])
    #    nested_txn.rollback()


#print(db.tables)


#students = db['student'].find(name="reza")
#for s in students:
 #   print(s['street'])


#student = db['student'].find_one(name="reza")
#print(student['street'])

db.freeze(students,format='json',filename='students.json')

#table1 = db['newstudent']
#table1.thaw(filename='students.json',format='json')

#db.connect()
#db.close()

#db['student'].delete()

#print(table1.columns)




#db.update_cache(table='student')


