import os

import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.web import url
from tornado.options import options, define, parse_command_line

define('port', default=8000, type=int, help='run on the given port')


class BaseHandler(tornado.web.RequestHandler):
    def get_json_argument(self, name, default=None):
        if self.request.body:
            raw_data = self.request.body.decode().replace('\'', '\"')
            try:
                json_data = tornado.escape.json_decode(raw_data)
                return json_data.get(name, default)
            except Exception as e:
                print('Error in get_json_argument method: ', e)
        else:
            print('Data not presented')

    def get_json_arguments(self):
        if self.request.body:
            raw_data = self.request.body.decode().replace('\'', '\"')
            try:
                json_data = tornado.escape.json_decode(raw_data)
                return json_data
            except Exception as e:
                print('Error in get_json_argument method: ', e)
        else:
            print('Data not presented')


class HomePageHandler(BaseHandler):
    def post(self):
        data = self.get_json_arguments()
        self.write(data)


class Application(tornado.web.Application):
    def __init__(self):
        routes = [
            url('/', HomePageHandler, name='home'),
        ]
        settings = dict(
            debug=True,
        )
        super().__init__(routes, **settings)


if __name__ == '__main__':
    parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
