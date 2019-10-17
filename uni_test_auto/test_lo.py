import unittest
import requests


class TestLo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()

    @classmethod
    def tearDown(cls):
        cls.session.close()

    # def setUp(self):
    #     self.session = requests.session()
    #
    # def tearDown(self):
    #     self.session.close()

    def test_01_verify_code(self):
        response1 = self.session.get("http://localhost/index.php?m=Home&c=User&a=verify")
        print(response1.status_code)
        print(response1.content)
        self.assertEqual(response1.status_code, 200)
        # 用响应头的Content-Type 来断言
        self.assertIn("image",response1.headers.get("Content-Type"))

    def test_02_login(self):
        # self.test_01_verify_code()
        loginUrl = "http://localhost/index.php?m=Home&c=User&a=do_login"
        myData = {"username": "13500000000", "password": "123456", "verify_code": "8888"}
        response2 = self.session.post(loginUrl, data=myData)
        print(response2.status_code)
        print(response2.json())
        self.assertEqual(response2.status_code, 200)

    def test_03_myorder(self):
        # self.test_01_verify_code()
        # self.test_02_login()
        response3 = self.session.get("http://localhost/Home/Order/order_list.html")
        print(response3.status_code)
        con = response3.text
        self.assertIn("我的订单", con)
        self.assertEqual(response3.status_code, 200)
