__author__ = 'admin'

import redis
import tornado.web
r = redis.StrictRedis(host='localhost', port=6379, db=0)

#print(r.get('foo'))
info=r.info()
print(info['used_memory_human'])
#['used_memory_human']



