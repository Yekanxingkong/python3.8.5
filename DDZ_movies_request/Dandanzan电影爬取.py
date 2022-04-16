import pymysql
import pymssql
import pyodbc
import os
import sys
import re
import requests
import requests_cache
import requests_html
import configparser
import tkinter.messagebox
import time
from urllib.parse import unquote,urlencode,quote
import struct
import mysql.connector
import bs4
import shutil
import smb.SMBConnection
import json
import datetime
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
from browsermobproxy import Server
BeautifulSoup = bs4.BeautifulSoup()
ConfigParser = configparser.ConfigParser()
messagebox = tkinter.messagebox
hosturl,youruesnames,yourpassword,sqlname,customers = "192.168.2.175","root","123456","My_Movies","My_Movies_001"
sqlini = "\\" + "Dandanzan电影数据库.txt"
thisini = "/Dandanzan_movies.ini"
# 需要确定好SQL数据库的位置和数据库名称、配置文件。
# 数据库配置文件，存放表的列名称和数据
# 配置文件存放程序所运行的数据
# url = 网址 ，passmath = 网页数据，
# having = 程序运行的次数
# reading = 是否决定写入数据库
# cofig = 报错的信息
# 判断并数据库是否存在，不存在则创建数据库
try:
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		charset="utf8"
	)
except:
	debug = hosturl + "数据库未能连接，10秒后重试。"
	sys.exit()
mycursor = mydb.cursor()
sqlcommand = "SHOW DATABASES"
mycursor.execute(sqlcommand)
# 第一次运行，如果没有数据是不运行for循环
debug = "this is not find"
for (x,) in mycursor:
	if(x == sqlname):
		debug = "find now"
		break
	else:
		debug = "this is not find"
if(debug == "this is not find"):
	mycursor.execute("CREATE DATABASE " + sqlname)
	mycursor.execute("ALTER DATABASE "+sqlname+" DEFAULT CHARACTER SET utf8")
mydb.close()
try:
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		database=sqlname,
		charset="utf8"
	)
except:
	debug = sql + "数据库连接错误，关闭程序重新启动。"
	sys.exit()
# 连接数据库，判断表是否存在。不存在则创建一个表
mycursor = mydb.cursor()
sqlcommand = "SHOW TABLES"
mycursor.execute(sqlcommand)
debug = "this is first start"
sqlmount = []
for (x,) in mycursor:
	sqlmount.append(x)
	if(x == customers):
		debug = "find now"
		break
	else:
		debug = "this is not find"
if(debug == "this is first start" or debug == "this is not find"):
	try:
		f2 = open(os.getcwd() + sqlini, "r", encoding='UTF-8')
	except:
		debug = "未能找到目录，请确认配置文件是否在同一目录之下"
		sys.exit()
	lines = f2.readlines()
	a = 0
	val = ""
	for i in lines:
		i = repr(i)
		math = i.find("\\n")
		if (i.find("\\n") != -1):
			i = i[0:i.find("\\n")]
		val = val + i + ","
	val = val[0:len(val) - 1]
	val = val.replace("'", '')
	val = val.strip("'")
	f2.close()
	sqlcommand = val
	mycursor.execute("CREATE TABLE " + customers + " (" + sqlcommand + ")")
# ---------------------------------------用于调试数据表的创建-------------------------------------
# sqlcommand = "SHOW TABLES"
# mycursor.execute(sqlcommand)
# for (x,) in mycursor:
# 	debug = x
# ---------------------------------------用于调试数据表的创建-------------------------------------

#检验是否全是中文字符
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True
#判断字符串是否包含中文
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False
#清理特殊符号转成空格
def is_del_sign(a):
	c = ""
	d = ""
	b = []
	for i in range(len(a)):
		if(is_all_chinese(a[i]) == False and a[i].isdigit() == False and a[i].isalpha() == False):
			if(a[i] == "：" or a[i] == "." or a[i] == " "):
				b.append(a[i])
			else:
				b.append(" ")
		else:
			b.append(a[i])
	for i in b:
		c = c + i
	return c
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass

	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass

	return False
# 判断是否是日期。 是返回日期，否则返回假
def is_years(list):
	# 进行字符长度判断是否为日期
	a = len(list)
	m = ""
	if(a == 4):
		debug = "len :" + str(a)
	else:
		for i in range(a):
			if is_number(list[i]) == True:
				m = m + "T"
			else:
				m = m + "F"
		n = m.find("TTTT")
		if n != -1:
			x = list[n:n+4]
			list = x
			m = ""
		else:
			return False
	a = len(list)
	for i in range(a):
		if is_number(list[i]) == True:
			m = m + "T"
		else:
			m = m + "F"
	if m.count("T") == 4:
		i = datetime.datetime.today().year
		for loopB in range(1900, i):
			if (str(loopB) == list):
				return list
			else:
				pass
	return False
