import sys
import itertools
import tornado.websocket
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver

from tornado.options import options, define
define("port", default=8888, help="run on the given port", type=int)


class Appliaction(tornado.web.Application):
    def __init__(self):
        urlpatterns = [
            (r"/", HomeHandler),
            (r"/mysocket", EchoHandler)
        ]
        settings = {
            'debug': True,
            'template_path': 'templates'
        }
        super().__init__(urlpatterns, **settings)


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('sample.html')


class EchoHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message('connected!')
    
    def on_message(self, message):
        self.write_message(message)

    def on_pong(self):
        write, flush = sys.stdout.write, sys.stdout.flush
        for char in itertools.cycle('.'):
            status = 'ping'+char+char
            write(status)
            flush()
            write('\x08' * 2 * len(char))

    def on_close(self):
        self.write_message('connection closed!')
        

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Appliaction())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
