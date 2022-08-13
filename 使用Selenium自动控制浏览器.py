# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:29:21 2021

@author: Administrator
"""

使用Selenium自动控制浏览器

设置Selenium

默认情况下，在执行Selenium指令时，程序会打开一个新标签页，并完成指定的任务。
=============================================================================
from selenium import webdriver
#调取webdriver模块
web = webdriver.Chrome()
#打开Chrome浏览器
=============================================================================




不过，也可以设置Selenium至静默模式。在该模式下，浏览器不会弹出显示，而是将程序所返回的结果直接显示在终端。
=============================================================================
from selenium import webdriver 
#调用webdriver模块
from selenium.webdriver.chrome.options import Options 
#调用Options类
option = Options() 
#实例化Option
option.add_argument('--headless') 
#设置静默模式
web = webdriver.Chrome(options = chrome_options)
#后台打开Chrome浏览器
=============================================================================





控制浏览器

控制浏览器时比较常用的操作包括：send_key()，click()，以及clear()。其中，send_key()可以实现输入信息功能；click()可以实现鼠标单击功能；clear()可以实现清空内容功能。
=============================================================================
#示例：

from selenium import webdriver
web = webdriver.Chrome()

web.get('https://www.example.com/')
#打开指定网页
tag = web.find_element_by_tag_name('tag_0')
#通过find_element_by_tag_name提取出名为tag_0的元素
tag.send_key('测试')
#在tag元素处输入文字“测试”
button = web.find_element_by_id('submit')
#通过find_element_by_id提取出id为submit的元素
button.click()
#单击button按钮
links = web.find_element_by_link_text('链接')
#通过find_element_by_link_text提取出文本所对应的超链接
for link in links:
    print(link)
    #遍历提取出链接信息

web.close()
#关闭网页
=============================================================================


注：每次调用webdriver打开一个网页后，都需要使用close()语句关闭它。