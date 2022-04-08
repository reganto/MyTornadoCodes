import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
import os.path
import pymysql

from tornado.options import define, options
define("port", default=8888, type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/(\w+)", ReverseHandler),
            (r"/page/form", FormExeHandler),
            (r"/page/save", SaveWordHandler),
            (r"/page/reverse", RetriveAndReverseHandler),
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            ui_modules = {'wordprocces' : WordProccess},
        )

        tornado.web.Application.__init__(self, handlers, **settings, debug=True)

#*******************************************************************************

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, word):
        self.write(word[::-1])

class FormExeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'form.html',
        )

class SaveWordHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            conn = pymysql.connect('localhost', user='God', db='testdb', passwd='')
            cur = conn.cursor()

            word = self.get_argument("sample", "")

            sql = "INSERT INTO words (word) VALUES (%s)"
            cur.execute(sql, (word))

            cur.close()
            conn.commit()
            conn.close()
        except:
            self.write("ERROR")
        else:
            self.redirect('/')

class RetriveAndReverseHandler(tornado.web.RequestHandler):
    def get(self):
        # try:
        conn = pymysql.connect('localhost', user='God', db='testdb', passwd='')
        cur = conn.cursor()

        myword = input("Enter word for reverse:")
        sql = "SELECT * FROM words WHERE word=%s"
        cur.execute(sql, (myword))

        for word in cur:
            if word != '':
                # print(type(word)
                word = str(word)
                word = word[2:len(word)-3]
                print(word)
                self.render("route.html", word=word)

        # except:
            # self.write("ERROR")


class WordProccess(tornado.web.UIModule):
    def render(self, word):
        word = word[::-1]
        return self.render_string(
            "modules/display.html",
            word = word,
        )
#*******************************************************************************

def main():

    tornado.options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
