#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/6/2 20:39 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

"""
1、工程-lesson8182  2、Python package -- Pythonclass   3、Python file =lesson_01
标识符：python里面 自己取的名字  == 命名规则  变量  函数== 取名  ==记住
1）只能包含字母 数字 和下划线
2）不能以数字开头
3）不能使用关键字  -不需要记忆这个关键字==自动报错
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
4）建议：不同数字和字母之间用下划线隔开  --方便阅读  python_lemon_8182

Python的编码规范  ==  PeP8规范 + Python之禅

脚本运行方式：
1、右键-run  == 第一次运行推荐
2、右上角  --run
3、菜单栏--run

控制台：
print()  -- Python内置函数（Python内部已经写好的，我们可以直接使用的功能）
   功能：把内容输出到控制台

注释：
1）注释方式： 
1、单行注释 #  -- # 之后的内容都被注释
2、多行注释   """ """   '''  '''
3、快捷方式：ctrl + /  =  反注释
2）代码里为什么需要注释？？== 不写注释的程序员不是好程序员
1、方便自己和别人查看代码 
2、需求变更 == 不删除代码-注释

基础语法：
1、代码顶格编写的 
2、缩进敏感：除了父子关系的代码，都不能加缩进   == 循环， 函数
tab  -- 四个空格 
3、区分大小写的
"""
# print("82期沐槿最美！")
# print("81期亚萌最帅！")
# print("82期岳岳最美！")
# print("81期建国最帅！")

'''
常用数据类型：
1）整型--整数--int
2）浮点型 - 小数 3.14 -float
3)布尔型：True=1  False=0  ==bool
4)字符串：-str  = 用成对的引号括起来的内容 单引号（''）,双引号（""）,三引号（''' '''）
1、引号嵌套 :单双引号 --三引号？？
2、保持格式 ： --所见即所得 --三引号

变量：-- 存储数据（任何数据） 容器  ==  保险柜：钱，金条，砖头，书，日记，银行卡  证件
1、定义变量名字 == 赋值 --  变量的声明  -初始化
变量要被使用之前，必须要先声明--没有报错 
2、名字 最好见名知意 

确认数据类型的内助函数:
type():内置函数-- 功能：判断数据类型--输出这个类型-重点
isinstance():内置函数-- 功能：判断数据类型--结果是bool值

'''
# print(type(20))
# print(type(3.1415926))
# print(type(True))
# print(isinstance(20.1,int))
# print(type('''121whsdakjshsd'''))
'''
字符串常用操作： == 列表  元组
1、取值：位置有编号  -- 从0开始=索引  [索引]
2、取多个值--切片：从哪里开始  结束  步长 ==[索引头:索引尾+1：步长] == 取头不取尾  
                                        索引头：可以省略，默认值-0
                                        索引尾：可以省略，默认末尾
                                        步长：可以省略，默认1
   取最后的值： -1  =最后一个
   逆序输出：步长为-1 
'''
str1 = "82期岳岳最美！"
#       012 3 45 67
print(str1[2])
print(str1[0:len(str1):1])
# print(str1[-1])
# print(str1[::-1])


# stu_info = '''---岳岳的基本信息---
#   性别：女
#      年龄：18
#          爱好：喜欢学习
# '''
# print(stu_info)  # 没有先申明  --调用
