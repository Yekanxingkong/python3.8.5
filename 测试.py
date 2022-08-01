import os,sys
try:
    import platform
    import pymysql
    import pymssql
    import pyodbc
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

getcwd = os.getcwd() + "\\"
list = os.listdir(getcwd)
a = os.walk(getcwd)
for x,n,m in a:
    for j in m:
        print(os.path.join(x,j))
print("------------------------------------")
g = os.walk('C:\\Users\\Administrator\\Desktop\\python3.8.5')
for path,dir_list,file_list in g:
    for dir_name in dir_list:
        pass
        #print(os.path.join(path, dir_name) )
def at():
    for loopA in list:
        print('检查文件的类型，是否为文件夹')
        print('检查文件的大小属性')
        print('读取视频文件，保存信息')
    print(list)
    print(os.path.split( os.path.realpath( sys.argv[0] ) )[0])

def iffile(path):
    if os.path.isdir(path):
        print("it's a directory")
    elif os.path.isfile(path):
        print("it's a normal file")
    else:
        print("it's a special file(socket,FIFO,device file)")


if __name__ == '__main__':
    sys = platform.system()
    if sys == "Windows":
        print("OS is Windows!!!")
    elif sys == "Linux":
        print("OS is Linux!!!")
    else:
        print("非Windows和Linux的系统暂不支持，程序退出！")
        sys.exit(0)