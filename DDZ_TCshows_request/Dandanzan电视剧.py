import pymssql
import pyodbc
import os
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
from lxml import etree
BeautifulSoup = bs4.BeautifulSoup()
ConfigParser = configparser.ConfigParser()
messagebox = tkinter.messagebox
#-------------------------------创建数据表------------------------------------------
def New_execute(hosturl,youruesnames,yourpassword,SQLname,customers,Sqlcommand):
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		database=SQLname
	)
	mycursor = mydb.cursor()
	mycursor.execute("CREATE TABLE " + customers + " (" + Sqlcommand + ")")
	#Sqlcommand = "编号ID INTEGER(50),分辨率Resolution VARCHAR(255),命名Name VARCHAR(50)"
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)
#-------------------------------创建数据表------------------------------------------
#-------------------------------创建数据表的命令------------------------------------------
def IntenSQL():
	hosturl = "localhost"
	youruesnames = "root"
	yourpassword = "123456"
	SQLname = "My_TVshows"
	customers = "Now_TVshows_001"
	f2 = open("C:/Users/Administrator/Desktop/1.txt", "r", encoding='UTF-8')
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
	Sqlcontent = val
	Sqlcommand = Sqlcontent
	New_execute(hosturl, youruesnames, yourpassword, SQLname, customers, Sqlcommand)
	#-------------------------------查询命令---------------------------------------
	Sqlcommand = "SELECT * FROM " + customers
	Select_cursor(hosturl, youruesnames, yourpassword, SQLname,Sqlcommand)
#-------------------------------创建数据表的命令------------------------------------------
#-------------------------------查询数据库下的数据表------------------------------------------
def Select_db(hosturl,youruesnames,yourpassword,SQLname):
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		database=SQLname
	)
	mycursor = mydb.cursor()
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)
#-------------------------------查询数据库下的数据表------------------------------------------
#-------------------------------查询数据表下的数据------------------------------------------
def Select_cursor(hosturl,youruesnames,yourpassword,SQLname,Sqlcommand):
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		database=SQLname
	)
	mycursor = mydb.cursor()
	mycursor.execute(Sqlcommand)
	cursor = mycursor.description
	a,b = [],[]
	for x in cursor:
		print(x)
		a.append(x)
	for x in mycursor:
		print(x)
		b.append(x)

	return a,b
#-------------------------------查询数据表下的数据------------------------------------------
# Sqlcommand = "SELECT * FROM " + customers
# Select_cursor(hosturl,youruesnames,yourpassword,SQLname,Sqlcommand)




# ------------------------------------------------------前置初始化结束，正本程序--------------------------------------
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
#中英文的筛选
def notebook(a,year):
	a = a.replace('”', "")
	a = a.replace('“', "")
	a = a.replace('"', "")
	a = a.strip('"')
	f = ""
	c = ""
	d = ""
	for i in range(len(a)):
		b = is_all_chinese(a[i]),a[i].isdigit(),a[i].isalpha()
		if(is_all_chinese(a[i]) == True):
			c = c + "T"
		else:
			c = c + "F"
		if(a[i].isdigit() == True):
			d = d + "T"
		else:
			d = d + "F"
		if(a[i].isalpha() == True):
			f = f + "T"
		else:
			f = f + "F"
	m = c.rfind("T")
	if d[m+1] == "F":
		z = a[0:m + 1]
		z = z.strip()
		x = a[m+1:len(a)]
		x = x.strip()
		x = x.replace('"', "")
	else:
		n = d.find("F",m + 1)
		z = a[0:n + 1]
		z = z.strip()
		x = a[n + 1:len(a)]
		x = x.strip()
		x = x.replace('"', "")
	if(year.isdigit() == False):
		k = ""
		for i in range(len(year)):
			if year[i].isdigit() == True:
				k = k + year[i]
	return z,x,k



def INTO_execute(hosturl,youruesnames,yourpassword,SQLname,customers,Sqlcommand):
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		database=SQLname
	)
	mycursor = mydb.cursor()
	mycursor.execute(Sqlcommand)
	#"INSERT INTO " + customers + " (编号ID,分辨率Resolution,命名Name) VALUES ('1','320x240','240p低品质')"
	# executemany()多个条件插入
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
#-------------------------------插入其它执行命令------------------------------------------

