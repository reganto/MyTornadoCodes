import tornado.web
from .base import BaseHandler


class homeHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.render('index.html', user = self.current_user)


