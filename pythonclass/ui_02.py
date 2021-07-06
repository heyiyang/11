#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/6/21 18:51
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
from selenium import webdriver # 从selenium工具包里导入webdriver库
import time
driver = webdriver.Chrome()   # webdriver 与chrome建立会话  ==赋值变量
driver.implicitly_wait(10)  # 隐式等待 --设置10s
driver.get("http://erp.lemfix.com/login.html")   # 打开URL地址网页
driver.maximize_window()

# 第二条用例： 获取页面的标题
title = driver.title  # 页面有标题  赋值
if title == "柠檬ERP":
    print("这个页面的标题是：{}".format(title))
else:
    print("这条测试不通过！")

# 第三条用例： 登录操作
driver.find_element_by_name("username").send_keys("test123")  # 代码找到元素,进行输入内容的操作
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
driver.find_element_by_id("btnSubmit").click()  # 通过id找到按钮，进行点击操作

"""
1、八大元素定位
2、四大元素操作
3、三大等待
4、字节： iframe切换

元素四大操作：
1、点击--click
2、输入--send_keys
3、获取文本  -- text
4、获取属性 -- id name class ...

使用场景：进行点击操作之后，当有页面变化的时候，为了避免没有加载出来。点击之后加一个等待
三大等待：
1、强制等待：time.sleep（2）
缺点：就算元素已经出来了，也还是要等待 == 不太灵活  --浪费时间
2、智能等待：等到火元素出现/存在
1）隐式等待：一般一个会话只执行一次。设置等待时间（10s）；只要元素出现/被找到了（2s），就会继续往下执行；
 如果这个一直没有出现，最多等待10s，报错！
2）显式等待： -- 面试 ？？

"""
# 第四条：判断是否登录成功
# time.sleep(5)  # 强制等待 5s
usemname = driver.find_element_by_xpath("//p").text   # 获取这个元素文本信息
if usemname == "测试用户":
    print("登录成功且用户名是：{}".format(usemname))
else:
    print("这条测试不通过!")

# 第五条： 点击零售出库
driver.find_element_by_xpath("//div[@id='leftMenu']//span[text()='零售出库']").click()

# 第六条：搜索编号，检查结果
'''
1、找到输入框 ===  done
2、输入搜索编号  ==done
3、点击查询按钮  == done
4、检查结果是否正确  == done

页面里有子页面的嵌套（俄罗斯套娃），先找到这个子页面，切换到这个子页面，在子页面里进行 元素！
1）怎么判断在子页面？
-- 查看元素的标签路径，只要路径存在iframe --  存在子页面！
2）怎么切换到子页面呢？
1、通过id进行切换  ==driver.switch_to.frame(id_iframe)  ==id
注意：id可以唯一，但是如果是变化的，就不能用来做为元素定位！！  ==优先
2、通过webelement 进行切换 ==  driver.switch_to.frame（元素定位的表达式)
==//iframe[@id="tabpanel-d10e6b3757-frame"]
'''
id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")   # 获取id属性
id_iframe = id + "-frame"   # 通过字符出阿奴的拼接 得到iframe id
# 通过id进行iframe切换
# driver.switch_to.frame(id_iframe)  # 通过id（name）来进行iframe切换
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_iframe)))
# 通过webelement 来进行iframe切换
driver.find_element_by_id("searchNumber").send_keys("448")
driver.find_element_by_id("searchBtn").click()  # 点击查询按钮
time.sleep(1)  # 隐式等待+强制等待

# 获取编号文本
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
if "448" in num:
    print("搜索成功！")
else:
    print("搜索失败！")