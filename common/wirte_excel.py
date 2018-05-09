import requests
import xlrd
import xlwt
import time
import os


def write_data ( file_name , sheet_name,title ):
    print ('start_time:' , time.time ())
    # 创建一个待写入文件
    file_dir = os.path.dirname (__file__) + '../../testdata/' + file_name + '_测试结果.xlsx'
    workbook = xlwt.Workbook ()
    sheet_name = book.add_sheet (sheet_name)
    style = xlwt.easyxf ("align:wrap on")  # 自动换行
    # title = ["序号" , "url" , "status_code" , "response"]
    n = 0
    # 写入表头
    for t in title:
        mysheet.write (0 , n , t)
        n += 1

    for j in range (1 , rows):
        mysheet.write (j , 0 , j)
        mysheet.write (j , 1 , urllist[j - 1] , style)
        mysheet.write (j , 2 , codelist[j - 1] , style)
        mysheet.write (j , 3 , responselist[j - 1] , style)
    print ('mysheet=' , mysheet)

    sec_col = mysheet.col (1)
    third_col = mysheet.col (2)
    forth_col = mysheet.col (3)
    sec_col.width = 256 * 50  # 第二列宽度
    third_col.width = 256 * 15  # 第三列宽度
    forth_col.width = 256 * 100  # 第四列宽度

    book2.save ("responseData.xls")

    end = time.time ()
    print ("endtime:" , end)
    print ("运行时间：" , end - start)  # 运行时间


start = time.time ()
print ("starttime:" , start)  # unix时间戳

book = xlrd.open_workbook ('requestData.xlsx')
table = book.sheets ()[0]
urllist = []
codelist = []
responselist = []
rows = table.nrows

for i in range (1 , table.nrows):
    url = table.cell (i , 1).value
    print ('url=' , url)
    r = requests.get (url)
    print ('r=' , r)
    urllist.append (url)
    codelist.append (r.status_code)
    print ('codelist=' , codelist)
    responselist.append (r.text)
    # print('responselist=',responselist)

book2 = xlwt.Workbook ()
mysheet = book2.add_sheet ("mysheet")
style = xlwt.easyxf ("align:wrap on")  # 自动换行

title = ["序号" , "url" , "status_code" , "response"]
n = 0
# 写入表头
for k in title:
    mysheet.write (0 , n , k)
    n += 1

for j in range (1 , rows):
    mysheet.write (j , 0 , j)
    mysheet.write (j , 1 , urllist[j - 1] , style)
    mysheet.write (j , 2 , codelist[j - 1] , style)
    mysheet.write (j , 3 , responselist[j - 1] , style)
print ('mysheet=' , mysheet)

sec_col = mysheet.col (1)
third_col = mysheet.col (2)
forth_col = mysheet.col (3)
sec_col.width = 256 * 50  # 第二列宽度
third_col.width = 256 * 15  # 第三列宽度
forth_col.width = 256 * 100  # 第四列宽度

book2.save ("responseData.xls")

end = time.time ()
print ("endtime:" , end)
print ("运行时间：" , end - start)  # 运行时间
