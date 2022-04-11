__author__ = 'Reganto'

from tornado import httpserver
from tornado import ioloop
from tornado import web
from tornado import options
import os.path

from urls import *


from tornado.options import define, options
define("port", default=8888, help=None, type=int)

class Application(web.Application):
    def __init__(self):
        handlers = urlList
        settings = dict(
            cookie_secret="61oETz3455545gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            debug = True
        )
        web.Application.__init__(self, handlers, **settings)


def main():
    options.parse_command_line()
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
