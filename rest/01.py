import tornado.ioloop
import pyrestful.rest

from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete

class Person(object):
	idperson = int 
	name = str

class PersonService(pyrestful.rest.RestHandler):
    @get('/person/{idperson}',{'format':'json'})
    def getPerson(self, idperson):
        p = Person()
        p.idperson = int(idperson)
        p.name = 'Mr.Robot'
        return p

    @post('/person',{'format':'json'},_catch_fire=True)
    def postPerson(self,person):
        return {'status':'person OK', 'person' : person}

if __name__ == '__main__':
    try:
        print("Start the service")
        app = pyrestful.rest.RestService([PersonService])
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(8080)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStop the service")
