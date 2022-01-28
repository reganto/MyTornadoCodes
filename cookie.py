import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver

from tornado.options import options, define
define("port", default=8888, type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", MainHandler),]
        settings = dict()
        tornado.web.Application.__init__(self, handlers, **settings, debug=True)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_cookie("mycookie"):
            self.set_cookie("mycookie", "abcdfgh12345678!@#$za")
            self.write("Your cookie was not set yet!")
        else:
            value = self.get_cookie("mycookie")
            self.write("Your cookie was set!" + " cookie value is " + value)

if __name__ == "__main__":
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
