import unittest
import json
from day06_frame.api.tpshop_login_api import Login
from parameterized import parameterized
import requests

from day06_frame.constant.constant import workPath


def getData():
    data = []
    with open(workPath + "/data/login_data.json", encoding="utf-8") as file:
        result = json.load(file)
        for i in result.values():
            temp = (i.get("username"),
                    i.get("password"),
                    i.get("veritycode"),
                    i.get("is_success"),
                    i.get("expect"))
            data.append(temp)

    print("参数化数据：", data)
    return data


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.session = requests.session()
        self.login = Login()

    def tearDown(self):
        self.session.close()

    def test_1_get_verify_code(self):
        response = self.login.get_verity_code(self.session)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))

    @parameterized.expand(getData())
    def test_2_go_login(self, username, password, verity_code, is_success, expect):
        response_verity = self.login.get_verity_code(self.session)
        data = [username, password, verity_code]
        response_login = self.login.go_login(self.session, data)
        # print(response_login.text)
        self.assertIn(expect, response_login.json().get("msg"))
