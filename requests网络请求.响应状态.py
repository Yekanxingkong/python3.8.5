import requests
import requests_cache
import requests_html
import tkinter.messagebox
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