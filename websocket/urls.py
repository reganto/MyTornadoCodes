from tornado.web import url
from handlers.home import HomeHandler, SocketHandler, Dev

url_patterns = [
    url(r"/", HomeHandler, name='home'),
    url(r"/socket", SocketHandler),
    # url(r'/wsocket', SocketHandler),
    url(r"/dev", Dev, name='dev'),
]
