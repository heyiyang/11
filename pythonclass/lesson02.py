#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/6/4 19:43
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
1. 下面哪些不能作为标识符？-- 标识符命名
1、find 2、 _num 3、7val 4、add. 5、def 6、pan 7、-print 8、open_file 9、FileName
10、print 11、INPUT 12、ls 13、user^name 14、list1 15、str_
答案：
1、find -- ok
2、_num -- ok
3、7val -- 不可以，不能以数字开头
4、add.  -- 不可以
5、def  --  不可以 关键字
6、pan  -- ok
7、-print  -- -_  不可以  只能下划线
8、open_file   -- 可以
9、FileName  -- ok ，大驼峰 --了解
10、print  -- 可以，虽然不是关键字，但是不推荐 == 导致函数不能使用
11、INPUT -- 可以，区分大小写
12、ls  --ok
13、user^name  --不可以
14、list1  ---  可以
15、str_  --可以

字符串更多 操作：
1、统计元素个数   --len()
2、常用方法的使用
1)index : 索引   --获取元素所在位置 ===  元素不存在的话，报错-代码会中断运行
2)find: 索引   --获取元素所在位置 == 元素不存在的话，返回-1，代码不会中断运行
3）count：统计元素出现的次数
4）replace：替换
'''
# str1 = "82期岳岳最美岳岳！"
# print(len(str1))
# # print(str1.index("建"))
# print(str1.find("岳"))
# print(str1.count("岳"))
# str2 = str1.replace("岳岳","绥微",1)
# print(str2)

"""
第一：字符串的格式化输出：--format
1、占坑 -- 占位符{}
2、format 变量传进去
注意：1、占位符里为空，默认按照变量的顺序 进行传输
2、指定顺序--占位符里家数字 =从0开始
3、手动和自动 -不能混合使用
第二：% 
1、占位符  -- %s （万能占位符）-字符串， %d-- 整数  %f-- 浮点型
2、传入参数  % 
"""
name = "sky"
gender = "female"
age = 20
hobby = "喜欢男"

# print('''---%s的基本信息---
# 性别：%s
# 年龄：%s
# 爱好：%s
# '''%(name,gender,age,hobby))

# print('''---{}的基本信息---
# 性别：{}
# 年龄：{}
# 爱好：{}
# '''.format(gender,name,age,hobby))

'''
python运算符
1、算术运算符： +-*/ % **
+: 1）两个数字的相加  2）两个字符串拼接
扩展：int()-- 强制数据类型的转化-整型
     str()  --强制数据类型的转化-字符串
     float（），bool(),list()  
-:两个数字的相减
*：1) 两个数字的相乘   2）字符串的重复输出 * 数字-重复次数
/: 两个数字的除法  --浮点型的结果

2、赋值运算符  = += -=
=： 右边的内容 赋值给左边的内容

3、比较运算符： >  >=  <  <=   ==  !=
1) 结果是布尔值  ： True False
2） ==  ！=  可以表示字符是否相等  -- 执行结果 vs 预期结果

4、逻辑运算符： and-与  or -或  not-非   == 结果是布尔值
and ： 真真为真
or：假假为假

5、成员运算符 ：in   not in == 结果是布尔值

'''
# a = 10 + 20
# print("hello"+ "python")
# print("hello" + str(a))
# # print("hellolemon" - "hello")  --不支持
# print(3 * 4)
# print("我爱你" * 3000)
# print(10 / 2)

# a = 20
# a += 10  #a = a + 10
# a -= 5  # a = a - 5
# print(a)
#
# print(4 > 6 or 5 > 3)
# print(not 4>5)
# # print(100 == 100)
# # print("喜君" != "喜君")
#
# str1 = "82期岳岳最美岳岳！"
# print("沐槿" in str1)

"""
列表，元组，字典，集合 
列表：[] 表示，--list
1、列表元素的可以包含任何的内容： 整型  浮点型  bool 字符串  list
2、列表取值： 索引取值 --从0开始 
    取多个值：切片 --字符串操作一模一样
扩展：列表的嵌套取值
3、获取元素个数  -- len() ==长度
4、list的元素是可以被改变的
增加：
append： 追加元素到末尾 --最常用的一种方法
insert：指定位置进行元素的插入
extend：一个列表的元素全部扩展到列表 = 列表合并 ==同时添加多个元素 ==扩展
删除
pop:默认删除最后一个元素，可以指定位置删除元素
remove：删除元素本身
clear: 清空列表
修改： 先取值 再赋值
5、列表的元素可以重复的 --- 多个 统计个数  --count
"""
# 创建列表  -- 空列表
list1 = [20,3.14,False,"喜君",[1,2,2,3,4]]
#增加
list1.append("可口")
list1.insert(3,"沐槿")
list1.extend(["晨雾","繁星","晚熟"])
# 删除
print(list1)
list1.pop(5)  # --更多
list1.remove(3.14)
# list1.clear()
# 修改
list1[0] = "倾卿"
list1[1] = "倾卿"
list1.append("倾卿")
print(list1)
print(list1.count("倾卿"))

# num = input("请输入一个数字：")  # 内置函数： 获取控制台输入内容
# print("你输入的数字是：{}".format(num))  # 格式化输出

