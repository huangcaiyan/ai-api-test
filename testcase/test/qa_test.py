import requests
import json
import random
import pymysql.cursors
from .conn import SQLHandle


class QATest:
    def __init__(self):
        self.sql = SQLHandle()

    # QA问题测试
    def qa_question ( self ):
        global answer
        name = random.randrange (100)
        headers = {'Content-Type': 'application/json' , 'Accept': 'application/json'}
        s = json.dumps ({
            "question": self.ran1 ,
            "aiRobotId": 175 ,
        })
        qa_question_req = requests.post (self.url , data=s , headers=headers)
        qa_question_num = json.loads (qa_question_req.text)
        print ('qa_question_num=' , qa_question_num)
        if qa_question_num['data'] == 'no available answer!':
            answer = '抱歉，机器人无法回答您的问题！请换个问法，谢谢！'
        else:
            for line in qa_question_num['data']:
                answer = line['answer']
        print ('机器人回答：' , answer)


if __name__ == '__main__':
    qatest = QATest ()
    qatest.qa_question ()
