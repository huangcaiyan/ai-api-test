import requests
from base import read_config
from .log import MyLog as Log
import os

local_read_config = read_config.ReadConfig ()


class ConfigHttp:
    def __init__ ( self ):
        global host , port , timeout
        host = local_read_config.get_http ('base_url')
        port = local_read_config.get_http ('port')
        timeout = local_read_config ('timeout')
        self.log = Log.get_log ()
        self.logger = self.log.get_logger ()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_url ( self , url ):
        """
        :param url:
        :return:
        """
        self.url = host + url

    def set_headers ( self , header ):
        """
        :param header:
        :return:
        """
        self.headers = header

    def set_params ( self , param ):
        """
        :param param:
        :return:
        """
        self.params = param

    def set_files ( self , filename ):
        """
        set upload files
        :param filename:
        :return:
        """
        if filename != '':
            file_path = os.path.abspath (os.path.dirname (__file__) + '/../..') + filename
            self.files = {'file': open (file_path , 'rb')}
        if filename == '' or filename is None:
            self.state = 1

    # defined http get method
    def get ( self ):
        """
        defined get method
        :return:
        """
        try:
            response = requests.get (self.url , headers=self.headers , params=self.params , timeout=float (timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error ('Time out!')
            return None

    def post ( self ):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post (self.url , headers=self.headers , params=self.params , data=self.data ,
                                      timeout=float (timeout))
            return response
        except TimeoutError:
            self.logger.error ('Time out!')
            return None

    def post_with_file ( self ):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post (self.url , headers=self.headers , data=self.data , files=self.files ,
                                      timeout=float (timeout))
            return response
        except TimeoutError:
            self.logger.error ("Time out!")
            return None

    def post_with_json ( self ):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post (self.url , headers=self.headers , json=self.data , timeout=float (timeout))
            return response
        except TimeoutError:
            self.logger.error ("Time out!")
            return None

if __name__ == '__main__':
    print('config http')