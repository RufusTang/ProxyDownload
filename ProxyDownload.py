# -*- coding: utf-8 -*-
# Python:      2.7.8
# Platform:    Windows
# Author:      wucl
# Program:     从代理网站获取可用代理
# History:     2015.6.11

import urllib2, re
from bs4 import BeautifulSoup

def get_proxies(url):
    """
    从代理网站获取可用代理ip地址列表并返回
    """
    resp = urllib2.urlopen(url)
    html = resp.read()
    soup = BeautifulSoup(html, 'html.parser')

    pattern = re.compile('([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5]):(\d+)')
    proxies = []

    for result in soup.findAll('p'):
        if result.find('span') !=-1:
            if len(pattern.findall(str(result))):
                ip = pattern.findall(str(result))[0][0] +"." + pattern.findall(str(result))[0][1] + "." +pattern.findall(str(result))[0][2]+"." +pattern.findall(str(result))[0][3]+":" +pattern.findall(str(result))[0][4]
                proxies.append(ip)
    return proxies



if __name__ == '__main__':
    urls = ['http://www.youdaili.net/Daili/http/27539.html','http://www.youdaili.net/Daili/http/27539_2.html','http://www.youdaili.net/Daili/http/27539_3.html','http://www.youdaili.net/Daili/http/27539_4.html','http://www.youdaili.net/Daili/http/27539_5.html']
    proxies = []
    for url in urls:
        proxies= proxies+get_proxies(url)

    print proxies
    Ipfile = open('Iplist.txt', 'w')
    for proxy in proxies:
        Ipfile.write(str(proxy)+'\n')

    Ipfile.close()