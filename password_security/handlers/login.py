from handlers.base import BaseHandler
import redis_connection

class LoginHandler(BaseHandler):
    def __init__(self):
        self.user_ip = self.request.remote_ip
        if redis_connection.getVariable(self.user_ip) is None:
            redis_connection.setVariable(self.user_ip, 0)
        self.security_counter = int(redis_connection.getVariable(self.user_ip))        

    def get(self):
        sc = 0
        if  self.security_counter > 3:
            sc = 1
            self.render('auth/login.html', sc=sc)
        self.render('auth/login.html', sc=0)

    def post(self):
        this_username = self.get_body_argument('username')
        this_password = self.get_body_argument('password')

        username = 'foofoofo'
        password = 'foofoofo'

        if (this_username == username) and (this_password == password):
            self.write('Login done successfully . . .')
        else:
            self.security_counter += 1
            redis_connection.setVariable(self.user_ip, self.security_counter)
            self.write('Your username or password is incorrect . . . ')
