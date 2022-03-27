import uuid
import secrets

from tornado.web import Application, url
from tornado.ioloop import IOLoop
from usernado import Handler


class Home(Handler.Web):
    def get(self):
        self.render("home.html")



class GhostCall(Handler.Web):
    def get(self):
        self.write({
            "id": uuid.uuid4().hex,
        })


if __name__ == "__main__":
    handlers = [
        url("/", Home, name="home"),
        url("/call/", GhostCall, name="call"),
    ]
    settings = {
        "debug": True,
        "cookie_secret": secrets.token_bytes(),
    }
    Application(handlers, **settings).listen(8000)
    IOLoop.current().start()
