import logging
from datetime import datetime
import os


class RecordLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # # 将log日志输入到文件中
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join("../logs")

        # 日志名构建
        log_file_name = datetime.now().strftime("%Y-%m-%d") + '.log'
        log_file_path = log_dir + "/" + log_file_name

        # 日志写进log文件中
        # 创建日志器
        self.file_handle = logging.FileHandler(log_file_path,'a', encoding='utf-8')
        # 设置日志格式
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s %(levelno)s: [%(levelname)s] ----->%(message)s'
        )
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    r1 = RecordLog()
    log_info = r1.get_log()
    log_info.debug("test1")
    r1.close_handle()