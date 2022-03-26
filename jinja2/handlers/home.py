import logging
from handlers.base import BaseHandler
logger = logging.getLogger('boilerplate.' + __name__)


class HomeHandler(BaseHandler):
    def get(self):
        self.render('sample.jinja2', name='reganto')
