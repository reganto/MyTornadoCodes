__author__ = 'admin'

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import base64
import uuid

from tornado.options import define,options
define("port",default=8001,help="run on the given port",type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("count")
        count = int(cookie) + 1 if cookie else 1

        countString = "1 time" if count == 1 else "%d times" % count

        self.get_secure_cookie("count",str(count))

        self.write(
            '<html><head><title>Cookie Counter</title></head>'
            '<body><h1>You&rsquo;ve viewed this page %s times.</h1>' % countString + '</body></html>'
        )

if __name__ == '__main__':
    tornado.options.parse_command_line()

    setting = {
        "cookie_secret" : base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    }

    application = tornado.web.Application([(r'/', MainHandler)], **setting)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



