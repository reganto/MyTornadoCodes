__author__ = 'admin'

import tornado.web
from pycket.session import SessionMixin
from pycket.notification import NotificationMixin


class BaseHandler(tornado.web.RequestHandler, SessionMixin, NotificationMixin):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.session.set('key', 'value')
        p = self.session.get('key')
        self.render('index.html')
