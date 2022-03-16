import pymssql
import pyodbc
import os
import mysql.connector
#-------------------------------查询数据表------------------------------------------
def New_execute(hosturl,youruesnames,yourpassword,SQLname,customers,Sqlcommand):
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		database=SQLname
	)
	mycursor = mydb.cursor()
	# ---------------查询数据库、数据表------------------
	#mycursor.execute("SHOW TABLES")
	# ---------------查询数据库、数据表------------------
	mycursor.execute(Sqlcommand)
	for (x,) in mycursor:
		print(x)
	# Sqlcommand = "SELECT * FROM " + customers
	# 每个列需要单独循环
#-------------------------------查询数据表,数据------------------------------------------
