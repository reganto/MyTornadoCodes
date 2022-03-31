import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.locale
import os.path
import pymongo

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

#conn = pymongo.Connection("localhost",27017)

conn = pymongo.MongoClient("localhost",27017)
db = conn.test3
names = db.collection_names()
print(names)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",MainHandler),
            (r"/recommended",RecommendedHandler),
        ]
        setting = dict(
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static"),
            ui_modules = {'Book':BookModule},
            debug = True
        )
        tornado.web.Application.__init__(self,handlers,**setting)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            page_title = "Burt's Books | Home",
            header_text = "Welcome to Burt's Books!"
        )

class BookModule(tornado.web.UIModule):
    def render(self,book):
        return self.render_string('modules/book.html',book=book)
    def embedded_javascript(self):
        return "document.write(\"hi!\")"
    def embedded_css(self):
        return ".book {background-color:rgb(255,0,0)}"
    def html_body(self):
        return "<script>document.write(\"Hello!\")</script>"

class RecommendedHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "recommended.html",
            page_title = "Burt's Book | Recommended Reading",
            header_text = "Recommended Reading",
            books = [
                {
                    "title":"Programming Collective Intelligence",
                    "subtitle":"Building Smart Web 2.0 Application",
                    "image":"/static/images/Desert.jpg",
                    "author":"Toby Segaran",
                    "date_added":1310248056,
                    "date_released":"August 2007",
                    "isbn":"978-0-596-52932-1",
                    "description":"<p>This is fascinating book demonstrate.</p>"
                },
            ]
        )


if __name__ == '__main__' :
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
