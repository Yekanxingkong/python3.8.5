import pymssql
import pyodbc
import os
import sys
import re
from urllib.parse import unquote,urlencode,quote
import struct
import mysql.connector
# 本地"localhost"
hosturl,youruesnames,yourpassword,sqlname,customers = "192.168.2.175","root","123456","数据库名称","表名称"
def dbnew_database(hosturl,youruesnames,yourpassword,sqlname,customers):
	try:
		mydb = mysql.connector.connect(
			host=hosturl,
			user=youruesnames,
			passwd=yourpassword,
			charset="utf8"
		)
	except:
		debug = hosturl + "数据库未能连接，10秒后重试。"
		# sys.exit()
		return False
	mycursor = mydb.cursor()
	sqlcommand = "SHOW DATABASES"
	mycursor.execute(sqlcommand)
	for (x,) in mycursor:
		if(x == sqlname):
			debug = "find now"
			break
		else:
			debug = "this is not find"
	if(debug == "this is not find"):
		mycursor.execute("CREATE DATABASE " + sqlname)
		mycursor.execute("ALTER DATABASE " + sqlname + " DEFAULT CHARACTER SET utf8")
	mydb.close()
	return True
# 	创建数据表需要数据表列的类型，是不能创建空表的。因此如果找不到直接中断
#   sqltxt = 输入txt的名字就可以，不要加后缀
#   sqltxt 的数据类型 SQL列表的表头名称（自定义不能有特殊符号） + 一个空格 + 数据类型（固定）
def dbnew_customers(hosturl,youruesnames,yourpassword,sqlname,customers,sqltxt):
	try:
		mydb = mysql.connector.connect(
			host=hosturl,
			user=youruesnames,
			passwd=yourpassword,
			database=sqlname,
			charset="utf8"
		)
	except:
		debug = hosturl + "数据库未能连接，10秒后重试。"
		# sys.exit()
		return False
	mycursor = mydb.cursor()
	sqlcommand = "SHOW TABLES"
	mycursor.execute(sqlcommand)
	debug = "this is first start"
	for (x,) in mycursor:
		if (x == customers):
			debug = "find now"
			break
		else:
			debug = "this is not find"
	if (debug == "this is first start" or debug == "this is not find"):
		try:
			f2 = open(os.getcwd() + "\\" + sqltxt +".txt", "r", encoding='UTF-8')
		except:
			debug = "未能找到目录，请确认配置文件是否在同一目录之下"
			# sys.exit()
			return debug
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
	mydb.close()
	return True
sqlcommand = "CREATE DATABASE " + sqlname#创建数据库，该命令为mysql数据库管理系统命令
sqlcommand = "DROP DATABASE " + sqlname#删除数据库，该命令为mysql数据库管理系统命令
sqlcommand = "SHOW DATABASES"#展示数据库命令
sqlcommand = "CREATE TABLE " + customers + " (" + a + ")"#创建数据表，表不可为空值，a = 数据（数据类型）
sqlcommand = "SHOW TABLES"#展示数据表命令
sqlcommand = "DROP TABLE " + customers#删除数据表
sqlcommand = "INSERT INTO " + customers + "(列名，也可以不添加) VALUES (对应的数据，用’‘，隔开)"#插入数据，executemany()多个条件插入，mycursor.rowcount显示插入的数量
sqlcommand = "SELECT * FROM " + customers#查询命令
sqlcommand = "UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值"#修改表的数据
----------------------------查询数据表下列的数值-------------------------------------
mycursor = mydb.cursor()
cursor = mycursor.description
for x in cursor:
	print(x)
----------------------------查询数据表下列的数值-------------------------------------
----------------------------查询数据表下内容-------------------------------------
mycursor = mydb.cursor()
mycursor.execute(sqlcommand)
for (x,) in mycursor:
	print(x)
查询单列的内容，可以用这样的方式取消，输出有括号和逗号
----------------------------查询数据表下内容-------------------------------------
--------------------------------------------------------------------------删除重复-----------------------------------------------------------------------------------------
row = "需要查询的列"
ID = "列的ID"
Sqlcommand = "DELETE FROM " + customers + " WHERE " + ID + " NOT IN ( SELECT hd.minid FROM ( SELECT MIN( " + ID + " ) AS minid FROM " + customers + " GROUP BY " + row + " ) hd )"
Sqlcommand = "SELECT * FROM " + customers + " WHERE " + row + " IN (SELECT " + row + " FROM " + customers + " GROUP BY " + row + " HAVING COUNT(" + row + ") > 1) "
--------------------------------------------------------------------------删除重复-----------------------------------------------------------------------------------------

