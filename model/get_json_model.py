# coding:utf8
from util.read_excel import *
import random
import json


def get_json_model ( model_file_name , model_sheet , testdata_file_name , testdata_sheet , ):
    """
    :param model_file_name: model file name
    :param model_sheet:  model sheet_name or sheet_index
    :param testdata_file_name: testdata file name
    :param testdata_sheet: testdata sheet_name or sheet_index
    # :param testdata_row_mun: testdata row num
    :return: lsit([{'key':'value','key':'value'...},{'key':'value'...}])
    """
    payloads = []
    model_values = get_value_in_order (model_file_name , model_sheet)
    testdata_values = get_value_in_order (testdata_file_name , testdata_sheet)
    model_names = []
    unique_index = 0
    print ('testdata_values=' , testdata_values)
    for i in range (0 , len (model_values)):
        model_name = model_values[i][0]
        model_names.append (model_name)
        if model_values[i][3] == 'y':
            unique_index = i
            print (unique_index)
    for j in range (0 , len (testdata_values)):
        payload_item = {}
        for k in range (0 , len (model_names)):
            if k == unique_index:
                testdata_u = testdata_values[j][k] + str (random (0 , 10000))
                payload_item[model_names[k]] = testdata_u
                print (payload_item)
            payload_item[model_names[k]] = testdata_values[j][k]
        payloads.append (payload_item)
    print ('payloads=' , payloads)
    return payloads


if __name__ == '__main__':
    model_file_name = 'models'
    testdata_file_name = 'testdata'
    model_sheet = 'PostKnowledgeModel'
    testdata_sheet = 'PostKnowledgeData'
    row_num = 1
    print (get_json_model (model_file_name , model_sheet , testdata_file_name , testdata_sheet).text)