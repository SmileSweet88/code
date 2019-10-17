import time
import unittest

from BeautifulReport import BeautifulReport
import logging

from day06_frame.constant.constant import workPath, log_config

from day06_frame.case.test_ihrm_employ import TestIhrmEmpoly
from day06_frame.case.test_ihrm_login import TestIhrmLogin

log_config()
try:
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(TestIhrmLogin))
    suit.addTest(unittest.makeSuite(TestIhrmEmpoly))
    # fileName = "{}ihrm_employ.html".format(time.strftime("%Y%m%d%H%M%S"))
    fileName = "report.html"
    filePath = workPath + "/report/"
    BeautifulReport(suit).report(filename=fileName, description="员工模块：增删改查", log_path=filePath)
except Exception as es:
    print("**************")
    logging.info(es)