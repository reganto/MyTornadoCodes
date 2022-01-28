import tornado.web
import tornado.ioloop
import tornado.escape
import tornado.httpclient
import tornado.gen

import bcrypt


class IndexHandler(tornado.web.RequestHandler):
    async def post(self):
        """Handle CPU Bound Task in Tornado"""
        hashed_password = await tornado.ioloop.IOLoop.current().run_in_executor(
                None,
                bcrypt.hashpw,
                tornado.escape.utf8(self.get_body_argument('password')),
                bcrypt.gensalt(),
                )
        print(hashed_password)

    async def get(self):
        """Handle IO Bound Task with native coroutines"""
        url = 'https://reqres.in/api/users'
        http_client = tornado.httpclient.AsyncHTTPClient()
        try:
            response = await http_client.fetch(url)
        except Exception as e:
            print('Error: %s' % e)
        else:
            print(response.body)

    @tornado.gen.coroutine
    def patch(self):
        """Handle IO Bound Task with generator base coroutines"""
        url = 'https://reqres.in/api/users'
        http_client = tornado.httpclient.AsyncHTTPClient()
        try:
            response = yield http_client.fetch(url)
        except Exception as e:
            print('Error: %s' % e)
        else:
            print(response.body)


class Application(tornado.web.Application):
    def __init__(self):
        url_patterns = [
                tornado.web.url('/', IndexHandler),
                ]
        settings = dict(
                autoreload=True
                )
        super(Application, self).__init__(url_patterns, **settings)


if __name__ == '__main__':
    Application().listen(8001)
    tornado.ioloop.IOLoop.current().start()

