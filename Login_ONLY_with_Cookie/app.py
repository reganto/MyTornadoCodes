import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define,options

from routes import ROUTES
from config import SETTINGS

define("port",default=8000,help="run on the given port",type=int)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application = tornado.web.Application(ROUTES, **SETTINGS)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

