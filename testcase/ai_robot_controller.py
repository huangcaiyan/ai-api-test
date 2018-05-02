#coding:utf8

import requests
import json
import random
from base import config

# url = 'http://10.75.2.180:9100/robot'
url = config.base_url + '/robot'
id_list = []
#获取机器人列表
def get_robot():

    gb_req = requests.get(url)
    g_robot = json.loads(gb_req.text)
    print(g_robot)
    # names = g_robot['data']
    print(g_robot['data'])
    for line in g_robot['data']:
        lines = line['robotId']
        id_list.append(lines)
        print(line['robotId'])
    print('id_list=',id_list)


 #    ra = random.choice(int(lines))
 #   print(ra)


#添加机器人
def add_robot():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    s = json.dumps({"customKbId": [0], "description": "智能机器人", "knowledgeId": [0], "name": "小白", "robotId": 0,  "systemKbId": [0]})
    add_req = requests.post(url, data=s, headers = headers)
    print(add_req.text)

#更新机器人
def put_robot():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    s = json.dumps({"customKbId": [0], "description": "智能聊天机器人", "knowledgeId": [0], "name": "牛牛", "robotId": 3,"systemKbId": [0]})
    put_req = requests.put(url, data=s, headers = headers)
    print(put_req.text)

#删除机器人
def del_robot():
    del_url = url + '/ '
    del_payload = {'id':'3'}
    del_req = requests.delete(del_url + del_payload['id'])
    print(del_req.text)

#获取单个机器人信息
def g_robot():
    del_payload = {'id':2}

    # id = random.randint(len(id_list))

    # print('id=',id)
    del_req = requests.get(url+'/1')
    print('url=',del_req.url)
    print(del_req.text)



if __name__ == '__main__':
    # print('添加机器人：', end='')
    # add_robot()
    # print('获取机器人列表', end='')
    # get_robot()
    # print('\n')
    #
    #
    # print('更新机器人', end='')
    # put_robot()
    # print('获取机器人列表', end='')
    # get_robot()
    # print('\n')
    #
    #
    # print('删除机器人', end='')
    # del_robot()
    # print('获取机器人列表', end='')
    # get_robot()
    # print('\n')
    #
    # print('获取单个机器人信息', end='')
    g_robot()

    # get_robot()
