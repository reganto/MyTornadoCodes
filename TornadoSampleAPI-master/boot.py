#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ReS4'

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado

from tornado.options import options, define

from ApiApp.urls.main_urls import url_patterns
from config import Config

config = Config()

define("port", default=config.web['port'], help="run on the given port", type=int)


class WebSystemApplication(tornado.web.Application):
    def __init__(self):
        handlers = url_patterns
        settings = dict(
            debug=True,
            autoreload=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(WebSystemApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