def requests_network_hyperlink(url):
	def killjava():
		# 程序结束必须调用结束java进程
		pids = psutil.pids()
		for pid in pids:
			p = psutil.Process(pid)
			debug = 'pid-%s,pname-%s' % (pid, p.name())
			if 'java.exe' in p.name():
				cmd = 'taskkill /f /im java.exe'
				os.system(cmd)
	server = Server(r'E:\python3.8.5\Lib\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
	# 二进制路径，必须下载放置，否则报错
	server.start()
	proxy = server.create_proxy()
	debug = 'proxy' + proxy.proxy
	chrome_options = Options()
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
	# 需要下载一个谷歌的对应版本，否则会报错
	chrome_options.add_argument('--headless')
	# 是否显示窗口
	browser = webdriver.Chrome(options=chrome_options)
	proxy.new_har(options={
			'captureContent': True,
			'captureHeaders': True
		})
	try:
		browser.get(url)
	except:
		killjava()
		proxy.close()
		server.stop()
		browser.quit()
		requests_network_hyperlink(url)
	time.sleep(2)
	json_data = proxy.har
	links = []
	for entry in json_data['log']['entries']:
		# 根据URL找到数据接口
		entry_url = entry['request']['url']
		# 获取接口返回内容
		links.append(entry_url)
	proxy.close()
	server.stop()
	browser.quit()
	killjava()
	return links
def requests_status_code(res):
	if(res == 200):
		debug = "服务器连接正常，响应：" + str(res)
		return True
	elif(res == 404):
		debug = "服务器未找到资源，响应：" + str(res)
		return  False
	elif(res == 501):
		debug = "服务器内部错误，无法完成请求，响应：" + str(res)
		return False
	else:
		debug = "遇到其它错误，响应：" + str(res)
		return False
	debug = "响应超范围，请联系管理员修复，错误代码：07"
	messagebox.showinfo("python提示", "响应超范围，请联系管理员修复，错误代码：07")
	return debug

def db_reading(sqlcontent):
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		database=sqlname
	)
	mycursor = mydb.cursor()
	sqlcommand = "SELECT max(编号（ID）) FROM " + customers
	mycursor.execute(sqlcommand)
	for (x,) in mycursor:
		math = x
	if str(math) == "None":
		math = 0
	else:
		math = int(math) + 1
	sqlcontent = "'" + str(math) + "'," + sqlcontent
	sqlcommand = "INSERT INTO " + customers + " VALUES (" + sqlcontent + ")"
	mycursor.execute(sqlcommand)
	mydb.commit()
	print("a reading sql :" + sqlcontent)
	return True

def __main__(v1,v2,v3,v4,v5):
	# 第一部分对中文名称的判断，
	def chinese(v1):
		for loopA in sqlmount:
			mydb = mysql.connector.connect(
				host=hosturl,
				user=youruesnames,
				passwd=yourpassword,
				database=sqlname
			)
			mycursor = mydb.cursor()
			sqlcommand = "SELECT 电影中文名字（ChineseName） FROM " + loopA
			mycursor.execute(sqlcommand)
			for (i,) in mycursor:
				if i == v1:
					debug = "find repeat name"
					return False
				else:
					pass
			mydb.close()
		return True
	# 第二部分对原名的判断
	def formerly(v1, v2):
		if v2 == "" or v1 == v2 or v2 == " ":
			v2 == "None"
	if chinese(v1) == False:
		return False
	else:
		return v1,v2,v3,v4,v5
def __int__(funcatalog):
	try:
		if not os.path.exists(funcatalog):
			raise FileNotFoundError("文件不存在")
	except:
		messagebox.showinfo("python提示", "funcatalog not ini ,but we can create new ini")
		# 创建提示框
		a = open(funcatalog, "w+", encoding='UTF-8')
		lines = ""
		v = ["[ini]", "passmath = 0", "having = 0", "reading = 1","cofig = "]
		for i in v:
			lines = lines + i + "\n"
		a.write(lines)
		a.close()
		del a,v
	conn = ConfigParser
	reading = conn.read(funcatalog)
	passmath = conn.get('ini', 'passmath')
	having = conn.get('ini', 'having')
	number = int(passmath)
	del conn, reading
	return number

