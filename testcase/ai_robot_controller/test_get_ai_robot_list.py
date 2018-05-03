import unittest
import paramunittest
from base import read_config
from common import log
from common import config_http
from common import read_excel

ai_robot_list_xls = read_excel.get_value_in_order ('ai_robot_testdata' , 'GetAiRobotList')
local_read_config = read_config.ReadConfig ()
local_config_http = config_http.ConfigHttp()
info = {}


@paramunittest.parametrized (*ai_robot_list_xls)
class GetAiRobotList (unittest.TestCase):
    def set_parameters ( self , case_name , method , result , code , msg ):
        """
        set params
        :param case_name:
        :param method:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str (case_name)
        self.method = str (method)
        self.result = str (result)
        self.code = str (code)
        self.msg = str (msg)
        self.info = None

    def description ( self ):
        """
        :return:
        """
        self.case_name

    def setUp ( self ):
        """
        :return:
        """
        self.log = log.MyLog.get_log ()
        self.logger = self.log.get_logger ()

    def test_get_ai_robot_list ( self ):
        """
        :return:
        """
        # set url
        self.url = ''
        local_config_http.set_url(self.url)
        # set params



if __name__ == '__main__':
    unittest.main()