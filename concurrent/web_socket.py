#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
define("port", default=8888, type=int, help="run on the given port")


class ShopingCart:
    totalInventory = 10
    callbacks = []
    carts = {}

    def register(self, callback):
        self.callbacks.append(callback)

    def unregister(self, callback):
        self.callbacks.remove(callback)

    def addItemToCart(self, session):
        if session in self.carts:
            return 

        self.carts[session] = True
        self.notifyCallbacks()

    def removeItemFromCart(self, session):
        if session not in self.carts:
            return 

        del self.carts[session]
        self.notifyCallbacks()

    def notifyCallbacks(self):
        for callbacks in self.callbacks:
            callback(self.getInventoryCount())

    def getInventoryCount(self):
        return self.totalInventory - len(self.carts)


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
            self.application.shopingCart.addItemToCart(session)
        elif action == 'remove':
            self.application.shopingCart.removeItemFromCart(session)
        else:
            self.set_status(400)


class StatusHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.application.shopingCart.register(self.callback)
    
    def on_close(self):
        self.application.shopingCart.unregister(self.callback)

    def on_message(self, message):
        pass

    def callback(self, count):
        self.write_message('Inventory Count:'.format(count))


class Application(tornado.web.Application):
    def __init__(self):
        self.shopingCart = ShopingCart()

        urlpatterns = [
            (r"/", DetailHandler),
            (r"/cart", CartHandler),
            (r"/cart/status", StatusHandler)
        ]

        settings = {
            'template_path': 'templates',
            # 'static_path': 'static'
        }

        super().__init__(urlpatterns, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
