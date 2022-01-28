# Author: reganto.net

from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def initialize(self, db):
        # self.db = db
        print('initialize')

    def prepare(self):
        # if self.current_user is None:
        #     self.redirect(self.reverse_url('login'))
        # self.db.connect()
        print('prepare')

    def post(self):
        # self.db.query()
        print('post')

    def on_finish(self):
        # self.db.close()
        print('on_finish')


if __name__ == '__main__':
    app = Application(
            [url('/', IndexHandler, dict(db='db_connection'))],
            autoreload=True 
            )
    app.listen(8005)
    IOLoop.current().start()

