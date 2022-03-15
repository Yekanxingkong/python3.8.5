import pymssql
import pyodbc
import os
import mysql.connector
#-------------------------------创建数据库------------------------------------------
def New_db(hosturl,youruesnames,yourpassword,SQLname):
    mydb = mysql.connector.connect(
        host=hosturl,
        user=youruesnames,
        passwd=yourpassword,
    )
    print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE " + SQLname)
    #创建数据库，该命令为mysql数据库管理系统命令
    #mycursor.execute("DROP DATABASE " + SQLname)
    #删除数据库，该命令为mysql数据库管理系统命令
    mycursor.execute("SHOW DATABASES")
    for (x,) in mycursor:
        print(x)
#NewMysqldbCursor("localhost","root","123456","mydatabase")
#地址、名称、密码
#-------------------------------创建数据库------------------------------------------