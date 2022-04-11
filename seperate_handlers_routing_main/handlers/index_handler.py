import tornado
from tornado import web

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

    def get_current_user(self):
        user_json = self.get_secure_cookie("username")
        if user_json:
            return tornado.escape.json_decode(user_json)
        else:
            return 'hi'
            
