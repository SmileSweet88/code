import logging
import unittest
import requests
from parameterized import parameterized
import json
from day06_frame.api.ihrm_login_api import IhrmLogin
from day06_frame.constant import constant
from day06_frame.constant.constant import workPath, GrobleToken, log_config


def getData():
    listData = []
    if GrobleToken is None:
        listData.append(("13800000002", "123456", "成功", 10000, True))
    else:
        with open(workPath + "/data/ihrm_login_data.json", encoding="utf-8") as f:
            result = json.load(f)
            for val in result.values():
                mobile = val.get("mobile")
                password = val.get("password")
                message = val.get("message")
                code = val.get("code")
                success = val.get("success")
                listData.append((mobile, password, message, code, success))
    print("参数化：登录数据： ", listData)
    return listData

log_config()
class TestIhrmLogin(unittest.TestCase):
    def setUp(self):
        self.session = requests.session()
        self.ihrmLogin = IhrmLogin()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(getData())
    def test_login(self, mobile, password, message,code,success):
        response = self.ihrmLogin.ihm_login(self.session, mobile, password)
        result = response.json()

        print(result)
        self.assertIn(message, result.get("message"))
        self.assertEqual(code, result.get("code"))
        self.assertEqual(success, result.get("success"))
