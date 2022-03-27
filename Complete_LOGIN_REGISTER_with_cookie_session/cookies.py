__author__ = 'e.azizi'

import tornado.httpserver
import tornado.options
import tornado.web
import tornado.ioloop
import os.path
import uuid
import hashlib
import base64
import redis
from models import *
from pycket.session import *
from pycket.notification import *

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class BaseHandler(tornado.web.RequestHandler,SessionMixin,NotificationMixin):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        password = password.encode('utf-8')
        user = User.select().where(User.username==username)
        auth=False
        for u in user:
            salt1=(u.salt)
            salt1 = salt1.encode('utf-8')
            hashed_password = hashlib.sha512(password + salt1).hexdigest()
            if u.password == hashed_password:
                auth = True
                break
        if auth:
                self.session.set('username', username+'category')
                self.set_secure_cookie("username",self.get_argument("username"))
                self.redirect("/")
        else:
                self.redirect("/login")



class RegisterHandler(BaseHandler):
    def get(self):
        self.render("register.html")

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        password = password.encode('utf-8')
        salt = uuid.uuid4().hex.encode('utf-8')
        hashed_password = hashlib.sha512(password + salt).hexdigest()
        user = User.select().where(User.username==username)
        confirm = True
        for u in user:
            if u.username == username:
                confirm = False
                break
        if confirm == True:
            User.create(
                  username=username,
                  password=hashed_password,
                  salt=salt
            )
            self.set_secure_cookie("username",self.get_argument("username"))
            self.session.set('username', username+'category')
            self.redirect("/")

        else:
            self.redirect("/register")



class WelcomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user = self.current_user
        category = self.session.get('username')
        self.render('index.html', user = self.current_user,category=category)

class LogoutHandler(BaseHandler):
    def get(self):
        if (self.get_argument("logout",None)):
             self.clear_cookie("username")
             self.redirect('/')

if __name__ == '__main__':
    tornado.options.parse_command_line()

    setting = {
        "template_path" : os.path.join(os.path.dirname(__file__),"templates"),
        "cookie_secret" : base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
        "_xsrf_cookies" : True,
        "login_url" : "/login",
        'pycket': {
                 'engine': 'redis',
                 'storage': {
                 'host': 'localhost',
                 'port': 6379,
                 'db_sessions': 10,
                 'db_notifications': 11,
                 'max_connections': 2 ** 31,
                 },
                 'cookies': {
                             'expires_days': 120,
                 },
        },
    }

    application = tornado.web.Application([
          (r'/',WelcomeHandler),
          (r'/login',LoginHandler),
          (r'/register',RegisterHandler),
          (r'/logout',LogoutHandler),
    ], **setting)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



