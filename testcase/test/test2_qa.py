#coding:utf8

import requests
import json
import random
import pymysql.cursors

url = 'http://10.75.2.121:9200/api/qa'

# 连接MySQL数据库
connection = pymysql.connect(host='10.75.2.178', port=3306, user='root', password='SunLand2@', db='sscp_test',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
# 通过cursor创建游标
cursor = connection.cursor()

# 执行数据查询
sql = "select question from ai_question"

cursor.execute(sql)

#查询数据库单条数据
# result = cursor.fetchone()
# print(result)
# for value in result.values():print(value)
qa_array = []
#查询全部的数据
result = cursor.fetchall()
for data in result:
    for value in data.values():
        # print(data)
        # print(value)
        qa_array.append(value)

# 关闭数据连接
connection.close()

ran1 = qa_array[random.randint(0, len(qa_array))]
print("随机问答："+ ran1)


#QA问题测试
def qa_question():
    name = random.randrange(100)
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    s = json.dumps({
      "question": ran1 ,
      "aiRobotId": 175,
})
    qa_question_req = requests.post(url, data=s, headers = headers)
    # print(qa_question_req.text)
    qa_question_num = json.loads(qa_question_req.text)
    # print(qa_question_num['data'])
    for line in qa_question_num['data']:
        global answer
        answer = line['answer']
        print("机器人回答："+ line['answer'])




if __name__ == '__main__':
    # print('qa：', end='')
    # for i in range(100):
    qa_question()


