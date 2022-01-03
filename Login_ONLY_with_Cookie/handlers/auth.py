from tornado.web import addslash

from .base import BaseHandler


class loginHandler(BaseHandler):
    
    @addslash
    def get(self):
        self.render("login.html", flash_messages={})

    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        try:
            self.login(username, password)
        except PermissionError:
            flash_messages = {
                    'username': username,
                    'password': password,
                    'error': "You'r username or password is incorrent"
                    }
            self.render('login.html', flash_messages=flash_messages)
        else:
            self.redirect_rev('home') 


class registerHandler(BaseHandler):

    @addslash
    def get(self):
        self.render("register.html", flash_messages={})

    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        try:
            self.register(username, password) 
        except ValueError: 
            flash_messages = {
                    'username': username,
                    'password': password,
                    'error': "User registeration failed! try again."
                    }
            self.render('register.html', flash_messages=flash_messages)
        else:
            self.redirect_rev('home')


class logoutHandler(BaseHandler):
    
    @addslash
    def get(self):
        self.logout()
        self.redirect_rev('home')

