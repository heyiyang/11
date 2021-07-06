#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/6/11 18:54
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
"""
1. 把字符串转成列表
2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套
"""
# str1 = "hello python lemon 柠檬" # ["hello","pyhton","lemon"]
# list1 = list(str1)
# print(list1)

# 扩展：["hello","python","lemon"]
# split （str,num）: 字符串内置函数：将一个字符串以一个指定的符号截断，返回列表--num -截取次数，默认-1==最后
# list2 = str1.split(" ")
# print(list2)

# 方法一：
# num1 = int(input("请输入整数："))
# sum1 = 0
# for i in range(num1):
#     sum1 += i
# print(sum1)
# 方法二： 定义成函数
# def add_fun(num2):
#     sum1 = 0
#     for i in range(num2):
#         sum1 += i
#     return sum1
# result = add_fun(100)
# print("这个整数序列的和是：{}".format(result))
# def object(item):
#     if isinstance(item,list) or isinstance(item,str) or isinstance(item,dict):
#     # if type(item)==list or type(item)==str or type(item) == dict:
#         length = len(item)  #取长度
#         if length >= 5:
#             print("True")
#         else:
#             print("False")
#     else:
#         print("你输入的数据类型不能计算长度！")
# object(12)

"""
http协议 --接口自动化： 第三方库：别人写好的，拿来用的 ---  
第一步：安装  ==requests
1、pip： 安装Python的第三方库  pip install requests
2、pycharm安装 第三方库
第二步： 导入

requests库所有的参数 格式都必须是字段格式！！！ --语法
http://47.115.15.198:7001/smarthome/user/register
{"phone": "15815541763",
  "pwd": "lemon123",
  "rePwd":"lemon123",
  "userName":"你猪八戒",
  "verificationCode":"611203"}
X-Lemonban-Media-Type:lemonban.v2
Content-Type:application/json

http协议的请求方法  ,返回值是响应消息
"""
import requests,jsonpath
import pprint   # pprint  --prety print==格式美观
# 注册接口

url_register = "http://47.115.15.198:7001/smarthome/user/register"   # 定义接口地址
data_register = {"phone": "15925541763","pwd": "lemon123","rePwd":"lemon123","userName":"fanxn","verificationCode":"611203"}
head = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
response = requests.post(url=url_register,json=data_register,headers=head)   # 方法传参  -关键字
# pprint.pprint(response.json())

#登录接口
url_login = "http://47.115.15.198:7001/smarthome/user/login"   # 定义接口地址
data_login = {"pwd": "lemon123","userName": "fanxn"}
head_login = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
response_l = requests.post(url=url_login,json=data_login,headers=head_login)   # 方法传参  -关键字
pprint.pprint(response_l.json())
login_resp = response_l.json()
"""
{'code': '0',
 'data': {'id': 616,
          'phone': '15925541763',
          'token_info': {'expires_in': '2021-06-11 20:59:24',
                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoiNjE2IiwiZXhwIjoxNjIzNDE2MzY0fQ.Xl766eY8p8mKrJJ0rvZ6EuPvB9EqwS8H_ScO35rvqGa8njBaMAPdfaY2kEKTww6TxtdSktaoyh3rqv_1ScicBQ',
                         'token_type': 'Bearer'},
          'type': False,
          'user_name': 'fanxn'},
 'msg': '操作成功'}
"""
# 获取id  token ？？
# 一、字典取值获取：--字典的嵌套取值
# id = login_resp["data"]["id"]
# token = login_resp["data"]["token_info"]["token"]
# 二、jsonpath -- 第三方库 ： 安装 + 导入
id = jsonpath.jsonpath(login_resp,"$..id")[0]  # 防止有多个，保存列表里
token = jsonpath.jsonpath(login_resp,"$..token")[0]
# print(id,token)

#完善信息接口
url_comp = "http://47.115.15.198:7001/smarthome/merchant/complete"   # 定义接口地址
data_comp = {
  "address": "湖南省长沙市岳麓区xx街道12345678901234567",
  "establishDate": "2021-04-02",
  "legalPerson": "韩",
  "licenseCode": "xh430646464sdfa",
  "licenseUrl": "http://127.0.0.1/smarthome/aaa.jpg",
  "merchantName": "青海文梅科技有限公司1234567890",
  "merchantType": 5,
  "registerAuthority": "城中区派出所123456789012345678901234",
  "tel": "18888888888",
  "userId": id,
  "validityDate": "2033-05-02"
}
# head_comp = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json",
#               "Authorization":"Bearer "+token}
# response = requests.put(url=url_comp,json=data_comp,headers=head_comp)   # 方法传参  -关键字
# print(response.json())

"""
扩展一个面试题：请一个获取百度页面请求么？

问题：
1、有乱码
text：获取响应内容，自动解码--80%以上的页面都可以使用
content.decode("utf8"):手动指定解码方式 
2、页面错的-- 百度服务器没有返回正确的页面！
大型服务器： 反爬虫机制 
User-Agent：Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
"""
def baidu_re():
    url_baidu = "https://www.baidu.com/"
    head_baidu = {"User-Agent":
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    res_baidu = requests.get(url=url_baidu,headers=head_baidu)
    # print(res_baidu.text)
    print(res_baidu.content.decode("utf8"))

# 百度 带参数的请求：
"""
https://www.baidu.com/s?wd=柠檬班
"""
def baidu_pa():
    url_baidu = "https://www.baidu.com/s"
    head_baidu = {"User-Agent":
                          "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    para = {"wd":"柠檬班"}
    res_baidu = requests.get(url=url_baidu,headers=head_baidu,params=para)  # 带参数的请求
    print(res_baidu.content.decode("utf8"))

#上传接口
url = "http://47.115.15.198:7001/smarthome/file/upload"
head1 =  {"X-Lemonban-Media-Type":"lemonban.v2"}
# 上传的文件参数
files = {"file": ("test.png", open("test.png", "rb"), "image/png")}
# 发送请求
response_u = requests.post(url=url, files=files,headers=head1)
# 打印结果
print(response_u.json())








