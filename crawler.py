#  -*- coding = utf-8  -*-
import re       #re库，设定正则表达式，进行文字匹配
import urllib   #制定URL，获取网页数据，获得html文档
import urllib.request  #对服务器发送请求
import sys      #系统库
import xlwt     #进行excel操作，存到Excel表格
from bs4 import BeautifulSoup    #网页解析，对html文档进行parser解析，获取数据
import sqlite3  #进行SQLite数据库操作,存到数据库

def main():
    baseurl="https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist=getData(baseurl)
    savepath=".\\Douban_Movie_Top250.xls"
    #3.保存数据
    saveData(datalist,savepath)

    #askURL("https://movie.douban.com/top250?start=")

#全局变量

#电影超链接模式
findLink = re.compile(r'<a href="(.*?)">')     #创建正则表达式对象，即匹配字符串的规则，或称为匹配目标字符串的模式
                                               #前加r表示  忽视转义字符等特殊符号，因为链接里含有'/'
                                               #<a href="(.*?)">  是对链接的正则表达式的表示
#电影图片模式
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)  #re.S 表示忽略换行符,作用：让换行符包含在字符中

#电影名称模式
findTitle = re.compile(r'<span class="title">(.*)</span>')

#电影评分模式
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

#电影评价人数模式
findJudgeNumber = re.compile(r'<span>(\d*)人评价</span>')

#电影概况模式
findInq = re.compile(r'<span class="inq">(.*)</span>')

#电影相关内容模式(导演、主演等等相关内容)
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)   #'?'表示0次或多次



#函数1.爬取网页 -> 解析网页 -> 提取数据data（正则表达式校验）
def getData(baseurl):
    datalist=[]

    #调用获取页面信息的函数10次
    for i in range(0,10):  #(0,10)左闭右开的特性，从第0项（第一页）开始获取电影，
                           # 在i=9时，继续获取25部电影信息，最终完成对250部电影数据的获取
        url = baseurl + str(i*25)

        # 步骤1. 保存获取到的网页源码
        html = askURL(url)

        # 步骤2. 逐一解析数据（使用bs） #每一次html获取信息都进行解析数据
        soup = BeautifulSoup(html,"html.parser")   #形成soup树形结构对象,可以进行对文档的提取

        # 步骤3. 提取数据data （用for循环，对每一个item）
        for item in soup.find_all('div',class_="item"):     #查找符合要求的字符串(div标签中含有class（属性值）为item，及其子孙信息)，返回列表
            #print(item)      #测试用item做筛选的过滤效果 #查看电影item全部信息
            data =[]          #用data保存一部电影的所有信息
            item = str(item)  #转化为字符串，可以用正则表达式校验，用re
                              #调用re，设定正则表达式(模式)，查找指定的字符串


            # 校验一：提取网页链接link
            link = re.findall(findLink,item)[0]       #查找影片详情超链接（只取每个item下第一个）
            #print(link)                              #测试结果,返回成功
            data.append(link)                         #列表追加信息，将提取的信息加入data列表

            # 校验二：提取电影图片
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)

            # 校验三：提取电影的名称，或为多个名称，包含中文或外文
            titles = re.findall(findTitle,item)      #中文名或英文名，或者同时存在中英名称。需要判断中文、英文或外文名
            if(len(titles) == 2):      #存在两个名称，中文、英文（外文）
                ch_title = titles[0]
                data.append(ch_title)  #添加中文名进data
                for_title = titles[1].replace("/","")  #去掉外文名称前的符号“/”
                data.append(for_title)                 #添加外文名进data
            else:
                data.append(titles[0])
                data.append(' ')        #只有中文名，则为外文名留空

            # 校验四：提取电影的评分
            rating = re.findall(findRating,item)[0]
            data.append(rating)

            # 校验五：提取电影的评价人数
            judgeNum = re.findall(findJudgeNumber,item)[0]
            data.append(judgeNum)

            # 校验六：提取电影的概述
            inq = re.findall(findInq,item)
            if len(inq) !=0:
                inq = inq[0].replace("。","")  #去掉句号“。”
                data.append(inq)
            else:
                data.append(" ")        #inq留空

            # 校验七：提取电影的相关内容，含多条相关信息（导演、主演、年份等等）
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)  #替换<br/>
            bd = re.sub('/'," ",bd)                  #替换'/'
            data.append(bd.strip())                  #strip()去掉前后空格

            # 将校验数据所得的data放入datalist
            datalist.append(data)       #把一部电影item中处理好的数据放入datalist

    #print(datalist)  #验证数据校验的结果是否成功
    return datalist

# 函数2. 得到指定的一个URL的网页内容，返回html
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
    try:       #尝试接收服务器返回信息
        response = urllib.request.urlopen(request)  #服务器返回的信息
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:   #如果请求发生错误，则返回code码和reason原因
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html







#函数3.保存数据
def saveData(datalist,savepath):
    print("save...")    #输出结果提示信息
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)            # 创建workbook对象
    sheet = book.add_sheet('MovieData_DoubanTop250',cell_overwrite_ok=True)
    col = ("电影详情链接","图片链接","电影中文名","电影外文名","评分","评价人数","概况","相关内容")  #定义元组
    for i in range(0,8):
        sheet.write(0,i,col[i])  #写入列名

    for i in range(0,250):
        print("第%d部"%(i+1))
        data = datalist[i]       #读取一部电影的数据
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  #按列写入本部电影的数据

    book.save(savepath)   #保存

if __name__ == "__main__":   #当程序执行时
#调用函数
    main()
    print("电影数据爬取工作已完毕")