from tornado.web import addslash

from .base import BaseHandler


class loginHandler(BaseHandler):
    
    @addslash
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        self.login(username, password)
        


class registerHandler(BaseHandler):

    @addslash
    def get(self):
        self.render("register.html")

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        self.register(username, password) 


class logoutHandler(BaseHandler):
    
    @addslash
    def get(self):
        self.logout()

