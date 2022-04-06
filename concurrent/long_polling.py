import uuid
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver

from tornado.options import options, define
define("port", default=8888, help="run on the given port", type=int)


class ShopingCart:
    totalInventory = 10
    callbacks = []
    carts = {}

    def register(self, callback):
        self.callbacks.append(callback)

    def moveItemToCart(self, session):
        if session in self.carts:
            return

        self.carts[session] = True
        self.notifyCallbacks()

    def removeItemFromCarts(self, session):
        if session not in self.carts:
            return

        del self.carts[session]
        self.notifyCallbacks()

    def notifyCallbacks(self):
        for c in self.callbacks:
            self.callbackHelper(c)
        
        self.callbacks = []

    def callbackHelper(self, callback):
        callback(self.getInventoryCount())

    def getInventoryCount(self):
        return self.totalInventory - len(self.carts)


class Application(tornado.web.Application):
    def __init__(self):
        self.shopingCart = ShopingCart()

        urlpatters = [
            (r"/", DetailHandler),
            (r"/cart", CartHandler),
            (r"/cart/status", StatusHandler)
        ]
        settings = {
            'debug': True,
            'template_path': 'templates',
            'static_path': 'static'
        }
        super().__init__(urlpatters, **settings)


class DetailHandler(tornado.web.RequestHandler):
    def get(self):
        session = uuid.uuid4()
        count = self.application.shopingCart.getInventoryCount()
        self.render("index.html", session=session, count=count)


class CartHandler(tornado.web.RequestHandler):
    def post(self):
        action = self.get_argument('action')
        session = self.get_argument('session')

        if not session:
            self.set_status(400)
            return
        
        if action == 'add':
            self.application.shopingCart.moveItemToCart(session)
        elif action == 'remove':
            self.application.shopingCart.removeItemFromCarts(session)
        else:
            self.set_status(400)


class StatusHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.application.shopingCart.register(self.on_message)

    def on_message(self, count):
        self.write('Inventory count: {}'.format(count))
        self.finish()


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Home')


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
