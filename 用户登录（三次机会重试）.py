=============================================================================
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:02:54 2021

@author: Administrator
"""

# -*- coding:utf-8 -*-
  
#先设定初始用户名和登录密码
init_usrname=input('Please enter initial username:')
init_password=input('Please enter initial password:')
#打印输出设置好的用户名和初始登录密码
print (init_usrname)
print (init_password)
  
#进入登录见面，flag0指的是输入密码的错误次数
#flag1指的是登录成功标志位
flag0=0
flag1=0
print('>>>User Login<<<')
  
while True:
#提示用户输入用户名
    usr=input('enter username:')
    if usr==init_usrname:
    #输入用户名正确则进入到输入登录密码阶段
        #判断输错登录密码次数
        while flag0<3:
            password=input('enter password:')
            if password==init_password:
            #若密码输入正确则登录成功因而跳出循环
                print('Success Login!')
                flag1=1
                break
            else:
            #计算输错次数，每输错一次flag加一
                flag0 +=1
                if flag0<=2:
                    print('Wrong Password,enter again!')
    #输错三次跳出输入登录密码环节重新进行用户名的输入，相应地flag也要归零
        if flag1==1:
              break
        flag0=0
        print ('You have tried three times,login again!')
    else:
        print ('Wrong Username,enter again!')
        
        
=============================================================================
        
n = 1
user = '123'
pwd = '456'
while   n < 4 :
 
    n1 = input("请输入用户名： ")
    n2 = input("请输入密码：   ")
 
    if  user == n1 and pwd == n2 :
        print("登录成功")
        break
 
    else:
        print("用户名或者密码错误")
        n = n + 1
        if n == 4:
 
            print("登录次数超过3次，登录失败")