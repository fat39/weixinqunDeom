# -*- coding:utf-8 -*-
from . import spider
from . import container
from . import parse_handler
from .logger import Log
from . import api
from conf import settings


def run():
    # 开启爬虫
    spider.run()

    # 从container获取obj，并解析出目标数据
    while True:
        # 先写非并发的，因此不能卡在这

        QunObj = container.Container.getQunObj()
        if not QunObj:
            break

        # 解析获取群信息
        QunInfoObj = parse_handler.parse(QunObj)

        # 下载照片，保存路径
        spider.ImgDownload(QunInfoObj)
        Log("system").debug("parse QunObj imgPath succ, path:{}".format(QunInfoObj.imgPath))

        # 发到api
        api.postToApi(settings.BACKEND_QUN_INFO_API,QunInfoObj)



