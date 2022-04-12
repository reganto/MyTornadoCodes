from handlers.home import HomeHandler
from handlers.alpha import ManageAlphaHandler

url_patterns = [
    (r"/", HomeHandler),
    (r"/poem", ManageAlphaHandler)
]
