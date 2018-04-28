import requests
import json
import unittest
from base.reqeusts_headers import *
from model.get_json_model import *
import config


class KnowledgeController (unittest.TestCase):

    def setUp ( self ):
        self.url = config.base_url + '/knowledge/'
        self.headers = req_headers
    def tearDown(self):
        pass

    def test_post_knowledge ( self ):
        model_file_name = 'models'
        # model_sheet = 'PostKnowledgeModel'
        model_sheet = 'posttest'
        testdata_file_name = 'testdata'
        # testdata_sheet = 'PostKnowledgeData'
        testdata_sheet = 'posttest'

        knowledge_model = get_json_model (model_file_name , model_sheet , testdata_file_name , testdata_sheet)
        model_index = random.randint (0 , len (knowledge_model))
        print('model_index=',model_index)
        knowledge_json = json.dumps (knowledge_model[model_index])
        print('json=',knowledge_json)
        post_req = requests.post (self.url , data=knowledge_json , headers=req_headers)
        print(post_req)




if __name__ == '__main__':
    unittest.main()



