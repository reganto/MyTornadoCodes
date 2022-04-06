import json
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver
import tornado.httpclient
import requests
import tornado.gen

from tornado.options import options, define
define("port", default=8888, help="run on the given port", type=int)


class Appliaction(tornado.web.Application):
    def __init__(self):
        urlpatterns = [
            (r"/", HomeHandler),
            (r"/slow/", SlowHandler),
            (r"/api/call/", APICallHandler),
            (r"/api/gen/", APIWithGenHandler),
        ]
        settings = dict(
            debug=True,
        )
        super().__init__(urlpatterns, **settings)


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Home')


class SlowHandler(tornado.web.RequestHandler):
    def get(self):
        response = requests.get('https://dog.ceo/api/breeds/image/random').json()
        self.write(response['status'] + '\n')


class APICallHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch('https://dog.ceo/api/breeds/image/random', callback=self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)
        self.write(body['status'] + '\n')
        self.finish()


class APIWithGenHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch, 'https://dog.ceo/api/breeds/image/random')
        body = json.loads(response.body)
        self.write(body['status'] + '\n')
        self.finish()


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Appliaction())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

