import requests,pprint
url_login = "http://47.115.15.198:7001/smarthome/user/login"   # 定义接口地址
data_login = {"pwd": "lemon123","userName": "fanxn"}
head_login = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
response_l = requests.post(url=url_login,json=data_login,headers=head_login)   # 方法传参  -关键字
pprint.pprint(response_l.json())
login_resp = response_l.json()

id = login_resp["data"]["id"]
token = login_resp["data"]["token_info"]["token"]
print(id,token)
url_complete = "http://47.115.15.198:7001/smarthome/merchant/complete"     #定义一个接口地址
data_complete = {
  "address": "湖南省长沙市岳麓区xx街道12345678901234567",
  "establishDate": "2021-04-02",
  "legalPerson": "韩",
  "licenseCode": "xh430646464sdfa",
  "licenseUrl": "http://127.0.0.1/smarthome/aaa.jpg",
  "merchantName": "青海文梅科技有限公司1234567890",
  "merchantType": 2,
  "registerAuthority": "城中区派出所123456789012345678901234",
  "tel": "18888888888",
  "userId": id,
  "validityDate": "2033-05-02"
}
head_complete = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json",
              "Authorization":"Bearer "+token}
response = requests.put(url=url_complete,json=data_complete,headers=head_complete)
print(response.json())