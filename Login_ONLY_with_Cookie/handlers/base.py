import uuid
import hashlib
from models import User
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

    def login(self, username: str, password: str) -> bool:
        """Login user with provided username and password

        :param self: An instance of Tornado.web.RequestHandler
        :param username: username that provided by user
        :type username: str
        :param password: password that provided by user
        :type password: str
        :rtype: bool
        """

        password = password.encode('utf-8')
        user = User.select().where(User.username==username)
        auth=False
        for u in user:
            salt1=(u.salt)
            salt1 = salt1.encode('utf-8')
            hashed_password = hashlib.sha512(password + salt1).hexdigest()
            if u.password == hashed_password:
                auth = True
                break
        if auth:
                self.set_secure_cookie("username", username)
                self.redirect("/")
        else:
                self.redirect("/login")


    def register(self, username: str, password: str) -> bool:
        """Register user with provided username and password

        :param self: An instance of Tornado.web.RequestHandler
        :param username: username that provided by user
        :type username: str
        :param password: password that provided by user
        :type password: str
        :rtype: bool
        """

        password = password.encode('utf-8')
        salt = uuid.uuid4().hex.encode('utf-8')
        hashed_password = hashlib.sha512(password + salt).hexdigest()
        user = User.select().where(User.username==username)
        confirm = True
        for u in user:
            if u.username == username:
                confirm = False
                break
        if confirm == True:
            User.create(
                  username=username,
                  password=hashed_password,
                  salt=salt
            )
            self.set_secure_cookie("username",self.get_argument("username"))
            self.redirect("/")
        else:
            self.redirect("/register")


    def logout(self):
        """Logout user

        :param self: An instance of tornado.web.RequestHandler
        """
        if (self.get_argument("logout", None)):
             self.clear_cookie("username")
             self.redirect('/')

    def authenticate(self) -> bool:
        """Current user is authenticated or not

        :param self: An instance of tornado.web.RequestHandler
        :rtype: bool
        """

