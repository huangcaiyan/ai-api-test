import os
from base import read_config
import logging
from datetime import datetime
import threading

localReadConfig = read_config.ReadConfig()


class Log:
    def __init__(self):
        global log_path, result_path, pro_dir
        pro_dir = read_config.pro_dir
        result_path = os.path.join(pro_dir, "result")
        if not os.path.exists(result_path):
            os.mkdir(result_path)
        log_path = os.path.join(result_path, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # defined handler
        handler = logging.FileHandler(os.path.join(log_path, "output.log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """
        self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)

    def get_report_path(self):
        """
        get report file path
        :return:
        """
        report_path = os.path.join(log_path, "report.html")
        return report_path

    def get_result_path(self):
        """
        get test result path
        :return:
        """
        return log_path

    def write_result(self, result):
        """

        :param result:
        :return:
        """
        result_path = os.path.join(log_path, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            logger.error(str(ex))


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")

