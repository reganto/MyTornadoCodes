from tornado.web import RequestHandler, Application, url
from tornado.ioloop import IOLoop
from datetime import timedelta
io_loop = IOLoop.current()


def _sample():
    print("sample")


def _other():
    print("other")


class App(Application):
    def __init__(self):
        handlers = [url("/", HomeHandler, name="home")]
        settings = dict(debug=True)
        super(App, self).__init__(handlers, **settings)


class HomeHandler(RequestHandler):
    def get(self):
        self.write("foo")
        #io_loop.add_callback(_sample)
        io_loop.add_timeout(timedelta(seconds=10), _other)


def main():
    app = App()
    app.listen(8888)
    io_loop.start()


if __name__ == "__main__":
    main()

