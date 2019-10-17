import requests
url = "http://182.92.81.159/api/sys/login"
jsonData = {"mobile":"13800000002","password":"123456"}
#
response = requests.post(url,json=jsonData)
print(response.status_code)
print(response.text)
print(response.headers.get("Content-Type"))