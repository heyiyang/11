#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/6/9 19:15
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 -- if
2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
注：num表示课堂人数。如果大于5，输出人数。
3、list1 = ['倾卿', '沐槿', '喜君', '可口', '晨雾', '繁星']
列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。--list2=[]
方法1： 手动扩充--字典--存放在列表里面；{} --简单
dict1 = {"name":"倾卿","gender":"male","age":18,"city":"深圳"}
dict2 = {"name":"沐槿","gender":"male","age":18,"city":"深圳"}
dict3 = {"name":"喜君","gender":"male","age":18,"city":"深圳"}
dict4 = {"name":"可口","gender":"male","age":18,"city":"深圳"}
dict5 = {"name":"晨雾","gender":"male","age":18,"city":"深圳"}
dict6 = {"name":"繁星","gender":"male","age":18,"city":"深圳"}
list2 = [dict1,dict2,dict3,dict4,dict5,dict6]
print(list2)
方法2： 自动--dict（）--不强制-- for循环 ，list2.append() --- 难度

4、for循环遍历其他的数据类型 --字典，列表 元组
'''
# a=[1,2,'6','summer']
# if "i" in a:
#     print("i是这个列表的成员！")
# else:
#     print("i不是列表的成员")
#
# dict_1={"class_id":45,'num':20}
# num = dict_1.get("num")  # 字典的取值
# # dict_1["num"]
# if num > 5:
#     print("这个班级的人数是：{}".format(num))
# else:
#     print("班级人数不5人！")

# #不唯一的
# list1 = ['倾卿', '沐槿', '喜君', '可口', '晨雾', '繁星']
# for name in list1:
#     print(name)
# list2 = [] #空列表
# for i in range(len(list1)):
#     dict1 = dict(name=list1[i],age=18,gender="male",city="北京")
#     list2.append(dict1)
# print(list2)
# dict6 = {"name":"繁星","gender":"male","age":18,"city":"深圳"}
# for i in dict6:
#     print(dict6.get(i))

'''
python的函数：
函数使用常用：一段代码频繁使用，封装成函数  ---  写一次就够了，下次再用的话去调用！==提高代码的复用率
def 函数名(): --- 命名规则？见名知意
    函数体-- 实现功能代码段
1、定义函数-- def，不会被执行；   调用函数--只有被调用的时候才会被执行--怎么调用？
2、一些经常变化的内容 不适合放在函数体写死  -- 最好参数化

函数参数定义：
1、定义-形参--变量
2、调用函数-传参 --实参-值

定义参数的类型：
1、必备参数：定义了必须要传入，不传入报错
2、默认参数（缺省参数）：定义的时候给了一个默认值，调用时不需要传入-默认值，传入--真正传入的值
注意： 需要再非默认参数后面
3、不定长参数 == 不确定多长
使用场景：参数不确定是否有的时候，不定长接受！
*args：当前面的参数都接受完了之后，剩下多余的参数都会被这个不定长参数接受，并且以元组的格式保存起来  == 位置传参
注意： 1）名字 变化，使用习惯 不会改变名字！
      2）位置不一定要在最后,根据需求放位置
**kwargs ：当前面的参数都接受完了之后，剩下多余的参数都会被这个不定长参数接受，并且以字典的格式保存起来  == 关键字传参
注意： 1）名字 变化，使用习惯 不会改变名字！
      2）位置一定要在最后
      
函数调用时传入参数方式：
1、位置传参：位置要求不能乱，依次传参
2、关键字传参：指定形参的变量名 进行传参 == 跟位置无关 ==准确
3、混合传参：关键字参数必须要在位置参数的后面，否则报错;而且不要重复传参
def good_job(salary,bonus,subsidy=500,*args,**kwargs):
    print("参数salary：{}".format(salary))
    print("参数bonus：{}".format(bonus))
    print("参数subsidy：{}".format(subsidy))
    print("参数args:{}".format(args))
    print("参数kwargs:{}".format(kwargs))
    sum1 = salary + bonus + subsidy
    for i in args:
        sum1 += i
    for j in kwargs:
        sum1 += kwargs[j]
    print("工资总和是：{}".format(sum1))
    
函数返回值：
使用场景：函数有需要给使用者抛出数据，后续使用== 改数据 返回值！
1、可以有，也可以没有 == return ;没有返回值 == None
2、可以多个么？== 逗号隔开进行返回，接受的时候元组保存
3、定义之后如何使用？--接受了后续 代码使用
4、返回值标志着代码的结束--后续代码不会再执行了！--放在函数最后

代码运行出错了，使用调试功能单步运行：--哪一行代码出错？
1、断点 --某行 点击--红点
2、点击debug 按钮--进入debug模式
3、单步执行按钮：
'''
print("666")
def good_job(salary,bonus,subsidy=500,*args,**kwargs):
    sum1 = salary + bonus + subsidy
    for i in args:
        sum1 += i
    for j in kwargs:
        sum1 += kwargs[j]
    return sum1,salary
    print("这个代码结束了么?")

# 用result 这个变量接受 函数的调用 = 返回值
result = good_job(10000,1500,800,100,200,300,a=100,b=100,c=300)  # 调用函数
print(result)
# if result > 12000:
#     print("这个工作的最终薪资是{},这是一个好的工作！".format(result))
# else:
#     print("钱太少 我不去！")

'''
内置函数：
print（）
input（）
type（）
isinstance()
len()
range()
str().int().float() list() tuple() dict() set()
字符串内置的方法： format，index find，replace，
列表内置方法：append，insert，pop，remove，extend，clear，count，index
字典：get，update，pop，keys  values， items
'''

"""
接口自动化： 第三方库：别人写好的，拿来用的 ---  安装+ 导入  ==requests
pip： 安装Python的第三方库  pip install requests
"""