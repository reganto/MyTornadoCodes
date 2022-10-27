import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from PIL import Image

import redis
from io import BytesIO
import base64


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
        #im = Image.open(file1)
        output = BytesIO(file1['body'])
        #im.save(output,im.format)
        r = redis.StrictRedis(host='localhost')
        m = original_fname.split('.')
        n = '1.'+m[1]
        r.set(n, output.getvalue())
        h=r.get(n)
        output = BytesIO(h)
        s = output.getvalue()
        str = base64.b64encode(s)
        output.close()
        self.render("image.html",img_tag = str)


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
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
