# -*- coding:utf-8 -*-

import os
import logging

BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))

BASE_URL = "https://www.weixinqun.com"
INDEX_URL = "https://www.weixinqun.com/group"


# 可修改为rabbitMQ
CONTAINER = "memory"


# 日志配置
LOG_LEVEL = logging.DEBUG
LOG_TYPES = {
    'system': 'system.log',
    'error':"error.log"
}

# 图片存放文件夹，这里写死了，指向api的static/imgs
IMGS_DIR = os.path.join("D:\Python相关\过程project\weixinqunBackend\static\imgs")


# qunInfo发送到该api进行数据库导入
BACKEND_QUN_INFO_API = "http://127.0.0.1:8000/api/quns/"