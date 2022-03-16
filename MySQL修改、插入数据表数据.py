import pymssql
import pyodbc
import os
import mysql.connector
#-------------------------------插入数据、执行其它命令------------------------------------------
def INTO_execute(hosturl,youruesnames,yourpassword,SQLname,customers,Sqlcommand):
	mydb = mysql.connector.connect(
		host=hosturl,
		user=youruesnames,
		passwd=yourpassword,
		database=SQLname
	)
	mycursor = mydb.cursor()
	mycursor.execute(Sqlcommand)
	#Sqlcommand = "INSERT INTO " + customers + " (列名) VALUES ('数据1','数据2','数据3')"
	# executemany()多个条件插入
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
#-------------------------------插入数据、执行其它命令------------------------------------------
# 例如：
#--------------------------------------------------------------------------查询重复命令-----------------------------------------------------------------------------------------
# customers = 表名
# row = "列名"
# Sqlcommand = "SELECT * FROM " + customers + " WHERE " + row + " IN (SELECT " + row + " FROM " + customers + " GROUP BY " + row + " HAVING COUNT(" + row + ") > 1) "
#select 列名 from 表名 group by 主项;select distinct 列名 from 表名
#--------------------------------------------------------------------------查询重复命令-----------------------------------------------------------------------------------------