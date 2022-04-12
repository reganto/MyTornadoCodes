import logging
from handlers.base import BaseHandler
logger = logging.getLogger('boilerplate.' + __name__)

from random import choice

class HomeHandler(BaseHandler):
    def get(self):
        numbers = [i for i in range(1, 101)]
        self.render('home/index.html', choice=choice, numbers=numbers)
