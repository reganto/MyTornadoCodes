import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload", UploadHandler)
        ]
        tornado.web.Application.__init__(self, handlers)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("tornadoUpload.html")

class UploadHandler(tornado.web.RequestHandler):
    def post(self):

        try:
            file1 = self.request.files['file1'][0]
        except:
            file1=None
        original_fname = file1['filename']
        m = original_fname.split('.')
        n = '1.'+m[1]

        output_file = open("static/uploads/" + n, 'wb')
        output_file.write(file1['body'])


        self.render('image.html',n=n)

settings = {
'template_path': 'templates',
'static_path': 'static',
"xsrf_cookies": False

}
application = tornado.web.Application([
   (r"/", IndexHandler),
            (r"/upload", UploadHandler)


], debug=True,**settings)



print ("Server started.")
if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
