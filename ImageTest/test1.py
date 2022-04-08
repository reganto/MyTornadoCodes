#import image
#from PIL import Image

import redis
#from io import BytesIO
#from tkinter import PhotoImage

#import Image
#myImage = PhotoImage(file='C:/Desert.jpg')
#im = Image.open('C:/Desert.png')
#im.show()
#im.close()
#image.show()
#myImage.


#output = BytesIO()
#output = StringIO(open('C:/Desert.jpg'))
#Image.EXTENSION
#im = open("C:/Desert.jpg")
#im.save(output,'PNG')
x=input()
#y=input()
r = redis.StrictRedis(host='localhost')
#r.set(x,y)
print(str(r.get(x))[1:])
#r.set('imagedata', output.getvalue())
#r.set('imagedata', im)
#h=r.get('imagedata')
#print(type(h))
#print(str(h))
#output = BytesIO(h)
#h.show()
#im = Image.open(h,'r')
#im.show()
#i = Image.open(output)
#i.show()
#output.close()
