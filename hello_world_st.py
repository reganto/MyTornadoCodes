from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self):
        self.write('hello, world!')


class App(Application):
    def __init__(self):
        handlers = [url('/', IndexHandler, name='index')]
        settings = {'debug': True}
        super().__init__(handlers, **settings)
        

if __name__ == '__main__':
    app = App()
    app.listen(8001)
    IOLoop.current().start()

