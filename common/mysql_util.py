import traceback
import sys
import pymysql
import os

test_result_dir = os.path.dirname (__file__) + '../../test_runner/report/mysql_util_testlog.txt'


class MysqlUtil (object):
    def __init__ ( self ):
        pass

    @staticmethod
    def get_connect ():
        db = pymysql.connect (host='10.75.2.178' , port=3306 , user='root' , password='SunLand2@' ,
                              db='sscp_test' ,
                              charset='utf8mb4' , cursorclass=pymysql.cursors.DictCursor)
        return db

    # 查询数据库表：单个结果集
    def fetchone ( self , sql ):
        db = self.get_connect ()
        cursor = db.cursor ()
        try:
            cursor.execute (sql)
            result = cursor.fetchone ()
        except:
            # 用traceback 查看异常
            traceback.print_exc ()
            db.rollback ()
        finally:
            db.close ()
        return result

    # 查询数据库表：多个结果集
    def fetchall ( self , sql ):
        db = self.get_connect ()
        cursor = db.cursor ()
        try:
            cursor.execute (sql)
            result = cursor.fetchall ()
            result_value = []
            for data in result:
                for value in data.values ():
                    result_value.append (value)
        except:
            # 用sys模块回溯最后的异常并输出异常信息
            info = sys.exc_info ()
            print (info[0] , ':' , info[1])
            db.rollback ()
        finally:
            db.close ()
        return result_value


if __name__ == '__main__':
    fetchall_sql = "select question from ai_question"
    sqlUtil = MysqlUtil ()
    result = sqlUtil.fetchall (fetchall_sql)
    print ('result=' , result)
