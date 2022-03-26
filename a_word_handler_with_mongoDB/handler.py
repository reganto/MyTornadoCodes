import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from pymongo import MongoClient

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

# connect to MOONGODB
client = MongoClient('localhost', 27017)

# create a new DATABASE
db = client.newdatabase

# create a new COLLECTION
dictionary = db.dictionary

# create two DOCUMENT
x = dictionary.insert_one({"word":"morteza", "definition":"A man with white heir"}).inserted_id
y = dictionary.insert_one({"word":"ali", "definition":"A good boy"}).inserted_id

# create application
class Application(tornado.web.Application):
    def __init__(self, db):
        handlers = [(r"/(\w+)", WordHandler)]
        self.db = db
        tornado.web.Application.__init__(self, handlers, debug=True)

# handler class
class WordHandler(tornado.web.RequestHandler):
    def get(self, word):
        coll = self.application.db.dictionary
        word_doc = coll.find_one({"word":word})
        if word_doc:
            del word_doc["_id"]
            self.write(word_doc)
        else:
            self.set_status(404)
            self.write({"error":"word not found"})

# main section
if __name__ == "__main__":
    tornado.options.parse_command_line()
    sample = Application(db)
    http_server = tornado.httpserver.HTTPServer(sample)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
