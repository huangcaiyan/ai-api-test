import requests
from base.reqeusts_headers import *
from model.get_json_model import *
from base import config


def post_knowledge (url, model_file_name , model_sheet , testdata_file_name , testdata_sheet ):
    knowledge_model = get_json_model (model_file_name , model_sheet , testdata_file_name , testdata_sheet)
    print('knowledge_model=',knowledge_model)
    print('x=>',knowledge_model[0])
    model_item = random.sample(knowledge_model)

    knowledge_json = json.dumps(random.sample(knowledge_model,1))
    post_req = requests.post (url , data=knowledge_json , headers=req_headers)
    # print (post_req)
    return post_req.text


if __name__ == '__main__':
    url = config.base_url
    model_file_name = 'models'
    model_sheet = 'PostKnowledgeModel'
    testdata_file_name = 'testdata'
    testdata_sheet = 'PostKnowledgeData'
    post_knowledge(url, model_file_name , model_sheet , testdata_file_name , testdata_sheet)



