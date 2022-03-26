from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.web import Application, RequestHandler
from tornado.websocket import WebSocketHandler

import sys
import json
import logging


class MainHandler(RequestHandler):
    
    def get(self):
        self.render('index.html')


class EchoWebSocket(WebSocketHandler):
    def on_message(self, msg):
        self.write_message(json.dumps({'message': msg}))


application = Application([
    (r"/", MainHandler),
    (r"/echo", EchoWebSocket),
])

def on_stdin(fd, events):
    content = fd.readline()
    print('fd: ', fd)
    print(f'received: {content}')
    print('on_stdin event: ', events)


def on_stdout(fd, events):
    print('stdout: ', fd, events)

def a_callback_that_calls_next_iter():
    print('foo')

def periodic_func():
    print('periodic func')

if __name__ == '__main__':
    #PeriodicCallback(periodic_func, 1)
    application.listen(8888)
    #IOLoop.instance().add_handler(sys.stdin, on_stdin, IOLoop.READ | IOLoop.ERROR)

    # IOLoop.instance().add_handler(sys.stdout, on_stdout, IOLoop.WRITE | IOLoop.ERROR)
    # IOLoop.instance().add_callback(a_callback_that_calls_next_iter)
    logging.info('Server started on port 8888')
    IOLoop.instance().start()