#以空格为分割方式，清除特殊字符,返回中文名称和原名
def DDZ_Movies_Name(list):
	a = list.count(" ")
	if(a > 0 ):
		# 到底有多少空格
		if a == 1:
			x = list.split(' ')
			for i in range(0,2):
				x[i] = x[i].replace('"', "'")
			return x[0], x[1]
		else:
			x = list.find(' ')
			list.replace('"', "'")
			return list[0:x], list[x + 1:len(list)]
	else:
		return False
# 判断链接是否是m3u8
def DDZ_hyperlink(a):
	l = a.find("https://b.baobuzz.com/m3u8/")
	x = a.find(".m3u8?sign=")
	z = a.find(".m3u8")
	if ( z == -1 and x == -1 and l == -1):
		return  False
	else:
		return True
# 控制网络访问，爬取网页的东西
def DDZ_movies_requests(url):
	proxies = {'http': None,
			   'https': None
			   }
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
		"sec-ch-ua-platform": "Windows",
		"Connection": "keep-alive",
		"Accept-Language": "zh-CN,zh;q=0.8"
	}
	try:
		reshtml = requests.get(url, headers=headers, proxies=proxies, timeout=8)
	except:
		debug = "reshtml ，错误代码：07 "
		return False
	if (requests_status_code(reshtml.status_code) == False):
			debug = "Not find url :" + url + "Show wrong :" + str(reshtml.status_code)
	reshtml.encoding = 'utf-8'
	tree = etree.HTML(reshtml.text)
	if (tree == ""):
		debug = "未能获取到网页代码"
		return False
	else:
		try:
			items = tree.xpath("//div/header/h1[@class='product-title']/text()")
		except:
			debug = "程序报错：重新运行"
			return False
		#修改爬取信息
	if (len(items) != 0):
		try:
			year = tree.xpath("//div/header/h1[@class='product-title']/span[1]/text()")
			pic = tree.xpath("//div/header//img[@class='thumb']/@src")
		except:
			debug = 1
			return False
		return items[0],year[0],pic[0]
	else:
		return False
# 控制程序运行
def DDZ_movies():
	int = os.getcwd() + thisini
	number = __int__(int)
	ler = str(number)
	ler = ler.rjust(5, '0')
	url = "https://www.dandanzan10.top/dianying/" + ler + ".html"
	time.sleep(1)
	if(DDZ_movies_requests(url) == False):
		debug = "该网页未能够提供信息"
	else:
		list,year,pic = DDZ_movies_requests(url)
		links = requests_network_hyperlink(url)
		for i in links:
			if DDZ_hyperlink(i) == True:
				link = i
				break
			else:
				link = "None"
		if link == "None":
			conn = ConfigParser
			reading = conn.read(int)
			conn.set("ini", "cofig", url)
			with open(int, "w+") as f:
				conn.write(f)
		if DDZ_Movies_Name(list) == False:
			debug = "名称中空格小于0，没有空格"
		else:
			chinese,orig = DDZ_Movies_Name(list)
			newyear = is_years(year)
			if newyear == False :
				conn = ConfigParser
				reading = conn.read(int)
				conn.set("ini", "cofig", str(number) + chinese + orig + year)
				with open(int, "w+") as f:
					conn.write(f)
			else:
				year = newyear
			conn = ConfigParser
			reading = conn.read(int)
			red = conn.get('ini', 'reading')
			a = __main__(chinese, orig, year, pic, link)
			if a != True and a != False:
				chinese, orig, year, pic, link = a[0],a[1],a[2],a[3],a[4]
				a = True
			else:
				pass
			if red == str(0) and a == True:
				sqlcontent = '"' + chinese + '",' + '"' + orig + '",' + "'" + year+ "'," + "'" + pic + "'" + ",'" + link + "'"
				db_reading(sqlcontent)
			else:
				print(chinese, orig, year, pic, link)
			del conn, reading
	if number == 99999:
		conn = ConfigParser
		reading = conn.read(int)
		having = conn.get('ini', 'having')
		having = int(having) + 1
		conn.set("ini", "having", str(having))
		with open(int, "w+") as f:
			conn.write(f)
		number = 0
	else:
		number = number + 1
	conn = ConfigParser
	reading = conn.read(int)
	conn.set("ini", "passmath", str(number))
	with open(int, "w+") as f:
		conn.write(f)
	DDZ_movies()
DDZ_movies()
# 	找不到，运行完毕，需要运行ini配置文件+1，更换网页继续爬取