# -*- coding:utf-8 -*-
import logging
from conf import settings

def logger(log_type):
    # create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    # create file handler and set level to warning
    log_file = "%s/logs/%s" % (settings.BASE_DIR, settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to logger
    logger.addHandler(ch)  #  #logger对象可以添加多个fh和ch对象
    logger.addHandler(fh)

    return logger

def Log(logType):
    if logType == "system":
        return system_log
    if logType == "error":
        return error_log

system_log = logger("system")
error_log = logger("error")

