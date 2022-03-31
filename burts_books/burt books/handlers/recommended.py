from handlers.base import BaseHandler


class RecommendedHandler(BaseHandler):
    def get(self):
        bookstore = self.settings['db'].bookstore

        books = bookstore.find()
        self.render(
            'recommended.html',
            page_title="Books | Recommended Reading",
            books=books,
            format=format
        )