import random

import pymysql


class SQLHandle(object):
    def __init__ ( self ):
        self.url = 'http://10.75.2.121:9200/api/qa'
        # 连接MySQL数据库
        self.connection = pymysql.connect (host='10.75.2.178' , port=3306 , user='root' , password='SunLand2@' ,
                                           db='sscp_test' ,
                                           charset='utf8mb4' , cursorclass=pymysql.cursors.DictCursor)
        # 通过cursor创建游标
        self.cursor = self.connection.cursor ()

    # 获取一个随机问答
    def select_all_questions ( self ):

        # 执行数据查询
        sql = "select question from ai_question"
        self.cursor.execute (sql)
        qa_array = []
        # 查询全部的数据
        result = self.cursor.fetchall ()
        for data in result:
            for value in data.values ():
                qa_array.append (value)
        # 关闭数据连接
        self.connection.close ()
        ran1 = qa_array[random.randint (0 , len (qa_array))]
        print ("随机问答：" , ran1)

    def test ( self ):
        # 执行数据查询
        # sql = "select question, answer from ai_question as a inner join ai_answer as b on a.question_id = b.question_id   "
        sql = "select  question from ai_question as a left join ai_answer as b on a.question_id = b.question_id  where answer = '%s'" % (
            test2_qa.answer)
        print ('sql=' , sql)
        cursor.execute (sql)
        all_values = cursor.fetchall ()
        print ('all_values=' , all_values)

        # 查询数据库单条数据
        result = cursor.fetchone ()
        print ('result=' , result)
        for value in result.values ():
            print ('数据库查询问答结果： ' + value)
if __name__ == '__main__':

