#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.wsgi

from flaskapp import app

if __name__ == '__main__':
    wsgi_app = tornado.wsgi.WSGIContainer(app)
    http_server = tornado.httpserver.HTTPServer(wsgi_app)
    http_server.listen(8001)
    tornado.ioloop.IOLoop.current().start()

