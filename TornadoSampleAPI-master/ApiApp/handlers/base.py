#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

from config import Config

s = Config()

# noinspection PyBroadException
class WebBaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(WebBaseHandler, self).__init__(application, request, **kwargs)
        self.result = dict(
            value="",
            message="",
            status=False
        )

    def on_finish(self):
        pass


def error_handler(self, status_code, **kwargs):
    if status_code == 404:
        self.finish({"error": "404, not found."})
    else:
        self.finish({"error": "500, system failure."})


tornado.web.RequestHandler.write_error = error_handler
