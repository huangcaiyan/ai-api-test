import unittest
from .knowledge_controller import *


class KnowledgeControllerSpec (unittest.TestCase):

    def setUp ( self ):
        self.url = config.base_url + '/knowledge/'
        self.headers = req_headers
    def tearDown(self):
        pass

    def test_post_knowledge ( self):
        url = config.base_url + '/knowledge/'
        model_file_name = 'models'
        model_sheet = 'PostKnowledgeModel'
        testdata_file_name = 'testdata'
        testdata_sheet = 'PostKnowledgeData'
        result = post_knowledge(url,model_file_name,model_sheet,testdata_file_name,testdata_sheet)
        self.assertIn('200',result)
    # def get_knowledge_list( self ):





if __name__ == '__main__':
    unittest.main()



