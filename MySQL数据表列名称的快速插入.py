import pymssql
import pyodbc
import os
import mysql.connector
#-------------------------------------数据表列名称的快速插入--------------------------------------
def IntenSQL():
	hosturl = "localhost"
	youruesnames = "root"
	yourpassword = "123456"
	SQLname = "数据库名称"
	customers = "表名称"
	f2 = open("1.txt", "r", encoding='UTF-8')
	lines = f2.readlines()
	val = ""
	for i in lines:
		i = repr(i)
		#显示字符串中的特殊符号
		math = i.find("\\n")
		if (i.find("\\n") != -1):
			i = i[0:i.find("\\n")]
		val = val + i + ","
	val = val[0:len(val) - 1]
	val = val.replace("'", '')
	# 去掉中间的指定字符串，或者前后的指定字符串
	val = val.strip("'")
	# 读取的时候会有特殊符号，要把特殊符号给去掉，并且去掉空格
	f2.close()
	Sqlcontent = val
	Sqlcommand = Sqlcontent
	New_execute(hosturl, youruesnames, yourpassword, SQLname, customers, Sqlcommand)
	#-------------------------------查询命令---------------------------------------
	Sqlcommand = "SELECT * FROM " + customers
	Select_cursor(hosturl, youruesnames, yourpassword, SQLname,Sqlcommand)
#-------------------------------------数据表列名称的快速插入--------------------------------------