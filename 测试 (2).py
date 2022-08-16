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
hosturl,youruesnames,yourpassword,SQLname,customers = "192.168.2.175","root","123456","CDK","PUBGcdk"
mydb = mysql.connector.connect(
    host=hosturl,
    user=youruesnames,
    passwd=yourpassword,
    database=SQLname
)
mycursor = mydb.cursor()
Sqlcommand = "SELECT 状态 FROM " + customers
Sqlcommand = "SELECT 状态 FROM " + customers + " WHERE PUBG_CKD='HKTBIXSfGNTuUHvjBmPC2we8ic6R3EAxkaKM'"
mycursor.execute(Sqlcommand)
for (x,) in mycursor:
    print(x)



