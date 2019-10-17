import requests
url = "http://182.92.81.159/api/sys/login"
jsonData = {"mobile":"13800000002","password":"123456"}
#
response = requests.post(url,json=jsonData)
 
print("获取响应行")
# 获取响应状态码
print("响应状态码",response.status_code)
# 获取接口url
print("接口url",response.url)
print("*"*50)
# 把响应数据转成文本
print("响应头")

# 获取响应头的所有内容
print("响应头的所有内容",response.headers)
# 获取响应头的指定内容
print("获取响应头的指定内容",response.headers.get("Content-Type"))
# 获取cookies 信息
print("获取cookies 信息",response.cookies)

# 获取字符集
print("获取字符集",response.encoding)
print("*"*50)

print("响应体")
# 以文本的形式显示响应信息
print("以文本的形式显示响应信息",response.text)
# 以二进制的形式显示响应信息
print("以二进制的形式显示响应信息",response.content)
# 以json 的形式显示响应信息
print("以json 的形式显示响应信息",response.json())
# 获取响应体中的指定数据
print(response.json().get("message"))
