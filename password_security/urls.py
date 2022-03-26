from handlers.home import HomeHandler
from handlers.login import LoginHandler

url_patterns = [
    (r"/", HomeHandler),
    ("/user/login", LoginHandler),
]
