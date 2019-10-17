# 实现iHr系统的员工模块的增删改查

# 登录接口：
#     url: http://182.92.81.159/api/sys/login
#     method : post
#     提交数据 {"mobile":"13800000002","password":"123456"}

# 员工接口
#     url: http://182.92.81.159/api/sys/user
#   通过session的方式实现 增删改查
#


import requests
import pymysql

# session = requests.session()
# # 登录
# loginUrl = "http://182.92.81.159/api/sys/login"
# loginData = {"mobile": "13800000002", "password": "123456"}
# responseL = session.post(loginUrl, json=loginData)
# print(responseL.status_code)
# print(responseL.json())
#
# # 添加员工
# addUrl = "http://182.92.81.159/api/sys/user"
# addData = {
#     "username": "yes2",
#     "mobile": "17111111112",
#     "timeOfEntry": "2019-10-01",
#     "formOfEmployment": 1,
#     "workNumber": "0000019",
#     "departmentName": "开发部",
#     "departmentId": "1066240656856453120",
#     "correctionTime": "2019-12-31T16:00:00.000Z"
# }
# response1 = session.post(addUrl, json=addData)
# eId = response1.json().get("data").get("id")
# print(eId)
# print(response1.json())
#
# # 修改员工
# modifyData = {
#     "username": "modi_yess",
#     "mobile": "17111111112",
#     "password": "9ad6255e79b13e1d1644f1314dff81af",
#     "workNumber": "0"
# }
# response2 = session.put(addUrl + '/' + eId, json=modifyData)
# print("改: ", response2.json())
#
# response3 = session.get(addUrl + '/' + eId)
# print("查: ", response3.json())
#
# response4 = session.delete(addUrl + '/' + eId)
# print("删: ", response4.json())

# 通过token 方式实现, 保存登录成功之后返回的data 数据,
# 每次请求时把这个token 数据传递过去
# 登录
loginUrl = "http://182.92.81.159/api/sys/login"
loginData = {"mobile": "13800000002", "password": "123456"}
responseL = requests.post(loginUrl, json=loginData)
token = responseL.json().get("data")
print(responseL.status_code)
print(responseL.json())

# 添加员工
myHeaders = {"Authorization": token}
addUrl = "http://182.92.81.159/api/sys/user"
addData = {
    "username": "yes2",
    "mobile": "17111111112",
    "timeOfEntry": "2019-10-01",
    "formOfEmployment": 1,
    "workNumber": "0000019",
    "departmentName": "开发部",
    "departmentId": "1066240656856453120",
    "correctionTime": "2019-12-31T16:00:00.000Z"
}
response1 = requests.post(addUrl, json=addData, headers=myHeaders)
eId = response1.json().get("data").get("id")
print(eId)
print(response1.json())

# 修改员工
modifyData = {
    "username": "modi_yess",
    "mobile": "17111111112",
    "password": "9ad6255e79b13e1d1644f1314dff81af",
    "workNumber": "0"
}
response2 = requests.put(addUrl + '/' + eId, json=modifyData, headers=myHeaders)
print("改: ", response2.json())

response3 = requests.get(addUrl + '/' + eId, headers=myHeaders)
print("查: ", response3.json())

# response4 = requests.delete(addUrl + '/' + eId, headers=myHeaders)
# print("删: ", response4.json())

# host:182.92.81.159
# port:3306
# username：readuser
# password：iHRM_user_2019
conn = pymysql.connect(host="182.92.81.159", user="readuser", password="iHRM_user_2019",
                 database="ihrm", port=3306, charset='utf8')
cur = conn.cursor()
sqlD = "select * from bs_user where id = {}".format(eId)
cur.execute(sqlD)
print(cur.fetchall())
