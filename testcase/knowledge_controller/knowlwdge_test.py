import requests
import json
from common.reqeusts_headers import *
from base import config


# 新增知识库
def post_knowledge ():
    url = config.base_url + '/knowledge/'
    data = json.dumps (
        {
            "description": '添加知识库类别' ,
            "name": "pai学院123"
        }
    )
    req_post = requests.post (url , data=data , headers=req_headers)
    print ('req_post=' , req_post.text)


# 修改知识库
def put_knowledge ():
    url = config.base_url + 'knowledge/'
    data = json.dumps (
        {
            'name': 'string' ,
            'description': '0502'
        }
    )
    req_put = requests.put (url , data=data)
    print (req_put.text)


# 获取知识库列表
def get_knowledge_list ():
    url = config.base_url + '/knowledge/list'
    req_get = requests.get (url,headers = req_headers)
    print ('req_get=' , req_get.text)


#
# 发布知识库
def put_publish_knowledge ():
    url = config.base_url + '/knowledge/publish/'
    data = json.dumps (
        {
            'knowledgeId': '1'
        }
    )
    req_put = requests.put (url , data=data)
    print('req_put=',req_put)
    print ('保存并学习知识库：' , req_put.text)


# 保存并学习知识库
def put_save_and_learn_knowledge ():
    url = config.base_url + '/knowledge/publish/' + knowledgeId + '1'
    data = json.dumps (
        {
            'knowledgeId': 1 ,
            'first': '1'
        }
    )


if __name__ == '__main__':
    # post_knowledge ()
    # put_knowledge ()
    get_knowledge_list()
    # put_publish_knowledge()
