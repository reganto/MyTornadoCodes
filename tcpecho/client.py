#!/usr/bin/env python

import tornado.ioloop
import tornado.gen
import tornado.tcpclient
from tornado.options import options, define

define("host", default="localhost", help="TCP server host")
define("port", default=8888, help="TCP port to connect to")
define("message", default="ping", help="message to send")


@tornado.gen.coroutine
def send_message():
    stream = yield tornado.tcpclient.TCPClient().connect(options.host, options.port)
    yield stream.write((options.message + '\n').encode())
    print('Send to server: ', options.message)
    reply = yield stream.read_until(b'\n')
    print('Response from server: ', reply.decode().strip())


if __name__ == "__main__":
    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.current().run_sync(send_message)
