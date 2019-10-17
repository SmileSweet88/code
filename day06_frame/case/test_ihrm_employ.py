import requests
import unittest

from day06_frame.api.ihrm_employ_api import IhrmEmploy
from day06_frame.api.ihrm_login_api import IhrmLogin
from day06_frame.constant import constant
import pymysql


class TestIhrmEmpoly(unittest.TestCase):
    id = ""

    def setUp(self):
        self.session = requests.session()
        self.ihrmEmploy = IhrmEmploy()

    def tearDown(self):
        self.session.close()

    def test_01_add_employ(self):
        print("新增员工时判断token 值：", constant.GrobleToken)
        if constant.GrobleToken is None:
            login = IhrmLogin()
            login.ihm_login(self.session, "13800000002", "123456")

        jsonData = {
            "username": "hello411q",
            "mobile": "16685101114",
            "workNumber": "13145201314"
        }
        response = self.ihrmEmploy.add_employ(self.session, jsonData)
        result = response.json()
        print(result)
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("成功", result.get("message"))
        self.assertIn(TestIhrmEmpoly.id, response.text)

        # con = pymysql.Connect(host="182.92.81.159",
        #                       user="readuser",
        #                       password="iHRM_user_2019",
        #                       database="ihrm", port=3306,
        #                       autocommit=True)
        # cur = con.cursor()
        # sql = 'select id from bs_user where username = "hello411q"'
        # cur.execute(sql)
        # dataDb = cur.fetchone()
        # print("数据库读取数据： ", dataDb)
        # empId = dataDb[0]
        # cur.close()
        # con.close()
        TestIhrmEmpoly.id = result.get("data").get("id")
        # TestIhrmEmpoly.id = empId
        print("添加：", result)
        print("添加后的id 值 ：", TestIhrmEmpoly.id)

    def test_02_modify_employ(self):
        data = {
            "username": "2aaq_修改",
            "mobile": "12885201310"
        }
        response = self.ihrmEmploy.modify_employ(self.session, TestIhrmEmpoly.id, data)
        result = response.json()
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("成功", result.get("message"))
        self.assertIn(TestIhrmEmpoly.id, response.text)
        print("修改：", result)

    def test_03_search_employ(self):
        response = self.ihrmEmploy.find_employ(self.session, TestIhrmEmpoly.id)
        result = response.json()
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("成功", result.get("message"))
        self.assertIn(TestIhrmEmpoly.id, response.text)
        print("查询：", result)

    def test_04_delete_employ(self):
        response = self.ihrmEmploy.del_employ(self.session, TestIhrmEmpoly.id)
        result = response.json()
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("成功", result.get("message"))
        self.assertEqual(None, result.get("data"))
        print("删除：", result)
