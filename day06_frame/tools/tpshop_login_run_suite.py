import time
import unittest
from BeautifulReport import BeautifulReport

from day06_frame.case.test_login import TestLogin
from day06_frame.constant.constant import workPath

suit = unittest.TestSuite()
# suit.addTest(unittest.makeSuite(TestLogin))
# suit.addTest(TestLogin("test_1_get_verify_code"))
suit.addTest(TestLogin("test_2_go_login"))
fileName = time.strftime("%Y%m%d%H%M%S") + 'tpshop_login_report.html'
BeautifulReport(suit).report(filename=fileName,
                             log_path=workPath + '/report',
                             description='登录报告！！')
