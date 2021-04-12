import xlwt
'''  原理测试
workbook = xlwt.Workbook(encoding="utf-8")    #创建workbook对象
worksheet = workbook.add_sheet('sheet1')      #创建工作表
worksheet.write(0,0,'hello')     #写入数据，
                                 # 参数1：行，参数2：列，参数3：内容
workbook.save('test_xlwt.xls')     #保存数据表
'''

workbook = xlwt.Workbook(encoding="utf-8")    #创建workbook对象
worksheet = workbook.add_sheet('sheet1')

#练习：创建9*9乘法表  目的：实际上实现对每个单元格的访问
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))
workbook.save('test_xlwt.xls')

