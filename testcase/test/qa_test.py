import requests
import json
from common.mysql_util import MysqlUtil
from base.reqeusts_headers import req_headers
from base.config import base_url

mysql_util = MysqlUtil ()


def get_all_question ():
    fetchall_sql = "select question from ai_question"
    all_question = mysql_util.fetchall (fetchall_sql)
    return all_question


def get_robot_answer ():
    question_list = get_all_question ()
    sql_pre = "select  question from ai_question as a left join ai_answer as b on a.question_id = b.question_id  where answer = '%s'"
    q_list = ['开学典礼什么时候']
    a_list = []
    find_q_list = []
    r_list = []
    write_list = []
    for q in question_list:
        s = json.dumps ({
            "question": q ,
            "aiRobotId": 175 ,
        })
        qa_question_req = requests.post (base_url , data=s , headers=req_headers)
        qa_question_data = json.loads (qa_question_req.text)['data']
        if qa_question_data == 'no available answer!':
            answer = '没有可用的答案'
        else:
            write_data = []
            for line in qa_question_data:
                answer = line['answer']
                # print ('机器人回答：' , answer)
                sql = sql_pre % (answer)
                find_q = mysql_util.fetchall (sql)
                find_q_one = mysql_util.fetchone (sql)
                if q in find_q:
                    result = 1
                else:
                    result = 0
                find_q_list.append (find_q_one)
                r_list.append (result)
        a_list.append (answer)
        write_list.append (q_list , find_q_list , a_list , r_list)
    return write_list


if __name__ == '__main__':
    data = get_robot_answer ()
    print ('data=' , data)
