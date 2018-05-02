import requests
import json
from base.reqeusts_headers import *
from model.get_json_model import *
from base import config


# 新增知识库
def post_knowledge ( url , model_file_name , model_sheet , testdata_file_name , testdata_sheet ):
    knowledge_model = get_json_model (model_file_name , model_sheet , testdata_file_name , testdata_sheet)
    print ('x=>' , knowledge_model[0])
    model_item = random.sample (knowledge_model , 1)

    knowledge_json = json.dumps (random.sample (knowledge_model , 1))
    post_req = requests.post (url , data=knowledge_json , headers=req_headers)
    print (post_req.text)
    return post_req.text


# 修改知识库
def put_knowledge ():
    headers = req_headers
    data = json.dumps (
        {
            'name': 'string' ,
            'description': '0502'
        }
    )
    req_put = requests.put (config.base_url , data=data , headers=headers)
    print (req_put.text)


# 获取知识库列表
def get_knowledge_list ():
    req_get = requests.get (config.base_url + '')


if __name__ == '__main__':
    url = config.base_url + '/knowledge/'
    model_file_name = 'models'
    model_sheet = 'PostKnowledgeModel'
    testdata_file_name = 'testdata'
    testdata_sheet = 'PostKnowledgeData'
    post_knowledge (url , model_file_name , model_sheet , testdata_file_name , testdata_sheet)
    # put_knowledge ()
