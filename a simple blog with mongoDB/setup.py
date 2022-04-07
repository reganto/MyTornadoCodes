#*****************************A Simple Blog*************************************
# -*- coding:UTF-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path
import json
from urls import *
from pymongo import MongoClient
#**************************
#from bson import ObjectId
from tornado.options import define, options



#************************ connect to mongodb************************************
#*************************create client for mongo*******************************
client = MongoClient('localhost', 27017)
#*********************** create a new database**********************************
db = client.pyblogdb
#*******************************end*********************************************



#************************** define port*****************************************

define("port", default=8888, help="run on the given port", type=int)

#*********************************end*******************************************



#**********************************Application**********************************
# routes
class Application(tornado.web.Application):

    def __init__(self, db):
        self.db = db
        # handlers
        handlers = urlList
        # settings as dict
        settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        ui_modules={"View_comment" : View_commentModule},
        debug=True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)
#***********************************end*****************************************





#***********************************create APP**********************************
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(db))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

#*************************************end***************************************


if __name__ == "__main__":
    main()
