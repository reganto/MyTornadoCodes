from tornado.web import UIModule


class BookModule(UIModule):
    def render(self, book, format):
        return self.render_string(
            'modules/book.html',
            book=book,
            format=format
        )
