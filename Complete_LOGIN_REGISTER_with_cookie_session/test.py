__author__ = 'e.azizi'

import tornado.httpserver
import tornado.options
import tornado.web
import tornado.ioloop
import os.path
import uuid
import hashlib
import base64
from models import *

password = '1'.encode('utf-8')

salt = uuid.uuid4().hex.encode('utf-8')
hashed_password = hashlib.sha512(password + salt).hexdigest()

m = input()

salt1 = uuid.uuid4().hex.encode('utf-8')
hashed_m = hashlib.sha512(m.encode('utf-8') + salt).hexdigest()

if (hashed_m)==(hashed_password):
    print('yes')
else:
    print('no')

print(hashed_password)
print(hashed_m)
print(salt.decode('utf-8'))
print(salt1.decode('utf-8'))
print(salt.encode('utf-8'))
print(salt1.encode('utf-8'))