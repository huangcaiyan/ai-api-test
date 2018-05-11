import requests
from common.common_info import *
import json
import logging


def post ( url , data ):
    post_url = base_url + url
    json_data = json.dumps (data)
    try:
        response = requests.post (post_url , data=json_data , headers=req_headers)
        response_text = json.loads (response.text)
        return response_text
    except TimeoutError as e:
        logging.error ('Time Out!')
        return None


if __name__ == '__main__':
    url = '/api/qa'
    #
    data = {
        "question": '开学典礼什么时候开始？' ,
        "aiRobotId": 175 ,
    }
    result = post (url , data)
    print ('result=' , result)

    response = {}
    code = result['code']
    answer = result['data'][0]['answer']
    msg = result['msg']

    response['code'] = code
    response['answer'] = answer
    response['msg'] = msg
    print ('answer=' , answer)
    print ('code=' , code)
    print ('msg=' , msg)
    print ('response=' , response)
