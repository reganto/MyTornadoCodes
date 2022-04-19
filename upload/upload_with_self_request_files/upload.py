import tornado.ioloop
import tornado.web
import os.path
import tornado.httpserver

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r"/", HomeHandler),
            (r"/myform", FormHandler),
        ]
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            debug = True
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class FormHandler(tornado.web.RequestHandler):
    def post(self):
        file = self.request.files
        files_length = len(file["my_file"])
        # fileContentType = file["my_file"][0]["content-type"]
        for i in range(files_length):
            fileName = file["my_file"][i]["filename"]
            fileBody = file["my_file"][i]["body"]
            fn = fileName.split(".")
            try : 
                exist = open("static/uploads/"+str(i)+"."+fn[1], "r")
                if exist:
                    i += 1
            except :
                test_vvvvvv = 0 
                test_vvvvvv += 0 
            f = open("static/uploads/"+str(i)+"."+fn[1], 'wb')
            f.write(fileBody)
            f.close()
        self.redirect("/") 
        #     print(fileName)
        # self.write(str(file))


if __name__ == "__main__":
    http_sever = tornado.httpserver.HTTPServer(Application())
    http_sever.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
