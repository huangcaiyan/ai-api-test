import requests
import json

url = 'http://10.75.2.121:9200/api/qa'


def get_question ():
    headers = {'Content-Type': 'application/json' , 'Accept': 'application/json'}
    s = json.dumps ({"question": '开学典礼什么时候开始？' ,
                     "aiRobotId": 175 , })
    response = requests.post (url , data=s , headers=headers)
    response_text = json.loads (response.text)
    code = response_text['code']
    msg = response_text['msg']
    print (code)
    print (response_text['data'])
    print(msg)
    print (response_text)


if __name__ == '__main__':
    get_question ()
