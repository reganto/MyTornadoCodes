from handlers.home import HomeHandler
from handlers.recommended import RecommendedHandler
from handlers.add_book import AddBookHandler
from handlers.edit import BookEditHandler

url_patterns = [
    (r"/", HomeHandler),
    (r"/recommended", RecommendedHandler),
    (r"/addbook", AddBookHandler),
    (r"/add", BookEditHandler),
    (r"/edit/([0-9Xx\-]+)", BookEditHandler),
]
