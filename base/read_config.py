import os
import codecs
import configparser

pro_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(pro_dir,'config.ini')

class ReadConfig:
    def __init__(self):
        fd = open(config_path)
        data = fd.read()

        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(config_path,'w')
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_email( self,name ):
        value = self.cf.get('EMAIL',name)
        return value

    def get_http( self,name ):
        value= self.cf.get('HTTP',name)
        return value

    def gt_db( self,name ):
        value = self.cf.get('DATABASE',name)
        return value
    