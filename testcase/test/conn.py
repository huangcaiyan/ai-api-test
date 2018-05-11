import random

import pymysql
import json
import requests


def conn ( search_sql ):
    # 连接MySQL数据库

    connection = pymysql.connect (host='10.75.2.178' , port=3306 , user='root' , password='SunLand2@' ,
                                  db='sscp_test' ,
                                  charset='utf8mb4' , cursorclass=pymysql.cursors.DictCursor)
    # 通过cursor创建游标
    cursor = connection.cursor ()
    cursor.execute (search_sql)
    result = cursor.fetchall ()

    search_results = []
    for r in result:
        for result_value in r.values ():
            search_results.append (result_value)
    connection.close ()
    return search_results


def get_all_question ():
    sql = "select question from ai_question"
    result = conn (sql)
    return result


def QA_test ():
    url = 'http://10.75.2.121:9200/api/qa'

    questions = get_all_question ()
    headers = {'Content-Type': 'application/json' , 'Accept': 'application/json'}
    Q_list = questions
    A_list = []
    R_list = []
    QAR_list = []
    for Q in questions:
        s = json.dumps ({
            "question": Q ,
            "aiRobotId": 175 ,
        })
        qa_question_req = requests.post (url , data=s , headers=headers)
        qa_question_text = json.loads (qa_question_req.text)
        try:
            qa_dict = {}
            for qa_question_data in qa_question_text['data']:
                A = qa_question_data['answer']
                search_equal_a_sql = "select  question from ai_question as a left join ai_answer as b on a.question_id = b.question_id  where answer = '%s'" % (
                    A)
                equal_a_question = conn (search_equal_a_sql)
                qa_dict['question'] = Q
                qa_dict['answer'] = A
                if Q in equal_a_question:
                    qa_dict['result'] = '匹配'
                    result = '匹配'
                else:
                    qa_dict['result'] = '不匹配'
                    result = '不匹配'
                A_list.append (A)
                R_list.append (result)
                QAR_list.append (qa_dict)
        except TypeError as e:
            print ('get_robot_answers =' , str (e))
            A = '无答案'

    print ('Q_list=' , Q_list)
    print ('A_list=' , A_list)
    print ('R_list=' , R_list)
    print ('QAR_list=' , QAR_list)
    return Q_list , A_list , R_list , QAR_list


if __name__ == '__main__':
    QA = QA_test ()
    print ('QA=' , QA)
