#!/usr/bin/env python

import os.path
import sqlite3
import json

from tornado.web import RequestHandler, Application, url
from tornado.ioloop import IOLoop
from tornado.websocket import WebSocketHandler
from tornado.options import parse_command_line

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *args: os.path.join(ROOT, *args)


class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html')


class DictionaryHandler(WebSocketHandler):
    def on_message(self, data):
        '''query from database for specific word'''
        data = json.loads(data) # Serialize data
        if data.get('m') is not None: # Insert new row to database
            self.application.insert_to_db(data.get('w'), data.get('m'))
        try:
            meaning = self.application.query_on_db(data.get('w'))    
        except Exception as e:
            print('Error %s' % e)
            self.write_message({'code': 404})
        else:
            self.write_message({'code': 200, 'w': data.get('w'), 'm': meaning}) 


class AddWordHandler(RequestHandler):
    def get(self):
        '''create dictionary table with two column. w-> word, m-> meaning'''
        cursor = self.application.connection.cursor()
        cursor.execute("CREATE TABLE dictionary(id integer PRIMARY KEY, w text, m text)")

#    def post(self):
#        '''add word to database'''
#        w = self.get_body_argument('w', None)
#        m = self.get_body_argument('m', None)
#
#        cursor = self.application.connection.cursor()
#        cursor.execute("INSERT INTO dictionary(w, m) VALUES(?, ?)", (w, m))
#        self.write('word added')

    def on_finish(self):
        connection.commit()


class App(Application):
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        url_patterns = [
                url('/', IndexHandler, name='index'),
                url('/query/', DictionaryHandler, name='dictionary'),
                url('/add/', AddWordHandler, name='add'),
                ]
        settings = {
                'debug': True,
                'template_path': path('templates'),
                }
        super().__init__(url_patterns, **settings)
        
    def insert_to_db(self, word, meaning):
        """Insert a row to database"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO dictionary(w, m) VALUES(?, ?)", (word, meaning))
        except Exception as e:
            print('Error %s' % e)
        else:
            self.connection.commit()
            return True
            
    def query_on_db(self, word):
        """Query on db to specific row"""
        try:
            cursor = self.connection.cursor()
            query = cursor.execute(f"SELECT * FROM dictionary WHERE w = '{word}'")
            _, word, meaning = query.fetchall()[0]
        except Exception as e:
            raise e
        else:
            return meaning
            



def make_app():
    parse_command_line()
    App().listen(8009)
    IOLoop.current().start()


if __name__ == '__main__':
    make_app()

