from common.post import post
from common.mysql_util import MysqlUtil
import logging
import xlwt

mysqlUtil = MysqlUtil ()


def get_questions ():
    sql = "select question from ai_question"
    questions = mysqlUtil.fetchall (sql)
    # print ('question=' , questions)
    return questions


def test_qa ():
    url = '/api/qa'
    q_list = []
    a_list = []
    r_list = []
    for question in get_questions ():
        data = {
            "question": question ,
            "aiRobotId": 175 ,
        }
        try:
            response = post (url , data)
            if response['code'] == 200:
                data = response['data'][0]
                if data != 'n':
                    answer = data['answer']
                    sql = "select  question from ai_question as a left join ai_answer as b on a.question_id = b.question_id  where answer = '%s'" % (
                        answer)
                    find_q = mysqlUtil.fetchall (sql)
                    if question in find_q:
                        result = 1
                    else:
                        result = 0
                    r_list.append (result)
                    q_list.append (question)
                    a_list.append (answer)
            else:
                answer = '没有可用的答案-1'
                result = 0
        except TimeoutError as e:
            answer = '没有可用的答案-2'
            result = 0
            logging.error ('Time Out!')
        # print ('Q=' , question)
        # print ('A=' , answer)
        # print ('result=' , result , '\n *************************************************************')
    return q_list , a_list , r_list


def write_result ():
    workbook = xlwt.Workbook ()
    table = workbook.add_sheet ('qa_test_result')



if __name__ == '__main__':
    test_qa ()
    print ('result=' , test_qa ())
    print ('q_list_len=' , len (test_qa ()[0]) , 'q_list=' , test_qa ()[0])
    print ('a_list_len=' , len (test_qa ()[1]) , 'a_list=' , test_qa ()[1])
    print ('r_list_len=' , len (test_qa ()[2]) , 'r_list=' , test_qa ()[2])