def intoDB(a,val1,val2,val3,val4):
	hosturl = "localhost"
	youruesnames = "root"
	yourpassword = "123456"
	SQLname = "My_TVshows"
	customers = "Now_TVshows_001"
	Sqlcontent = "'" + str(a) + "'," + '"' + val1 + '",' + '"' + val2 + '",' + "'" + val3 + "'," + "'" + val4 + "'"
	Sqlcommand = "INSERT INTO " + customers + " (编号Id,电视剧中文名ChineseName,电视剧原名Originally,年代year,海报名称pic) VALUES (" + Sqlcontent + ")"
	#需要修改列的名称
	INTO_execute(hosturl, youruesnames, yourpassword, SQLname, customers, Sqlcommand)

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


def DDZ_TVshows_requests(url,number,funcatalog):
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
		if (requests_status_code(reshtml.status_code) == False):
			print("Not find TVshows in number :" + number + "Show wrong :" + str(reshtml.status_code))
			number = number + 1
			time.sleep(1)
			main(number, funcatalog)
		reshtml.encoding = 'utf-8'
		tree = etree.HTML(reshtml.text)
		#修改爬取信息
		items = tree.xpath("//div/header/h1[@class='product-title']/text()")
		if (len(items) != 0):
			year = tree.xpath("//div/header/h1[@class='product-title']/span[1]/text()")
			pic = tree.xpath("//div/header//img[@class='thumb']/@src")
			ChineseName,Originally,year = notebook(items[0], year[0])
			return ChineseName,Originally,year,pic[0]
	except:
		print("网页分析中发生错误，错误代码：10。程序继续。")
		conn = ConfigParser
		reading = conn.read(funcatalog)
		cofig = conn.get('ini', 'cofig')
		conn.set("ini", "cofig", cofig + "\n" + url)
		with open(funcatalog, "w+") as f:
			conn.write(f)
		del conn,reading
	number = number + 1
	main(number,funcatalog)


def main(number,funcatalog):
	conn = ConfigParser
	reading = conn.read(funcatalog)
	if(number <= 99999):
		ler = str(number)
		#ler = ler.rjust(5, '0')
		conn.set("ini", "passmath", str(number))
		with open(funcatalog, "w+") as f:
			conn.write(f)
		ChineseName,Originally,year,pic = DDZ_TVshows_requests("https://www.dandanzan10.top/dianshiju/" + ler + ".html",number,funcatalog)
		#网址
		print(number,ChineseName,Originally,year,pic)
		intoDB(number,ChineseName,Originally,year,pic)
		time.sleep(3)
		number = number + 1
		del conn, reading
		main(number,funcatalog)
	else:
		having = conn.get('ini', 'having')
		having = int(having)
		conn.set("ini", "passmath", "0")
		conn.set("ini", "having", str(having + 1))
		with open(funcatalog, "w+") as f:
			conn.write(f)
		del conn,reading,having
		__int__()


def __int__():
	funcatalog = os.getcwd() + "/Dandanzan电视剧.ini"
	#取脚本运行目录
	if not os.path.exists(funcatalog):
		raise FileNotFoundError("文件不存在")
	try:
		conn = ConfigParser
		reading = conn.read(funcatalog)
		passmath = conn.get('ini', 'passmath')
		having = conn.get('ini', 'having')
		number = int(passmath)
	#-------------------------------------写入数据------------------------------------
		# conn.set("ini", "passmath", str(number))
		# with open(funcatalog, "w+") as f:
		# 	conn.write(f)
	#-------------------------------------写入数据------------------------------------
	except:
		messagebox.showinfo("python提示", "Dandanzan电视剧错误：错误代码：03")
		print("无法读取Dandanzan电视剧.ini的配置信息，程序结束。")
		exit()
	del conn,reading
	main(number,funcatalog)


__int__()
# hosturl = "localhost"
# youruesnames = "root"
# yourpassword = "123456"
# SQLname = "My_TVshows"
# customers = "Now_TVshows_001"
# Sqlcommand = "SELECT * FROM " + customers
# Select_cursor(hosturl,youruesnames,yourpassword,SQLname,Sqlcommand)















