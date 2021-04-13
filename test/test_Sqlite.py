import sqlite3
'''
SQLite 亲和(Affinity)类型
     TEXT       （包含众多char类型）
     NUMERIC     （包含日期数类型、布尔数类型）
     INTEGER   (包含众多int类型)
     REAL      （包含众多浮点型数据）
     NONE




'''





# 测试1.连接数据库
# conn = sqlite3.connect("test_sqlite.db")   #打开或创建数据库文件，没有则创建并打开
# print("Opened database successfully")
#
#
#
# 测试2.建表
# c = conn.cursor()    #获取游标
#
# #  '''结构可以保持字符串结构，为段落
# sql = '''
#       create table company
#           ( id int primary key not null,
#           name text not null,
#           age int not null,
#           address char(50),
#           salary real);
#
# '''
#
# c.execute(sql)       #执行sql语句
# conn.commit()        #提交数据库操作
# conn.close()         #关闭数据库连接
#
# print("Created .db successfully")


# 测试3.插入数据

conn = sqlite3.connect("test_sqlite.db")   #打开或创建数据库文件，没有则创建并打开
print("Opened database successfully")

c = conn.cursor()    #获取游标

#插入语句
# sql1 = '''
#       insert into company (id,name,age,address,salary)
#         values(1,'张三',23,"健翔桥",7000);
#
# '''
# sql2 = '''
#       insert into company (id,name,age,address,salary)
#         values(2,'李四',22,"清河小营",8000);
#
# '''

sql = "select id,name,address,salary from company"
'''

'''

# 测试4.查询数据

cursor = c.execute(sql)

for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3],"\n")  #'\n'每查完一行信息，插入换行


conn.close()         #关闭数据库连接

print("Selected data successfully")

















