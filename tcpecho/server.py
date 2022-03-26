import tornado.ioloop
import tornado.gen
from tornado.iostream import StreamClosedError
import tornado.tcpserver
from tornado.options import options, define

define("port", default=8887, help="TCP port to listen on", type=int)


class EchoServer(tornado.tcpserver.TCPServer):
    @tornado.gen.coroutine
    def handle_stream(self, stream, address):
        while True:
            try:
                data = yield stream.read_until(b'\n')
                if not data.endswith(b'\n'):
                    data = data + b'\n'
                yield stream.write(data)
            except StreamClosedError:
                break
            except Exception as e:
                print(e)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    server = EchoServer()
    server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
