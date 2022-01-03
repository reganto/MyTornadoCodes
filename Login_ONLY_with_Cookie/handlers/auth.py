from tornado.web import addslash

from .base import BaseHandler


class loginHandler(BaseHandler):
    
    @addslash
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        try:
            self.login(username, password)
        except PermissionError:
            self.write(
                    '''<h3>You'r username or password is incorrect</h3>'''
                    '''<p>Corrent you'r information and try again</p>'''
                    '''<a href="/login/">try again</a>'''
            )
        else:
            self.redirect_rev('home') 


class registerHandler(BaseHandler):

    @addslash
    def get(self):
        self.render("register.html")

    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        try:
            self.register(username, password) 
        except ValueError: 
            self.write(
                    '''<div><h3>User registeration failed!</h3></div>'''
                    '''<p>Corrent username and password and try again</p>'''
                    '''<p><a href="/register/">try again</a><p>'''
            )
        else:
            self.redirect_rev('home')


class logoutHandler(BaseHandler):
    
    @addslash
    def get(self):
        self.logout()
        self.redirect_rev('home')

