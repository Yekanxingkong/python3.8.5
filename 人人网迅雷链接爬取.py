# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:32:07 2021

@author: Administrator
"""
import requests
from lxml import etree
class SpiderSignIn():    
    def _int_(self,url):
        self.headers ={
            'User-agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
            }
        signhtml = requests.get(url = url ,headers = self.headers,timeout = 5.000)
        response = signhtml.status_code
        if response == 200:
            print('请求成功')
            self.html = signhtml.text
        elif response == 404:
            print('请求失败!请检查服务器连接,或者检查网络连接是否正常')

    def sitting(self):
        self._int_('https://chaoqing.co/')
        Obtain = etree.HTML(self.html)        
        ObtainHeret = Obtain.xpath('//a/@href')   
        a = ''
        for LoopA in ObtainHeret:
            herf = LoopA.find('html')#没有找到返回-1
            if herf != -1 and a.find(LoopA) == -1:
                a = a + LoopA
                self.SignInSeed(LoopA)
            else:
                pass

    def SignInSeed(self,seedurl): 
        print('获取到的电影网址：'+ seedurl)
        self._int_(seedurl)        
        tree = etree.HTML(self.html)
        stree = tree.xpath('///a/@href')
        litte = tree.xpath('///a/@data-title')
        # litte = tree.xpath('///span/text()')//寻找更小的标题，网页源代码有颜色
        print(litte)
        for LoopA in stree:
            herf = LoopA.find('magnet:?xt=urn')            
            if herf != -1:
                print(LoopA)

if __name__ == '__main__':
    SpiderSignIn = SpiderSignIn()
    SpiderSignIn.sitting()
    SpiderSignIn._int_()
    SpiderSignIn.SignInSeed()