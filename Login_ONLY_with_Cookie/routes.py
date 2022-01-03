import handlers
from tornado.web import url

ROUTES = [
    url(r'/', handlers.homeHandler, name='home'),
    url(r'/login/?', handlers.loginHandler, name='login'),
    url(r'/register/?', handlers.registerHandler, name='register'),
    url(r'/logout/?', handlers.logoutHandler, name='logout'),
]

