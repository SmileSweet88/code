import requests
# 接口测试回顾：
# 首先根据URL以及请求方式定位接口资源
# 然后提交测试数据
# 最后发送接收并处理响应结果

# 例子：　百度搜索test
url = "http://www.baidu.com/s"
responeData = requests.get(url,params={"wd":"玉林地震"})
print(responeData.status_code)
print(responeData.text)
