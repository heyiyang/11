#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/6/16 21:55 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

'''
UI 自动化： selenium库
代码   -------翻译（浏览器驱动-driver）---   浏览器
            chromedriver.exe  ====  1、下载  2、 解压--exe  3、复制到Python安装目录
Python/java
selenium-webdriver驱动 --->发送指令（打开浏览器，网页）  ----> 浏览器驱动接受  --->驱动浏览器执行对应的操作
                                        <----                <----
UI自动化发送指令和操作过程：
1、启动chromedriver之后，启动了一个服务：IP端口 监听
2、python的webdriver--chromedriver建立连接 （http协议）
3、Chromedriver收到webdriver 指令之后，驱动浏览器执行操作
4、Chromedriver把结果  返回给webdriver
5、继续发送后续的指令...

selenium工具包，包括三个部分：---了解
1、ide --录制脚本
2、webdriver：库--提供了对网页操作的各种方法（点击，输入等操作）= 各种语言版本，结合语言来使用
3、grid：分布式--多个浏览器执行并发
人    ------   浏览器
'''
from selenium import webdriver # 从selenium工具包里导入webdriver库
import time
driver = webdriver.Chrome()   # webdriver 与chrome建立会话  ==赋值变量
'''
对浏览器的常用的操作：
1、打开某个网页
2、最大化窗口
3、页面回退  前进  刷新
4、关掉：
quit（）: 关闭整个浏览器，Chromedriver 服务关闭
close()：关闭当前窗口
'''
# driver.get("https://baidu.com")   # 打开URL地址网页
# driver.maximize_window()
# time.sleep(2)
# driver.get("https:taobao.com")
# time.sleep(2)
# driver.back()  # 回退操作
# time.sleep(2)
# driver.forward()  # 页面前进
# time.sleep(2)
# driver.refresh()   # 页面刷新
# driver.close()   # 关闭
'''
web 页面三个部分：
1、HTML：页面呈现的内容--  标签语言 --- 每一种元素不同的标签
2、CSS：页面布局，字体颜色，字体大小
3、JavaScript：-js-- 控制页面

元素 = 标签+ 属性（id,name,class,type...）
id -- 开发遵循语法规定，id设置唯一的；== 标准唯一
name -- 唯一

元素定位方法：八大元素定位==  id， name， xpath  === 代码驱动操作
元素四大操作：
1、点击--click
2、输入--send_keys

xpath : 用的最多一种元素定位方法：
绝对路径：/html/body/div[1]/aside/div/section/div[1]/div[2]/p  == 不能推荐方法
--从根开始，以/开头，逐级位置，继承关系---极易发生变化，大概率导致元素找不到 
相对路径：//*[@id="username"]  
-- 以// 开头，某个标签+属性 == 相对稳定很多 --推荐使用
# 层级
//div[@class="login-logo"]//b
# 文本 -- 文本唯一且固定
//b[text()="柠檬ERP"]
# 包含
//b[contains(text(),"柠檬")]
'''
driver.get("http://erp.lemfix.com/login.html")   # 打开URL地址网页
driver.maximize_window()
driver.find_element_by_name("username").send_keys("test123")  # 代码找到元素,进行输入内容的操作
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
driver.find_element_by_id("btnSubmit").click()  # 通过id找到按钮，进行点击操作










