import requests
import json
from base.config import *
from base.reqeusts_headers import *


def add_knowledge ():
    url = base_url + '/knowledge/'
    headers = req_headers
    payload = json.dumps (
        {
            "description": "string" ,

            "name": "0502知识库"
        }
    )
    add_req = requests.post (url=url , data=payload , headers=headers)
    print ('添加知识库：' , add_req.text)

if __name__ == '__main__':
    add_knowledge()
