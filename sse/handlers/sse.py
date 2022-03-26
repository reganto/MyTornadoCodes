# from tornado.httputil import Http
from handlers.base import BaseHandler


class StartConnection(BaseHandler):
    def get(self):
        self.render(
            'sse.html',
            page_title='sse'
        )


class SSEHandler(BaseHandler):
    def get(self):
        self.write('event: message\nretry: 1000\ndata: Hello\n\n')
        self.set_header('content-type', 'text/event-stream')
        self.set_header('cache-control', 'no-cache') 
        self.finish()
