#import peewee

from peewee import *

db = MySQLDatabase("people", host="localhost", port=3306, user="root", passwd="")



class SampleDB(Model):
    class Meta:
        database = db

class Person(SampleDB):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()


class Pet(SampleDB):
    owner = ForeignKeyField(Person,related_name='pets')
    name = CharField()
    animal_type = CharField()



class School(SampleDB):
    name = CharField()

class Teacher(SampleDB):
    name = CharField()

db.create_tables([Person,Pet,School,Teacher],safe=True)

#herb = Person.get(Person.name == 'jeam')

#with db.transaction():
 #   herb.delete_instance(recursive=True)





from datetime import date
#herb = Person.get(Person.name == 'Herb')


#db.set_autocommit(False)
#try:
 #   herb.delete_instance(recursive=True)
#except:
 #   db.rollback()
  #  raise
#else:
 #   try:
  #      db.commit()
   # except:
    #    db.rollback()
     #   raise
#finally:
 #   db.set_autocommit(True)



#Person.insert_many()




#try:
 #   with db.transaction():
  #      bob_fido = Pet.create(owner = herb , name = 'Fido', animal_type = 'dog')

#except IntegrityError :
 #   pass






#uncle_jeam = Person(name = 'jeam', birthday = date(1967,11,15),is_relative = True)
#uncle_jeam.save()

#Alex = Person.create(name = 'Alex', birthday = date(1976,7,8), is_relative = True)
#herb = Person.create(name = 'Herb', birthday = date(1950,5,5), is_relative = True)

#uncle_jeam = Person.get(Person.name == 'jeam')
#uncle_jeam.name = 'Jeamy'
#uncle_jeam.save()
#herb = Person.get(Person.name == 'Herb')
#grandma.name = 'Grandma L.'
#grandma.save()

#Jeamy_kitty = Pet.create(owner = uncle_jeam , name = 'Kitty1', animal_type = 'cat')
#Jeamy_dog = Pet.create(owner = uncle_jeam , name = 'Dog', animal_type = 'dog')
#bob_fido = Pet.create(owner = herb , name = 'Fido', animal_type = 'dog')
#bob_mitten = Pet.create(owner = herb , name = 'Mittens', animal_type = 'cat')
#bob_mitten_jr = Pet.

#Jeamy_dog = Pet.get(Pet.name=='Dog')
#Jeamy_dog.delete_instance()
#herb.delete().execute()

#with db.transaction():
 #   herb.delete_instance(recursive=True)




#Pet.create(owner = herb , name = 'Mittens Jr', animal_type = 'cat')

#herb_mitten_jr = Pet.get(Pet.name == 'Dog')

#herb_mitten_jr.delete_instance()

#for person in Person.select().order_by(Person.birthday.asc()):
 #   print(person.name,person.pets.count(),'pets')
  #  for pet in person.pets:
   #     print('  ',pet.name,pet.animal_type)

#query = Person.select().join(Pet,JOIN_LEFT_OUTER).distinct()

#for q in query:
    #print(q.name)
#mat = ['bob','tom','Herb']
#mat1=[]
#for i in range(5):
 #   mat1.append(i*2)

#query1 = Pet.select().join(Person).where(Person.id==3 )
#query1 = Pet.select().join(Person)

#print("New Query !!!")

#for q in query1:
 #   print(q.name)



#query = Pet.select(Pet,Person).join(Person).where(Pet.animal_type=='cat')
#for pet in Pet.select().where(Pet.owner == herb).order_by(Pet.name):
 #   print(pet.name)


#d1940 = date(1940,1,1)
#d1960 = date(1960,1,1)

#query = (Person.select().where((Person.birthday<d1940) | (Person.birthday>d1960)))
#for person in query:
 #   print(person.name)

#expression = (fn.Lower(fn.Substr(Person.name,1,1))=='h')
#for person in Person.select().where(expression):
 #   print(person.name)
