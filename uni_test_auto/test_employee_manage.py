import requests
import unittest


class TestEmManage(unittest.TestCase):
    eid = ""

    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        cls.emUrl = "http://182.92.81.159/api/sys/user"

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def test_01_login(self):
        loginUrl = "http://182.92.81.159/api/sys/login"
        loginData = {"mobile": "13800000002", "password": "123456"}
        response = self.session.post(loginUrl, json=loginData)
        self.assertEqual(response.status_code, 200)
        self.assertIn("成功", response.json().get("message"))

    def test_02_add(self):
        addData = {
            "username": "张12",
            "mobile": "12121212212",
            "timeOfEntry": "2019-10-01",
            "formOfEmployment": 1,
            "workNumber": "0000019",
            "departmentName": "开发部",
            "departmentId": "1066240656856453120",
            "correctionTime": "2019-12-31T16:00:00.000Z"
        }
        response = self.session.post(self.emUrl, json=addData)
        TestEmManage.eid = response.json().get("data").get("id")
        self.assertEqual(response.status_code, 200)
        self.assertIn("成功", response.json().get("message"))
        print("添加成功:", response.json())

    def test_03_find(self):
        response = self.session.get(self.emUrl + "/" + TestEmManage.eid)

        self.assertEqual(response.status_code, 200)
        self.assertIn("成功", response.json().get("message"))
        print("查询成功:", response.json())
