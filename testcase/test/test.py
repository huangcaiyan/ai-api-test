import requests
import json
import random
from .conn import conn
from base.reqeusts_headers import req_headers

url = 'http://10.75.2.121:9200/api/qa'


def qustion ():
    # 执行数据查询
    sql = "select question from ai_question"
    qa_array = conn (sql)

    def get_question():
        for ran in qa_array:
            s = json.dumps ({
                "question": ran ,
                "aiRobotId": 175 ,
            })


    # QA问题测试
    def qa_question ():
        name = random.randrange (100)
        headers = {'Content-Type': 'application/json' , 'Accept': 'application/json'}
        global ran
        for ran in qa_array:
            print ('ran=' , ran)
            s = json.dumps ({
                "question": ran ,
                "aiRobotId": 175 ,
            })
            qa_question_req = requests.post (url , data=s , headers=headers)
            qa_question_num = json.loads (qa_question_req.text)
            try:
                for line in qa_question_num['data']:
                    global answer
                    answer = line['answer']
                    print ("机器人回答：" + line['answer'])
                    print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
            except TypeError as e:
                answer = 0
                print ('机器人回答：抱歉，机器人回答不了您的问题。。。')
                print ('----------------------------------------------------------\n')

    qa_question ()

    # 连接MySQL数据库
    connection = pymysql.connect (host='10.75.2.178' , port=3306 , user='root' , password='SunLand2@' , db='sscp_test' ,
                                  charset='utf8mb4' , cursorclass=pymysql.cursors.DictCursor)
    # 通过cursor创建游标
    cursor = connection.cursor ()

    # 执行数据查询
    try:
        sql = "select  question from ai_question as a left join ai_answer as b on a.question_id = b.question_id  where answer = '%s'" % (
            answer)
        cursor.execute (sql)
    except AttributeError:
        pass
    # 查询数据库单条数据
    # result = cursor.fetchone()
    # # print(result)
    # try:
    #     for value in result.values():print('数据库查询问答结果： '+ value)
    # except AttributeError:
    #     print('没有查询到数据')

    # 查询数据库全部数据

    alist = []
    result = cursor.fetchall ()

    for data in result:
        for value in data.values ():
            print (data['question'])
            alist.append (data['question'])

    if ran in alist:
        print ('匹配成功')
    else:
        print ('匹配失败')
    print ('*******************************')
    connection.close ()


if __name__ == '__main__':
    qustion ()
