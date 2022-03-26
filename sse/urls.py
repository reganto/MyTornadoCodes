from tornado.web import url
from handlers.home import HomeHandler
from handlers.sse import SSEHandler, StartConnection

url_patterns = [
    url(r"/", HomeHandler, name='home'),
    url(r"/showpage", StartConnection),
    url(r"/s", SSEHandler),
]
