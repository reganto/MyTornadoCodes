import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from settings import settings
from urls import url_patterns


class Application(tornado.web.Application):
    def __init__(self):
        super().__init__(url_patterns, **settings)


def make_app():
    print(f"Server (re)started on {options.address}:{options.port}")
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port, options.address)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    make_app() 
