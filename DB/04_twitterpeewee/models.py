__author__ = 'admin'

from peewee import *
from datetime import *
database = MySQLDatabase('twitterdb',host='localhost',user='testuser',passwd='',threadlocals = True)

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

    class Meta:
        order_by = ('username',)

    def following(self):
        return (
            User.select().where(RelationShip.from_user==self)
        )

    def followers(self):
        return (
            User.select().join(RelationShip,on=RelationShip.from_user).where(RelationShip.to_user==self)
        )



class RelationShip(BaseModel):
    from_user = ForeignKeyField(User,related_name='relationships')
    to_user = ForeignKeyField(User,related_name='related_to')

    class Meta:
        indexes = (
            (('from_user','to_user'),True),
        )


class Message(BaseModel):
    user = ForeignKeyField(User)
    content = TextField()
    pub_date = DateTimeField()

 
class Meta:
        order_by = ('pub_date',)

def create_tables():
    database.connect()
    database.create_tables([User,RelationShip,Message])
    
    
    

#create_tables()

#try:
 #   with database.transaction():
  #      user = User.create(
   #         usrname = request.form['username'],
    #        password = md5(request.form['password']).hexdigest(),
     #       email = request.form['email'],
      #      join_date = datetime.now()
       # )
    #aut_user(user)
    #return redirect(url_for('homepage'))
#
#except IntegrityError:
#   pass
#user = User.select().where(User.username=='u1')

#print(user.id)
#message = Message.select().where(Message.user << user.following())

#for u in message:
 #   print(u.content)









