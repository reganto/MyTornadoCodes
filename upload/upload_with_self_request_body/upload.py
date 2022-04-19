import tornado.ioloop
import tornado.web
import tornado.httpserver
import os.path
import tornado.httpclient



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/myform", FormHandler),
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            debug = True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class FormHandler(tornado.web.RequestHandler):
    def put(self):
        file = self.request.body
        # sample = str(file)
        # sample = sample.split(".")
        # sample = sample[len(sample)-1]
        # self.write(sample)
        # f = open("static/uploads/"+"01", "wb")
        # f.write(file)
        # f.close()
        self.write(file)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
