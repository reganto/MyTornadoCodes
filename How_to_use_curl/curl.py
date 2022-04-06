# How to use of Curl


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


# Curl test
class Mainhandler(tornado.web.RequestHandler):
    def post(self, word):
        # curl -d name=reganto http://localhost:8000/
        x = self.get_argument("name")
        self.write(x)
        # curl -d name=reganto http://localhost:8000/word
        self.write(word)




class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/(\w+)", Mainhandler)]
        tornado.web.Application.__init__(self, handlers, debug=True)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
