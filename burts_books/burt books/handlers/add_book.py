from handlers.base import BaseHandler


class AddBookHandler(BaseHandler):
    def get(self):
        self.render('books/show_form.html', page_title='add new book')