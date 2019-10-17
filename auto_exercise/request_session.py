import requests

# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify GET

# 登录：http://localhost/index.php?m=Home&c=User&a=do_login POST

# 登录提交的参数: {"username":"xxxxx","password":"yyyy","verify_code":"zzzz"},
# 非 JSON
# 提交我的订单：http://localhost/Home/Order/order_list.html GET
# cookie 中实现出现大量的代码冗余，
# 于是出现了session封装Cookie的提取与提交，以简化代码

# 创建session对象
session = requests.session()
response1 = session.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response1.status_code)
print(response1.content)
# 获取cookie 信息
co = response1.cookies
print(co)
print("*" * 100)

loginUrl = "http://localhost/index.php?m=Home&c=User&a=do_login"
myData = {"username": "13500000000", "password": "123456", "verify_code": "8888"}
response2 = session.post(loginUrl, data=myData)
print(response2.status_code)
print(response2.json())
coo = response2.cookies
print("登录成功---》 ",coo)
print("*" * 100)

response3 = session.get("http://localhost/Home/Order/order_list.html")
print(response3.status_code)
print(response3.text)
print("*" * 100)






































