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
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    new_db_SQLname = False
    for (x,) in mycursor:
        if(x == SQLname):
            new_db_SQLname = True
        else:
            pass
    if(new_db_SQLname == False):
        mycursor.execute("CREATE DATABASE " + SQLname)
        return 1
    else:
        return 0
#-------------------------------创建数据库------------------------------------------
#-------------------------------删除数据库------------------------------------------
def Del_db(hosturl,youruesnames,yourpassword,SQLname):
    mydb = mysql.connector.connect(
        host=hosturl,
        user=youruesnames,
        passwd=yourpassword,
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    del_db_SQLname = False
    for (x,) in mycursor:
        if(x == SQLname):
            del_db_SQLname = True
        else:
            pass
    if(new_db_SQLname == True):
        mycursor.execute("DROP DATABASE " + SQLname)
        return 1
    else:
        return 0
#-------------------------------删除数据库------------------------------------------
#hosturl,youruesnames,yourpassword,sqlname,customers = "192.168.2.175","root","123456","数据库名称","表名称"