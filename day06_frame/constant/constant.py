'''
tpshop 基url
'''
import os
import logging
import logging.handlers
import time

Tpshop_BaseUrl = "http://localhost/"

# 获取当前文件的绝对路径
abs_file = os.path.abspath(__file__)
# 返回到指定文件的父级目录，每次只返回一层
parentP = os.path.dirname(abs_file)
workPath = os.path.dirname(parentP)

iHrm_BaseUrl = "http://182.92.81.159/"
iHrm_user = iHrm_BaseUrl + "/api/sys/user/"

GrobleToken = None


def log_config():
    # 获取日志器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # 设置处理器
    fileName = workPath +  "/log/{}my_log.log".format(time.strftime("%Y%m%d%H%M%S"))
    to1 = logging.StreamHandler()
    to2 = logging.handlers.TimedRotatingFileHandler(fileName, when='h', interval=1,
                                                    backupCount=2, encoding="utf-8")

    # 设置格式化器
    fmt ='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)]  %(message)s'
    fotmate = logging.Formatter(fmt = fmt)

#    把格式化器
    to1.setFormatter(fotmate)
    to2.setFormatter(fotmate)
    logger.addHandler(to1)
    logger.addHandler(to2)
