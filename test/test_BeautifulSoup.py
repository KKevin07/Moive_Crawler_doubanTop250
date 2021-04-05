'''
BeautifulSoup4: 将复杂HEML文档转换成一个复杂的树形结构，
                每个节点都是Python对象，对象共有四种：
                -Tag
                -NavigableString
                -BeautifulSoup
                -Comment
'''
from bs4 import  BeautifulSoup

file = open("./baidu.html","rb")       #read(bytes)方式打开html文件
html = file.read()
bs = BeautifulSoup(html,"html.parser") #用html.parser解析器 #用bs形成树形结构

#print(bs.title)        #根据标签在html形成的树结构中，抓取符合标签的第一个结构及其内容
#print(bs.a)
#print(bs.head)

#print(type(bs.head))   #查询bs.head的类型，返回值为 class 'bs4.element.Tag'

# 1. Tag  标签及其内容：拿到它找到的第一个内容


print(bs.title.string)         #只输出string字符内容，不打印Tag,返回值为 “百度一下，你就知道”
print(type(bs.title.string))   #查询bs.title.string的类型，返回值为<class 'bs4.element.NavigableString'>






