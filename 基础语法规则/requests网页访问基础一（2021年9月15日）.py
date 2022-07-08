# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:29:53 2021

@author: Administrator
"""

import requests
class SpiderSignIn():    
    def _int_(self):
        url = 'http://www.bing.com'
        self.headers ={
            'User-agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
            }
        signhtml = requests.get(url = url ,headers = self.headers,timeout = 5.000)
        response = signhtml.status_code
        if response == 200:
            print('请求成功')
        elif response == 404:
            print('请求失败!请检查服务器连接,或者检查网络连接是否正常')
        self.html = signhtml.text
        
        
    def sitting(self):
        print(self.html)
        
if __name__ == '__main__':
    SpiderSignIn = SpiderSignIn()
    SpiderSignIn._int_()
    SpiderSignIn.sitting()

# =============================================================================
# r=requests.get("http://www.baidu.com/")
# 
# r.status_code
# http请求的返回状态，200表示连接成功，404表示连接失败
# 
# r.text
# http响应内容的字符串形式，url对应的页面内容
# 
# r.encoding
# 从HTTP header中猜测的响应内容编码方式
# 
# r.apparent_encoding
# 从内容分析出的响应内容的编码方式（备选编码方式）
# 
# r.content
# HTTP响应内容的二进制形式
# 
# r.headers
# http响应内容的头部内容            
# =============================================================================