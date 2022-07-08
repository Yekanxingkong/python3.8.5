# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 12:43:30 2021

@author: Administrator
"""

import os

# 获取当前运行的文件路径
print(__file__)

# 获取 文件目录、文件名【带后缀】
print(os.path.split(__file__)[0])
print(os.path.split(__file__)[1])

# 先获取文件名【带后缀】，再获取文件名【不带后缀】、文件后缀
print(os.path.splitext(os.path.basename(__file__))[0])
print(os.path.splitext(os.path.basename(__file__))[1])

一、时间日期基本介绍

时间日期类型在Python中主要有两个模块：time模块和datetime模块

time模块:是基于Unix Timestamp（时间戳）实现的，所能表述的范围被限定在1970-2038年之间；

时间戳：是指格林尼治时间1970年01月01日00时00分00秒起至现在的总秒数，结果是一个浮点数。

二、时间日期类型--time模块

1. 获取当前时间戳

print(time.time())

示例：获取一个程序执行了多少秒

import time
start_time = time.time()
sum = 0
for i in range(1000000):
    sum += i
end_time = time.time()
print("程序执行了%f秒"%(end_time - start_time))

输出结果：

程序执行了0.128733秒

2. 将时间戳转化为标准时间日期格式

通过时间元组进行转换，使用time.localtime(时间戳)把获取的时间戳转为当地的时间元组，使用time.gmtime(时间戳)把获取的时间戳转为格林尼治时间元组；如果不加参数，默认为当前时间戳。

import time
time_tuple = time.localtime(time.time())
print("当前时间为{}年{}月{}日{}点{}分{}秒".format(time_tuple[0],time_tuple[1],time_tuple[2],time_tuple[3],time_tuple[4],time_tuple[5]))

3. 格式化时间

（1）以(RPC)标准时间格式输出时间

time.asctime(time.localtime())  # 参数为时间元组
time.ctime(time.time())  # 参数为浮点数时间戳

输出结果：Thu Jun 25 10:31:48 2020

（2）以time.strftime()格式化时间

# 格式化成2020-06-25 11:18:29形式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 格式化成Thu Jun 25 11:18:29 2020形式
print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))

注意：strftime语句中时间格式化符号中是不能包含中文的，如果想输出中文，还是通过上面%语句输出或者format格式输出。

三、time模块案例演示

示例：2008年8月8日，20:08:08往后88,888,888秒是哪天？星期几？

import time
# time.mktime()方法可以把时间元组转为时间戳
tuple01 = (2008,8,8,20,8,8,0,0,0)
# 待求时间戳
time01 = time.mktime(tuple01) + 88888888
# 待求时间元组
tuple02 = time.localtime(time01)
# 打印结果
print("结果:",time.strftime("%Y-%m-%d %H:%M:%S",tuple02),end="\t")
tuple_week = ("星期一","星期二","星期三","星期四","星期五","星期六","星期天")
print(tuple_week[tuple02[6]])

输出结果：

结果: 2011-06-03 15:29:36 星期五

四、datetime模块基本使用

1. date类

获取今天的日期

date01 = datetime.date.today()

返回的结果是2020-06-26 可以对年、月、日各个属性单独访问：

print("年份",date01.year)
print("月份",date01.month)
print("日期",date01.day)

2. time类

time类可以直接定义当前的时间，精确到微秒
time01 = datetime.time(8,23,2,121212)
可以对时、分、秒、微秒各个属性单独访问：
print("时",time01.hour)
print("分",time01.minute)
print("秒",time01.second)
print("微秒",time01.microsecond)

3. datetime类

获取日期和时间（年份、月份、日期、时 分、秒、微秒、时区）
datetime01 = datetime.datetime.now()

五、datetime基本使用

1. 获取当前时间

from datetime import datetime
print(datetime.now())   # 获取当前日期时间
print(datetime.today()) # 获取当前时间
print(datetime.utcnow())    # 获取当前的格林尼治时间

输出结果：

2020-06-26 16:35:43.928699
2020-06-26 16:35:43.928732
2020-06-26 08:35:43.928741

2. 获取当前日期时间的日期和时间

from datetime import datetime
dt01 = datetime.today()
print(dt01.date())
print(dt01.time())

输出结果：

2020-06-26
16:35:43.929583

获取日期时间的年、月、日、时、分、秒、微秒

from datetime import datetime
dt01 = datetime.today()
print(dt01.year)
print(dt01.month)
print(dt01.day)
print(dt01.hour)
print(dt01.minute)
print(dt01.second)
print(dt01.microsecond)

输出结果：

2020
6
26
16
35
43
929583