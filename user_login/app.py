import os

import tornado.web
import tornado.ioloop
from tornado.web import url

from tornado.options import options, define, parse_command_line
define('port', default=8000, type=int, help='run on the given port')

BASE = os.path.dirname(os.path.abspath(__file__))
add_path = lambda *args: os.path.join(BASE, *args)


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('username')


class LoginHandler(BaseHandler):
    @tornado.web.addslash
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.get_body_argument('username', None)
        self.set_secure_cookie('username', username)
        self.redirect(self.reverse_url('home'))


class HomePageHandler(BaseHandler):
    def get(self):
        self.render('home.html')


class ProfilePageHandler(BaseHandler):
    @tornado.web.addslash
    @tornado.web.authenticated
    def get(self):
        self.render('profile.html', user=self.current_user)


class LogoutHandler(BaseHandler):
    @tornado.web.addslash
    def get(self):
        self.clear_cookie('username')
        self.redirect(self.reverse_url('home'))


class Application(tornado.web.Application):
    def __init__(self):
        routes = [
            url('/', HomePageHandler, name='home'),
            url(r'/user/login/?', LoginHandler, name='login'),
            url(r'/user/profile/?', ProfilePageHandler, name='profile'),
            url(r'/user/logout/?', LogoutHandler, name='logout'),
        ]
        settings = dict(
            template_path = add_path('templates'),
            cookie_secret = os.urandom(16),
            xsrf_cookies = True,
            login_url = '/user/login/',
            debug = True,
        )
        super().__init__(routes, **settings)


if __name__ == '__main__':
    parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
