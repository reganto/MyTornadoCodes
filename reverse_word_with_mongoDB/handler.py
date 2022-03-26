import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo
import pprint
from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

name = {'name':'morteza'}
client = pymongo.MongoClient()
db = client.db
names = db.names
name_id = names.insert_one(name).inserted_id
pprint.pprint(name_id)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")

class ReverseHandler(tornado.web.RequestHandler):
    def get(self):
        word = self.get_argument('word', '')
        self.write(word[::-1])


if __name__ == "__main__":
    tornado.options.parse_command_line();
    app = tornado.web.Application(handlers=[
    (r"/", MainHandler),
    (r"/reverse/", ReverseHandler),
    (r"/another", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
