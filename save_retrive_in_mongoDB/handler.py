import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from pymongo import MongoClient

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

# connect to mongodb
# create a mongo client
client = MongoClient('localhost', 27017)
# connect to newdatabase
db = client.newdatabase

class WordHandler(tornado.web.RequestHandler):
    def get(self, word):
        coll = self.application.db.dictionary
        word_doc = coll.find_one({"word":word})
        if word_doc:
            del word_doc["_id"]
            self.write(word_doc)
        else:
            self.set_status(404)

    # curl -d definition=connection+without+wire http://localhost:8888/wireless
    def post(self, word):
        definition = self.get_argument("definition")
        coll = self.application.db.dictionary
        word_doc = coll.find_one({"word":word})
        if word_doc:
            word_doc["definition"] = definition
            coll.save(word_doc)
        else:
            word_doc = {"word":word, "definition":definition}
            coll.insert_one(word_doc)
        del word_doc["_id"]
        self.write(word_doc)

class Application(tornado.web.Application):
    def __init__(self, db):
        handlers = [(r"/(\w+)", WordHandler)]
        self.db = db
        tornado.web.Application.__init__(self, handlers, debug=True)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(db))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
