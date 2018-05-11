from common.common_info import *
import requests
import logging
import json


# from base.Log import MyLog as Log


class ConfigHttp:
    def __init__ ( self ):
        self.url = None
        self.headers = {}
        self.params = {}
        self.data = {}
        # self.log = Log.get_log ()
        # self.logger = self.log.get_logger ()

    def set_url ( self , url ):
        self.url = base_url + '/' + url

    def set_headers ( self , headers ):
        self.headers = headers

    def set_params ( self , param ):
        self.params = param

    def set_data ( self , data ):
        self.data = data

    def post ( self ):
        try:
            resopnse = requests.post (self.url , data=self.data , headers=self.headers)
            return resopnse
        except TimeoutError as e:
            logging.error ('Time Out!')
            return None


if __name__ == '__main__':
    print ('config_http')
    url = 'http://10.75.2.121:9200/api/qa'
    headers = {'Content-Type': 'application/json' , 'Accept': 'application/json'}
    data = json.dumps ({
        "question": '请问怎么选课' ,
        "aiRobotId": 175 ,
    })
    configHttp = ConfigHttp ()
    configHttp.set_url (url)
    configHttp.set_headers (headers)
    configHttp.set_data (data)
    result = configHttp.post ()
    print ('result=' , result)
