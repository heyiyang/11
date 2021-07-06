#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/6/7 15:05 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
1、在pycharm的控制台里输入以下内容，并且以如下格式输出到控制台

2、现在有字符串：str1 = 'python hello aaa 123123aabb'
1）请取出并打印字符串中的'python'。[0:6]
2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？-- in
3）替换python为 “lemon”. -- replace
4) 找到aaa的起始位置 -- 索引
'''
# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")
# gender = input("请输入你的性别：")
# print('''********************
# 姓名：{}
# 年龄：{}
# 性别：{}
# ********************'''.format(name,age,gender))
# str1 = 'python hello aaa 123123aabb'
# print(str1[0:6:1])
# print("o a" in str1)
# print("he" in str1)
# print(str1.replace("python","lemon"))
# print(str1.find("aaa"))
# print(str1.index("aaa"))

'''
元组：tuple  （）
1、元组元素的可以包含任何的内容： 整型  浮点型  bool 字符串  list 元组 ， 元素之间用逗号 隔开
2、元组取值： 索引取值 --从0开始 
    取多个值：切片 --字符串操作一模一样
扩展：tuple的嵌套取值
3、获取元素个数  -- len() ==长度
4、tuple的元素是不可以被改变的！！ 没有增加 删除 修改的方法！
扩展：1、转化为列表--list()
     2、列表的修改方法元素的修改
     3、转化回元组！-- tuple()
5、元素可以重复
'''
# tuple1 = (20,3.14,False,"喜君",[1,2,2,3,4],(1,2,3,4))  # 定义了空元组
# print(tuple1[-1][2])
# print(tuple1)
# # tuple1[3] = "倾卿"    不可以被修改的
# list2 = list(tuple1)  # 转化为元组
# print(list2)
# list2[3] = "倾卿"
# list2[1] = "倾卿"
# list2[2] = "倾卿"
# print(list2)
# tuple2 = tuple(list2)
# print(tuple2)
# print(tuple2.count("倾卿"))

'''
字典: dict  {}  
1、元素是一对儿，键值对--key：value --字典的一个元素,元素之间用逗号隔开
2、key--表头 == 不能重复的，唯一的；而且key不能是列表和字典 -- 可变的数据类型
   value：可以任意数据类型，并且是可以重复
3、字典什么场景下是使用？--存储物体的一些属性信息  --人：名字，性别，身高 体重 年龄 城市 公司 薪资 ID
4、len() ---  统计元素个数
5、重要：字典无序的！！！--没有索引了， 不能通过索引取值！ --Python3.6版本之前 
如何取值 ？  --通过key取value 
6、key不可以改变 ，value可以被改变  --- value 增加删除修改
增删：
'''
dict1 = {"name":"sky","gender":"Female","age":18,"height":"165","weight":"45"}
# print(dict1["weight"])  # 1、通过key 取value
# print(dict1.get("weight"))  # 2、通过key 取value
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# dict1["city"] = "北京"   # key不存在的时候，增加新的键值对--新增元素
# dict1["name"] = "Wake"   # key存在的时候，修改原来的键值对 -修改元素 ==重新赋值
# print(dict1)
# # 新增多个元素 --字典合并 === key相同的话，修改原来键值对
# dict1.update({"age":"12","hobby":"学习"})
# print(dict1)
# # 删除  == 字典是无序的，没有默认最后一个说法，指定key进行删除 -键值对
# dict1.pop("age")
# dict1.clear()
# print(dict1)

'''
扩展的内容：
集合：--用的非常少 set  {} 
1、元素不能重复 == 使用场景：用来列表去重  == 把列表转化为集合,去重之后，转化为列表
'''
# list3 = [11,22,44,55,22,33,11,11,11]
# print(list3)
# set1 = set(list3)  # 把列表转化为集合
# print(type(set1))
# list4 = list(set1)
# print(list4)
'''
Python常用数据类型： 
数值型：int float 
一般： bool 
重要的数据类型： str  list  dict    === 重要！！！
了解扩展：tuple， set
'''

'''
python的控制流：
判断：if 判断
if 条件:   ---  判断（逻辑运算符，成员运算符，比较运算符）  ==成立（True） 冒号-- 后面缩进
    执行语句 （子代码） ==四个空格缩进-tab
elif 条件：判断（逻辑运算符，成员运算符，比较运算符） --- 可以没有，可多个
    执行语句 （子代码） ==四个空格缩进-tab
elif 条件：判断（逻辑运算符，成员运算符，比较运算符） --- 可以没有，可多个
    执行语句
    。。。
    。。。
else:   ---兜底 --没有条件
    执行语句-分支
    
input：在控制台输入的内容 是  字符串  == int()
'''
# money = int(input("请输入你的存款："))
# if money >= 200 :
#     print("我要买大房子！")
# elif money >= 100:
#     print("理财")
# elif money >= 50:
#     print("付房子首付！")
# elif money >= 10:
#     print("付个彩丽，娶老婆~")
# else:
#     print("继续搬砖！")

'''
循环（while--死循环）：for 循环
使用场景：遍历 -全部元素 ： 字符串，list  tuple  dict--练习
需求：每一个元素都一次取出来并打印出来！（遍历）== 冒号后面缩进 --循环体
for循环什么时候结束？  -- 元素都取完了，就结束 ，循环次数= 元素个数？

扩展手动终止循环：
1、break：跳出整个循环，后面的循环不载执行
2、continue：跳出本次循环，后面的循环依然会再执行

伴随着for循环一起使用的内置函数：
range() ：生成一个整数序列 =编号
开始数字：省略--默认值 =0
结束数字： 不省略 --必填  == 取头不取尾 +1
步长：省略： 默认=1  ==偶数 序列  奇数序列
'''
count = 0  # 计数器
str1 = "我爱柠檬班！"
for i in str1:
    if i == "柠":
        # break  # 跳出循环，后面的循环不再执行
        continue # 跳出本次循环，后面的循环依然会再执行
    print(i)
    print("*" * 20)
    count += 1
# print(count)
# print(len(str1))
#
# for j in range(2,11,2):
#     print(j)

# 生成一个字段函数：
dict1 = {"name":"tricy","age":17}

dict2 = dict(name="tricy",age=18,city="beijing")
print(dict2)

