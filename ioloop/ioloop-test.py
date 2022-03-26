from tornado.ioloop import PeriodicCallback, IOLoop
from tornado.httpclient import AsyncHTTPClient
import sys
import json
from pprint import pprint

counter = 0

def my_func():
    global counter
    counter += 1
    print(counter)

def callback():
    print('eggs')

def on_stdin(fd, events):
    content = fd.readline()
    if content == 'end\n':
        print('handler removed!')
        IOLoop.instance().remove_handler(fd)
    elif content == 'update\n':
        print('handler updated!')
        IOLoop.instance().update_handler(fd, IOLoop.WRITE)
    print(content)

async def food():
    print('Monkey said: Feed me!')
    client = AsyncHTTPClient()
    response = await client.fetch('https://reqres.in/api/users/')
    return response


if __name__ == '__main__':
    #c = PeriodicCallback(my_func, 1000)
    #c.start()
    #IOLoop.instance().add_callback(callback)
    #IOLoop.instance().add_handler(sys.stdin, on_stdin, IOLoop.READ)
    IOLoop.instance().call_later(1, callback)
    IOLoop.instance().call_at(IOLoop.time(5000), my_func)
    IOLoop.instance().start()
    #response = IOLoop.instance().run_sync(food, 2000)
    #pprint(json.loads(response.body))
  
