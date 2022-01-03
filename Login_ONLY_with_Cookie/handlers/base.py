import uuid
import hashlib
from models import User
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

    def login(self, username: str, password: str) -> None:
        """Login user with provided username and password

        :param username: username that provided by user
        :type username: str
        :param password: password that provided by user
        :type password: str
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
        else:
                raise PermissionError("You'r username or password is incorrent") 


    def register(self, username: str, password: str) -> None:
        """Register user with provided username and password

        :param username: username that provided by user
        :type username: str
        :param password: password that provided by user
        :type password: str
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
        else:
            raise ValueError('User registration failed!')


    def logout(self) -> None:
        """Logout user"""
        self.clear_cookie("username")

    def authenticate(self) -> bool:
        """Current user is authenticated or not

        :rtype: bool
        """
        if self.current_user:
            return True
        return False

    def redirect_rev(self, name: str):
        self.redirect(self.reverse_url(name))

