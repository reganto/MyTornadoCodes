import logging

import bcrypt

from handlers.base import BaseHandler
from models import User, session


logger = logging.getLogger('Reganto')


class SignupHandler(BaseHandler):
    def post(self):
        this_username = self.get_body_argument('username', ' ', True)
        this_password = self.get_body_argument('password', ' ', True)

        hashed_password = bcrypt.hashpw(
            this_password.encode('utf-8'), bcrypt.gensalt()
        )

        this_user = User(
            username=this_username, 
            password=hashed_password
        )
        session.add(this_user)
        try:
            result = session.commit()
        except Exception as e:
            logger.info('signup failed')
            self.write(
                {
                    'status': 'failed',
                    'description': str(e),
                }
            )
            session.rollback()
        else:
            logger.info('User added to db')
            self.write(
                {
                    'status': 'success'
                }
            )


class SigninHandler(BaseHandler):
    def post(self):
        this_username = self.get_body_argument('username', ' ')
        this_password = self.get_body_argument('password', ' ')

        try:
            record = session.query(User).filter_by(username=this_username).first()
        except Exception as e:
            pass
        else:
            if record is None:
                logger.info('User already exist')
                self.write(
                    {
                        'status': 'user does not exist'
                    }
                )
                return
            result = bcrypt.checkpw(
                this_password.encode('utf-8'), 
                record.password.encode('utf-8')
            )

        if result:
            logger.info('login successfully')
            self.set_secure_cookie('user', this_username)
            self.write(
                {
                    'status': 'success',
                    'cookie': self.get_cookie('user')
                }
            )
        else:
            logger.info('login failed')
            self.write(
                {
                    'status': 'failed'
                }
            )