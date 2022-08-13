import os,sys
try:
    import platform
    import pymysql
    import pymssql
    import pyodbc
    import mysql.connector
    import os
    import re
    import requests
    import requests_cache
    import requests_html
    import configparser
    import tkinter.messagebox
    import time
    import struct
    import mysql.connector
    import bs4
    import shutil
    import smb.SMBConnection
    import json
    import datetime
    import psutil
    import random, string
    from urllib.parse import unquote, urlencode, quote
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from lxml import etree
    from browsermobproxy import Server
except:
    libs = {'requests', \
            'beautifulsoup4'}
    for lib in libs:
        # 阿里云：http://mirrors.aliyun.com/pypi/simple/
        cmd = os.system('E:\python3.8.5\Scripts\pip.exe install -i https://pypi.tuna.tsinghua.edu.cn/simple ' + lib)
        #返回0表示成功，1则失败
        # os.system乱码的情况，在设置-编辑器-文件编码-设置全局UTF-8，两个编辑模式为GBK
        if(cmd == 1):
            print("PIP失效，请检查Python环境。\n未配置环境，程序无法运行")
            sys.exit(0)
        else:
            print("已使用PIP安装了所需的环境。")
    BeautifulSoup = bs4.BeautifulSoup()
    ConfigParser = configparser.ConfigParser()
    messagebox = tkinter.messagebox

#-------------------------------创建数据库------------------------------------------
def New_db(hosturl,youruesnames,yourpassword,SQLname):
    mydb = mysql.connector.connect(
        host=hosturl,
        user=youruesnames,
        passwd=yourpassword,
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    new_db_SQLname = False
    for (x,) in mycursor:
        if(x == SQLname):
            new_db_SQLname = True
        else:
            pass
    if(new_db_SQLname == False):
        mycursor.execute("CREATE DATABASE " + SQLname)
        return 1
    else:
        return 0
#-------------------------------创建数据库------------------------------------------
#-------------------------------删除数据库------------------------------------------
def Del_db(hosturl,youruesnames,yourpassword,SQLname):
    mydb = mysql.connector.connect(
        host=hosturl,
        user=youruesnames,
        passwd=yourpassword,
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    del_db_SQLname = False
    for (x,) in mycursor:
        if(x == SQLname):
            del_db_SQLname = True
        else:
            pass
    if(new_db_SQLname == True):
        mycursor.execute("DROP DATABASE " + SQLname)
        return 1
    else:
        return 0
#-------------------------------删除数据库------------------------------------------
#-------------------------------创建数据表------------------------------------------
def New_execute(hosturl,youruesnames,yourpassword,SQLname,customers,Sqlcommand):
    mydb = mysql.connector.connect(
        host=hosturl,
        user=youruesnames,
        passwd=yourpassword,
        database=SQLname
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    cus_tile = False
    for (x,) in mycursor:
        if (x == customers):
            cus_tile = True
        else:
            pass
    if (cus_tile == True):
        mycursor.execute("CREATE TABLE " + customers + " (" + Sqlcommand + ")")
        return 1
    else:
        return 0

#-------------------------------创建数据表------------------------------------------
#customers = 表名称
#Sqlcommand = "列名称1 INTEGER(50),列名称2 VARCHAR(255)"
#Mysql的插入语句，注意数据类型
#sql表创建的时候，必须携带列的类型，无法创建完全空表！！！！！！


def INTO_execute(hosturl,youruesnames,yourpassword,SQLname,customers,Sqlcommand):
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		database=SQLname
	)
	mycursor = mydb.cursor()
	mycursor.execute(Sqlcommand)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

def into_cdk():
    num = string.ascii_letters + string.digits
    cdk = "HKTB" + "".join(random.sample(num, 32))
    return cdk




def main(cdk):
    try:
        hosturl,youruesnames,yourpassword,sqlname,customers = "192.168.2.175","root","123456","数据库名称","表名称"
        if(New_db(hosturl,youruesnames,yourpassword,SQLname) == 1):
            print("已创建数据库：" + SQLname)
        else:
            pass
        Sqlcommand = "序号 INTEGER(50),PUBG_CKD VARCHAR(255),状态 VARCHAR(255)"
        if(New_execute(hosturl,youruesnames,yourpassword,SQLname,customers,Sqlcommand) == 1):
            print("已创建数据表：" + customers)
        else:
            Sqlcommand = ""
    except:
        print("Database connection failed, please check the server!!!")
        sys.exit(0)
    #for loopA in range(100):
    #   Sqlcommand = "INSERT INTO " + customers + " (序号,PUBG_CKD,状态) VALUES ('"+ loopA +"','"+ cdk +"','Ture')"
    #   mydb.commit()


    #查询数据
    mydb = mysql.connector.connect(
        host=hosturl,
        user=youruesnames,
        passwd=yourpassword,
        database=SQLname
    )
    mycursor = mydb.cursor()
    Sqlcommand = "SELECT PUBG_CKD FROM " + customers
    mycursor.execute(Sqlcommand)
    for (x,) in mycursor:
        if(x == cdk):
            sql_revise = "UPDATE Person SET 状态 = 'Flase' WHERE PUBG_CKD = '"+ cdk +"' "
            mycursor.execute(sql_revise)
            mydb.commit()
            return 1
        else:
            pass
    return 0




if __name__ == '__main__':
    sys = platform.system()
    if sys == "Windows":
        print("OS is Windows!!!")
        for loopA in range(10):
            print(into_cdk())
    elif sys == "Linux":
        print("OS is Linux!!!")
    else:
        print("非Windows和Linux的系统暂不支持，程序退出！")
        sys.exit(0)