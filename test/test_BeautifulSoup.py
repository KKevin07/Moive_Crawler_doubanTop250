'''
BeautifulSoup4: 将复杂HTML文档转换成一个复杂的树形结构，
                每个节点都是Python对象，对象共有四种类型：
                -Tag
                -NavigableString
                -BeautifulSoup
                -Comment
BeautifulSoup4 使用作用：学会如何去定位想要的文本、标签
               意义：在爬虫方法里提取有用的信息、数据，要熟练掌握，非常重要
'''
from bs4 import  BeautifulSoup

file = open("./baidu.html","rb")       #read(bytes)方式打开html文件
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser") #bs函数解析，用html.parser解析器 #用bs形成树形结构

#print(bs.title)        #根据标签在html形成的树结构中，抓取符合标签的第一个结构及其内容
#print(bs.a)
#print(bs.head)

#print(type(bs.head))   #查询bs.head的类型，返回值为 class 'bs4.element.Tag'

# 类型1. Tag  标签及其内容：拿到它找到的第一个内容


# print(bs.title.string)         #只输出string字符内容，不打印Tag,返回值为 “百度一下，你就知道”
# print(type(bs.title.string))   #查询bs.title.string的类型，返回值为<class 'bs4.element.NavigableString'>

# 类型2.NavigableString   标签里的字符串（内容）

#print(bs.a.attrs)       #attrs可以拿到一个标签里的所有属性，返回值为 {'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'}

#print(type(bs))        #查询对象bs的类型，返回值为<class 'bs4.BeautifulSoup'>
# 类型3.BeautifulSoup 表示整个文件

#print(bs.name)          #返回值为[document]
#print(bs)               #实际上为html文档内的内容

# print(bs.a.string)       #第一个标签a的string为<!--新闻-->，这里的a.string输出时去掉了字符注释，返回值为“新闻”
# print(type(bs.a.string)) #查看第一个标签a的类型，返回值为<class 'bs4.element.Comment'>

# 类型4.Comment  是一个特殊的NavigableString,输出的内容不包含注释符号
#常用的方法有BeautifulSoup string  按Tag标签  三种

#____________________分割线_______________________________

#文档的遍历

#contents:获取Tag的所有子节点，返回一个list。
#print(bs.head.contents)      #可以获取到制定标签里的内容，以列表的形式
#print(bs.head.contents[1])    #抓取列表内容的第二条信息
#存在其他遍历方法，这里不再多引述。


#文档的搜索

# 搜索方式 一. find_all()       查找所有     (最经常使用)
# 作用.   字符串过滤：会查找与字符串完全匹配的内容
#t_list = bs.find_all("a")

import re
# 方案1.1 正则表达式搜索       使用search()方法来匹配内容,匹配含有指定信息的某一标签及其内容
#t_list= bs.find_all(re.compile("a"))

# 方法 ：传入一个函数（方法），根据函数的要求来搜索    （功能强大）
# def name_is_exists(tag):          #搜索含有“name”的Tag标签，条件：tag.has_attr("name")
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:       #打印列表信息的for循环方式，能让列表的显示更清晰、更醒目
#     print(item)

#print(t_list)


# 方案1.2  kwargs参数（关键字参数）        #根据kwargs参数特征来匹配

#t_list= bs.find_all(id="head")   #匹配条件：  参数id="head"
#t_list= bs.find_all(class_=True)  #匹配条件： 参数class存在
#t_list= bs.find_all(href="http://news.baidu.com")   #匹配条件：href="http://news.baidu.com

# for item in t_list:
#     print(item)

# 方案1.3   text参数

#t_list= bs.find_all(text = "hao123")   #匹配“hao123”文本
#t_list= bs.find_all(text = ["hao123","地图","贴吧"])

#text参数结合正则表达式，进行查询（返回值为 标签里的字符串）
#t_list= bs.find_all(text=re.compile("\d"))  #条件：含有“\d”格式的文本  #可查询含\d数字的文本，返回值为 标签里的字符串


#  方案1.4  limit  参数

# t_list = bs.find_all("a",limit=3)  #只查询三个
#
# for item in t_list:
#     print(item)


#  搜索方式 二. css 选择器 （快速定位某个点或某个内容）（经常用）(返回值类型为 列表)

#print(bs.select('title'))

#t_list = bs.select('title')  #用过标签来查找
#t_list = bs.select(".mnav")   #用类名来查找，"."指代类，"mnav"为类名
#t_list = bs.select("#u1")     #用id来查找,"#"指代id
#t_list = bs.select("a[class='bri']")   #通过属性来查找  #条件：a标签中的属性中含“bri”

#t_list = bs.select("head>title")  #通过子标签来查找 #找<head>下的<title>

#也可通过兄弟结点标签来查找
t_list = bs.select(".mnav ~ .bri")    #与mnav类别同层次的bri类型

print(t_list[0].get_text())  #print()方式下，get_text()拿到标签下的文本

#for item in t_list:
#    print(item)

#———————————————————————分割线—————————————————————————————————————————————————————————————————————









