from handlers.base import BaseHandler


class BookEditHandler(BaseHandler):
    def data_received(self):
        pass

    def get(self, isbn=None):
        book = dict()
        if isbn:
            bookstore = self.settings['db'].bookstore
            book = bookstore.find_one({'isbn': isbn})
        self.render(
            'book_edit.html',
            page_title='Edit or Add',
            book=book
        )

    def post(self, isbn=None):
        import time

        book_fields = ['isbn', 'title', 'subtitle', 'image', \
            'author', 'date_released', 'description']
        bookstore = self.settings['db'].bookstore
        book = dict()
        if isbn: # Edit
            book = bookstore.find_one({'isbn': isbn})
        for key in book_fields:
            # TODO::verify user inputs
            book[key] = self.get_body_argument(key, None)
        if isbn:
            bookstore.save(book)
        else: # Add
            book['date_added'] = int(time.time())
            bookstore.insert(book)
        self.redirect('/recommended')
