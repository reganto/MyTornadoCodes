import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options
import os.path
from routes import *

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urlList
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname("__file__"), "static"),
            xsrf_cookies = False,
            debug = True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
