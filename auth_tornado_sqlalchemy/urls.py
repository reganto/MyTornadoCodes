from tornado.web import url
from handlers.home import HomeHandler
from handlers.auth import SignupHandler, SigninHandler

url_patterns = [
    url(r"/", HomeHandler, name='home'),
    url(r"/auth/signup/", SignupHandler, name='signup'),
    url(r"/auth/signin/", SigninHandler, name='signin'),
]
