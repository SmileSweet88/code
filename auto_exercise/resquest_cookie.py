import requests

# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify GET

# 登录：http://localhost/index.php?m=Home&c=User&a=do_login POST

# 登录提交的参数: {"username":"xxxxx","password":"yyyy","verify_code":"zzzz"},
# 非 JSON
# 提交我的订单：http://localhost/Home/Order/order_list.html GET
response1 = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response1.status_code)
print(response1.content)
# 获取cookie 信息
co = response1.cookies
sessionId = co.get("PHPSESSID")
print(sessionId)
print("*" * 100)

loginUrl = "http://localhost/index.php?m=Home&c=User&a=do_login"
myData = {"username": "13500000000", "password": "123456", "verify_code": "8888"}
# 把cookie 信息传递回服务器
response2 = requests.post(loginUrl, data=myData, cookies={"PHPSESSID": sessionId})
print(response2.status_code)
print(response2.json())
coo = response2.cookies
print("登录成功---》 ",coo)
print("*" * 100)

# 把cookie 信息传回给服务器
response3 = requests.get("http://localhost/Home/Order/order_list.html", cookies={"PHPSESSID": sessionId})
print(response3.status_code)
print(response3.text)
print("*" * 100)






































