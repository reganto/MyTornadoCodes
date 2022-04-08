import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
import os.path
from PIL import Image
import redis
from io import BytesIO
import base64

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        r = redis.StrictRedis(host='localhost')
        #im = Image.open('C:/Desert.png')
        h=r.get('imagedata')
        output = BytesIO(h)
        #im.save(output,im.format)
        s = output.getvalue()
        str = base64.b64encode(s)
        output.close()
        self.render("index.html",img_tag = str)



if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/',HelloHandler)],
        template_path = os.path.join(os.path.dirname(__file__),'templates'),

    )
    server=tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
