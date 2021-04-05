#  -*- coding = utf-8  -*-
import re       #正则表达式，进行文字匹配
import urllib   #制定URL，获取网页数据
import urllib.request  #对服务器发送请求
import sys      #系统库
import xlwt     #进行excel操作，存到Excel表格
from bs4 import BeautifulSoup    #网页解析，获取数据
import sqlite3  #进行SQLite数据库操作,存到数据库

def main():
    baseurl="https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist=getData(baseurl)
    savepath=".\\Douban_Movie_Top250.xls"
    #3.保存数据
    #saveData(savepath)

    askURL("https://movie.douban.com/top250?start=")







#函数1.爬取网页
def getData(baseurl):
    datalist=[]

    #调用获取页面信息的函数10次
    for i in range(0,10):  #(0,10)左闭右开的特性，从第0项（第一页）开始获取电影，
                           # 在i=9时，继续获取25部电影信息，最终完成对250部电影数据的获取
        url = baseurl + str(i*25)
        html = askURL(url) #保存获取到的网页源码

        # 函数2.逐一解析数据 #每一次html获取信息都进行解析数据

    return datalist

#得到指定的一个URL的网页内容
#对豆瓣电影的爬取工作运用在250部电影，需要10个页面，每一页含有25部电影，
def askURL(url):
    head={               #模拟本机IE浏览器的头部信息，用于伪装
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68"
    }                      #head内信息多则用列表方式
                           #head["User-Agent"] #head内信息不多时使用键值对方式
                           #User-Agent表示本机的类型和浏览器信息（本质上是告知目标网页服务器，本机可以接受什么类别的文件内容）

    request=urllib.request.Request(url,headers=head)
    #urllib.request进行访问，向服务器发送请求，括号内为封装的信息（网址、头部），用request对象接收
    html = ""  #用于存储服务器返回的信息
    try:     #尝试接收服务器返回信息
        response = urllib.request.urlopen(request)  #服务器返回的信息
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:   #如果请求发生错误，则返回code码和reason原因
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html







#函数3.保存数据
def saveData(savepath):
    print("save...") #返回值待定，只是为了格式不出错

if __name__ == "__main__":   #当程序执行时
#调用函数
    main()