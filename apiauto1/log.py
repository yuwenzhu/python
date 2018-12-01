# import logging
# from logging.handlers import RotatingFileHandler
# import threading
# from apiauto.day8.testdata.getpath import GetTestLogPath
# class LogSignleton(object):
# 	def __init__(self):
# 		pass
# 	def __new__(cls):
# 		mutex = threading.Lock()
# 		mutex.acquire() # 上锁，防止多线程下出问题
# 		if not hasattr(cls, 'instance'):
# 			cls.instance = super(LogSignleton, cls).__new__(cls)
# 			cls.instance.log_filename = GetTestLogPath()
# 			cls.instance.max_bytes_each = 51200
# 			cls.instance.backup_count = 10
# 			cls.instance.fmt = "|(asctime)s |(filename)s[line: |(lineno)d] |(levelname)s: |(message)s"
# 			cls.instance.log_level_in_console = 10
# 			cls.instance.log_level_in_logfile = 20
# 			cls.instance.logger_name = "test_logger"
# 			cls.instance.console_log_on = 1#屏幕输出1、0
# 			cls.instance.logfile_log_on = 1#文件输出
# 			cls.instance.logger = logging.getLogger(cls.instance.logger_name)
# 			cls.instance.__config_logger()
# 		mutex.release()
# 		return cls.instance
# 	def get_logger(self):
# 		return self.logger
#
# 	def __config_logger(self):
# 	# 设置日志格式
# 		fmt = self.fmt.replace('|', '%')
# 		formatter = logging.Formatter(fmt)
# 		if self.console_log_on == 1: # 如果开启控制台日志
# 			console = logging.StreamHandler()
# 			console.setFormatter(formatter)
# 			self.logger.addHandler(console)
# 			self.logger.setLevel(self.log_level_in_console)
# 		if self.logfile_log_on == 1: # 如果开启文件日志
# 			rt_file_handler = RotatingFileHandler(
# 			self.log_filename, maxBytes=self.max_bytes_each, backupCount=self.backup_count)
# 			rt_file_handler.setFormatter(formatter)
# 			self.logger.addHandler(rt_file_handler)
# 			self.logger.setLevel(self.log_level_in_logfile)
# logsignleton = LogSignleton()
# logger = logsignleton.get_logger()
# # logger.info('info')

import logging
from logging.handlers import RotatingFileHandler
import threading
from testdata.getpath import GetTestLogPath
import configparser
from testdata.getpath import GetTestConfig

class LogSignleton(object):
    def __init__(self):
        pass

    def __new__(cls):
        config = configparser.ConfigParser()
        config.read(GetTestConfig('logconfig.conf'),encoding='utf-8-sig')
        LOGGING = 'LOGGING'
        mutex = threading.Lock()
        mutex.acquire() # 上锁，防止多线程下出问题
        if not hasattr(cls, 'instance'):
            cls.instance = super(LogSignleton, cls).__new__(cls)
            cls.instance.log_filename = GetTestLogPath()
            cls.instance.max_bytes_each = config['LOGGING']['max_bytes_each']
            cls.instance.backup_count = config['LOGGING']['backup_count']
            # print(cls.instance.backup_count)
            cls.instance.fmt = config['LOGGING']['fmt']
            cls.instance.log_level_in_console = config['LOGGING']['log_level_in_console']
            cls.instance.log_level_in_logfile = config['LOGGING']['log_level_in_logfile']
            cls.instance.logger_name = config['LOGGING']['logger_name']
            cls.instance.console_log_on = config['LOGGING']['console_log_on']
            cls.instance.logfile_log_on = config['LOGGING']['logfile_log_on']
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()
        mutex.release()
        return cls.instance

    def get_logger(self):
        return self.logger

    def __config_logger(self):

        # 设置日志格式
        fmt = self.fmt.replace('|', '%')
        formatter = logging.Formatter(fmt)
        if self.console_log_on == 1:  # 如果开启控制台日志
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            self.logger.setLevel(self.log_level_in_console)
        if self.logfile_log_on == 1:  # 如果开启文件日志
            rt_file_handler = RotatingFileHandler(
            self.log_filename, maxBytes=self.max_bytes_each, backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)
            self.logger.setLevel(self.log_level_in_logfile)
logsignleton = LogSignleton()
logger = logsignleton.get_logger()

# logger.error('error')