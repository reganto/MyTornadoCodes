# import logging
# from itertools import cycle
import time
# from time import time
import tornado.websocket
from handlers.base import BaseHandler
# logger = logging.getLogger('boilerplate.' + __name__)

# from mysql.connector import connect

from tornado.escape import xhtml_escape

from settings import options
# db = connect(
#     host="localhost",
#     database="dot",
#     username="reganto",
#     password="1"
# )
# def counter(start: int, step: int) -> int:
#     count = start
#     while True:
#         count += step
#         yield count
        
# t = cycle(range(100))

class HomeHandler(BaseHandler):
    def get(self):
        self.render(
            'home/index.html',
            page_title='Usernado'
        )


class SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('Websocket opened')
        # self.set_nodelay(True)
        # self.get_compression_options()
    def on_message(self, message):
        try:
            if isinstance(message, str):
                username = xhtml_escape(message.strip())
                # username = message
                print(username)
                self.write_message(username)
            else:
                self.on_close()
        except tornado.websocket.WebSocketClosedError as e:
            print('websocket closed already')
    def on_ping(data):
        print('ping')
    def on_pong(self, data):
        print(f'pong')
    def on_close(self):
        print(f'Websocket closed -> {self.close_code} -> {self.close_reason}')


# class SocketHandler(tornado.websocket.WebSocketHandler):
#     def open(self):
#         c = tornado.websocket.websocket_connect(
#             url='ws://'+options.address+str(options.port)+'/wsocket',
#             connect_timeout=10,
#             on_message_callback=self.msg,
#             compression_options={},
#             ping_interval=1,
#             ping_timeout=2,
#             max_message_size=11
#         )
#         print(c)
#     def msg():
#         print('ok')
#     def on_message(self, message):
#         print(message)
#         self.write_message(xhtml_escape(message))


class Dev(BaseHandler):
    def get(self):
        self.render(
            'dev.html',
            page_title='dev'
        )
