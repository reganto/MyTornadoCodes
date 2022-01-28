from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def post(self, name):
        age = self.get_query_argument('age', None)
        gender = self.get_body_argument('gender', None)
        print(name, age, gender)


if __name__ == '__main__':
    app = Application(
            [url('/(\w+)', IndexHandler)],
            autoreload=True 
            )
    app.listen(8005)
    IOLoop.current().start()

