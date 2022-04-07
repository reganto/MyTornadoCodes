__author__ = 'admin'
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web
import os.path
from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        arr =  ['ali','hassan']
        self.render('index.html',arr=arr)

if __name__ == '__main__' :
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [(r'/',IndexHandler)],
        template_path = os.path.join(os.path.dirname(__file__),"templates"),
        static_path = os.path.join(os.path.dirname(__file__),"static"),
        debug = True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



