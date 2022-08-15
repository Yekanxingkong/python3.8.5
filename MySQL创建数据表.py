import pymssql
import pyodbc
import os
import mysql.connector
#-------------------------------创建数据表------------------------------------------
def New_execute(hosturl,youruesnames,yourpassword,SQLname,customers,Sqlcommand):
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		database=SQLname
	)
	mycursor = mydb.cursor()
	#mycursor.execute("CREATE TABLE " + customers + " (" + Sqlcommand + ")")
	mycursor.execute("SHOW TABLES")
	for (x,) in mycursor:
		print(x)
#-------------------------------创建数据表------------------------------------------
#customers = 表名称
#Sqlcommand = "列名称1 INTEGER(50),列名称2 VARCHAR(255)"
#Mysql的插入语句，注意数据类型
#sql表创建的时候，必须携带列的类型，无法创建完全空表！！！！！！


hosturl,youruesnames,yourpassword,SQLname,customers = "192.168.2.175","root","123456","CDK","PUBGcdk"
Sqlcommand = "序号 INTEGER(50),PUBG_CKD VARCHAR(255),状态 VARCHAR(255)"
New_execute(hosturl,youruesnames,yourpassword,SQLname,customers,Sqlcommand)