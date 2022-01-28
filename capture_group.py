import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.options

from tornado.options import define, options
define("port", default=8888, type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/([0-9]+)", NumberHandler),
            (r"/word/(\w+)", WordHandler),
        ]

        settings = dict(
            debug = True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Reganto")

class NumberHandler(tornado.web.RequestHandler):
    def get(self, number):
        self.write(number)

class WordHandler(tornado.web.RequestHandler):
    def get(self, word):
        self.write(word)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
