import os
import os.path

SETTINGS = dict(
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    cookie_secret = os.urandom(16), 
    _xsrf_cookies = True,
    login_url = "/login"
)

