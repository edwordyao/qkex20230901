# -*- coding: utf-8 -*-
from logging.handlers import RotatingFileHandler
from qkex_mon_ui.project_path import get_project_path
import colorlog, datetime, logging, time, os
log_path = get_project_path() + '\\logs'
if not os.path.exists(log_path):
    os.mkdir(log_path)
log_name = os.path.join(log_path, '%s.Logs' % time.strftime('%Y-%m-%d'))
log_colors_config = {
 'DEBUG': "'cyan'",
 'INFO': "'green'",
 'WARNING': "'yellow'",
 'ERROR': "'red'",
 'CRITICAL': "'red'"}

class Logsv(object):

    def __init__(self, logName=log_name):
        self.logName = logName
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.formatter = colorlog.ColoredFormatter('%(log_color)s[%(asctime)s] [%(levelname)s]- %(message)s',
          log_colors=log_colors_config)

    @staticmethod
    def get_file_sorted(file_path):
        """最后修改时间顺序升序排列 os.path.getmtime()->获取文件最后修改时间"""
        dir_list = os.listdir(file_path)
        if not dir_list:
            return
        dir_list = sorted(dir_list, key=(lambda x: os.path.getmtime(os.path.join(file_path, x))))
        return dir_list

    @staticmethod
    def TimeStampToTime(timestamp):
        """格式化时间"""
        timeStruct = time.localtime(timestamp)
        return str(time.strftime('%Y-%m-%d', timeStruct))

    @staticmethod
    def delete_logs(file_path):
        try:
            os.remove(file_path)
        except PermissionError as e:
            try:
                Logsv().warning('删除日志文件失败：{}'.format(e))
            finally:
                e = None
                del e

    def handle_logs(self):
        """处理日志过期天数和文件数量"""
        dir_list = [
         'logs']
        for dir in dir_list:
            dirPath = get_project_path() + '\\' + dir
            file_list = self.get_file_sorted(dirPath)
            if file_list:
                for i in file_list:
                    file_path = os.path.join(dirPath, i)
                    t_list = self.TimeStampToTime(os.path.getctime(file_path)).split('-')
                    now_list = self.TimeStampToTime(time.time()).split('-')
                    t = datetime.datetime(int(t_list[0]), int(t_list[1]), int(t_list[2]))
                    now = datetime.datetime(int(now_list[0]), int(now_list[1]), int(now_list[2]))
                    if (now - t).days > 10:
                        self.delete_logs(file_path)

    def __console(self, level, message):
        fh = RotatingFileHandler(filename=(self.logName), mode='a', maxBytes=5242880, backupCount=5, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        ch = colorlog.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        else:
            if level == 'debug':
                self.logger.debug(message)
            else:
                if level == 'warning':
                    self.logger.warning(message)
                else:
                    if level == 'error':
                        self.logger.error(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)
if __name__ == '__main__':
    log = Logsv()
    log.debug('---测试开始----')
    log.info('操作步骤')
    log.warning('----测试结束----')
    log.error('----测试错误----')
    log.handle_logs()