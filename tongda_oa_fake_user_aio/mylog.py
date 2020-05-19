# -*- coding: utf-8 -*-
import sys,os
from loguru import logger

def mylogger(flag=None):
    """
    Log日志，如果传入Flag值就保存为log文件，否则默认不保存文件
    :param flag:
    :return:
    """
    BaseDir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(BaseDir,"debug.log")
    err_log_path = os.path.join(BaseDir,"error.log")

    logfile_fmt = '<light-green>{time:YYYY/MM/DD HH:mm:ss}</light-green> - ' \
              '[<level>{level: <5}</level>] - ' \
              '<level>{message}</level>'

    logger.remove()
    logger.add(sys.stdout,colorize=True,enqueue=True, format="<green>{time:MM/DD HH:mm:ss}</green> - <level>{level}</level> - <level>{message}</level>")
    if flag:
        logger.add(log_file_path,format=logfile_fmt,enqueue=True,encoding="utf-8")
        logger.add(err_log_path,format=logfile_fmt,enqueue=True,encoding="utf-8",level="ERROR")
    return logger

if __name__ == "__main__":
    
    mylogger().info("123")
    mylogger().debug(456)
    mylogger().error(789)
    mylogger().success(890)