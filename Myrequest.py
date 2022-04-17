import os
import re
import requests
import requests_cache
import requests_html
import configparser
import tkinter.messagebox
import time
import struct
import bs4
import shutil
import json
from urllib.parse import unquote,urlencode,quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
from browsermobproxy import Server
BeautifulSoup = bs4.BeautifulSoup()
ConfigParser = configparser.ConfigParser()
messagebox = tkinter.messagebox

#需要运行js的浏览器模拟访问
# 占用非常大的内存，运行速度很慢，一般运用于搜索，和匿名访问
def requests_Chromeget_url(url):
	proxies = {'http': None,
			   'https': None
			   }
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
		"sec-ch-ua-platform": "Windows",
		"Connection": "keep-alive",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Language": "zh-CN,zh;q=0.8"
	}
	res = requests_html.HTMLSession(
		browser_args=[
			'--no-sand',  # 沙箱环境
			'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'  # 自定义UA
		],
		headless=False
	)
	value = urlencode({'text': "我是转码"})
	# 中文搜索时需要进行对十六进制转换
	debug = quote(name)#单词转十六进制
	debug = unquote(value)#解码
	html = res.get(url, headers=headers,proxies=proxies)
	html.html.render()
	#第一次需要下载Chromium，也可以手动安装：Chromium extracted to: C:\Users\Administrator\AppData\Local\pyppeteer\pyppeteer\local-chromium\588429
	#目录是需要自己创建的，来源python3.8.5\Lib\site-packages\pyppeteer\chromium_downloader.py，print（DOWNLOADS_FOLDER，REVISION）
	#目录名称要一模一样，包括谷歌的
	html.encoding = 'utf-8'
	tree = etree.HTML(html.text)
	# 转换为text文档
	items = html.html.links
	#提取网页链接
	for i in items:
		print(i)

# 一般访问
def requests_get_url(url):
	proxies = {'http': None,
			   'https': None
			   }
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
		"sec-ch-ua-platform": "Windows",
		"Connection": "keep-alive",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Language": "zh-CN,zh;q=0.8"
	}
	res = requests.get(url, headers=headers, proxies=proxies, timeout=8)
	html = res.text()
# 	1、写法
	res.encoding = 'utf-8'
	tree = etree.HTML(res.text)


# 模拟浏览器发出访问，同时运行js，调用java，获取network中的数据
# 注意：创建一个谷歌浏览器，再创建一个java，用完之后一定要关闭
# 安装java环境，安装二进制文件，安装一个轻量级谷歌，安装相应的库
# 启动代理, 修改下载的文件路径
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



