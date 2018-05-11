import requests
import xlrd
import xlwt
import time
import os
from testcase.test.conn import *

db_name = 'sscp_test'
sql_1 = "select question from ai_question"
a_url = 'http://10.75.2.121:9200/api/qa'
robot_id = 175
x = QA_test (a_url , db_name , robot_id , sql_1)
print ('x=' , x)


def write_data ( file_name , sheet_name ):
    """
    :param file_name: 存储文件名
    :param sheet_name: 存储文件的sheet 名
    :param title_name:表土名list
    :return:
    """
    title_name = ["序号" , "学员提问" , "机器人回答" , "匹配结果"]
    # write_data = [[1 , 2 , 3 , ] , ['www.baidu.com' , 'www.123.com' , 'www.888.com'] , ['200' , '404' , '500'] ,
    #               ['请求成功' , '未找到' , '服务器错误']]
    start = time.time ()
    print ('start_time:' , start)

    # 创建一个待写入文件
    file_dir = os.path.dirname (__file__) + '../../testdata/' + file_name + '_测试结果.xlsx'
    workbook = xlwt.Workbook ()
    mysheet = workbook.add_sheet (sheet_name)
    style = xlwt.easyxf ("align:wrap on")  # 自动换行

    question_list = []
    response_lsit = []
    result_lsit = []
    data = QA_test(url,db_name,robot_id,search_q_sql)

    # 编写表头
    # sheet.write(col,row,str)
    n = 0
    for t in title_name:
        mysheet.write (0 , n , t)
        n += 1

    # 添加数据

    for row in range (1 , len (write_data[0])):
        for col in range (0 , len (title_name)):
            for list in write_data_lists:
                mysheet.write (row , col , row)
                mysheet.write (row , col , list[row - 1] , style)
    print ('mysheet=' , mysheet)

    workbook.save (file_dir)
    end = time.time ()
    print ("endtime:" , end)
    print ("运行时间：" , end - start)  # 运行时间


if __name__ == '__main__':
    write_data ('test' , 'write_test')

# *************************************************************************************************************
# start = time.time ()
# print ("starttime:" , start)  # unix时间戳
#
# book = xlrd.open_workbook ('requestData.xlsx')
# table = book.sheets ()[0]
# urllist = []
# codelist = []
# responselist = []
# rows = table.nrows
#
# for i in range (1 , table.nrows):
#     url = table.cell (i , 1).value
#     print ('url=' , url)
#     r = requests.get (url)
#     print ('r=' , r)
#     urllist.append (url)
#     codelist.append (r.status_code)
#     print ('codelist=' , codelist)
#     responselist.append (r.text)
#     # print('responselist=',responselist)
#
# book2 = xlwt.Workbook ()
# mysheet = book2.add_sheet ("mysheet")
# style = xlwt.easyxf ("align:wrap on")  # 自动换行
#
# title = ["序号" , "url" , "status_code" , "response"]
# n = 0
# # 写入表头
# for k in title:
#     mysheet.write (0 , n , k)
#     n += 1
#
# for j in range (1 , rows):
#     mysheet.write (j , 0 , j)
#     mysheet.write (j , 1 , urllist[j - 1] , style)
#     mysheet.write (j , 2 , codelist[j - 1] , style)
#     mysheet.write (j , 3 , responselist[j - 1] , style)
# print ('mysheet=' , mysheet)
#
# sec_col = mysheet.col (1)
# third_col = mysheet.col (2)
# forth_col = mysheet.col (3)
# sec_col.width = 256 * 50  # 第二列宽度
# third_col.width = 256 * 15  # 第三列宽度
# forth_col.width = 256 * 100  # 第四列宽度
#
# book2.save ("responseData.xls")
#
# end = time.time ()
# print ("endtime:" , end)
# print ("运行时间：" , end - start)  # 运行时间
