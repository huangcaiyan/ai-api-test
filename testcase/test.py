from base.reqeusts_headers import *
from model.get_json_model import *
from base import config


def post_knowledge ():
    json_data = json.dumps ({
        "description": "课表" ,
        "name": "课程"
    })
    # print('json_data=',json_data)
    post_req = requests.post (config.base_url + '/knowledge/' , data=json_data , headers=req_headers)
    print (post_req.text)


if __name__ == '__main__':
    # unittest.main()
    post_knowledge ()
