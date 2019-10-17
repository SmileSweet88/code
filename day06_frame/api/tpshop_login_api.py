import requests

from day06_frame.constant.constant import *


class Login:
    def get_verity_code(self, session):
        """
        获取验证码
        :param session:
        :return:
        """
        response = session.get(Tpshop_BaseUrl + 'index.php?m=Home&c=User&a=verify')
        return response

    def go_login(self, session, data):
        loginUrl = Tpshop_BaseUrl + 'index.php?m=Home&c=User&a=do_login'
        requestData = {"username": data[0], "password": data[1],
                       "verify_code": data[2]}
        return session.post(loginUrl, data=requestData)
