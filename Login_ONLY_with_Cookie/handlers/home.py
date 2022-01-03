from .base import BaseHandler


class homeHandler(BaseHandler):

    # @tornado.web.authenticated
    def get(self):
        if self.authenticate():
            self.render('index.html', user=self.current_user)
            return
        self.redirect_rev('login')

