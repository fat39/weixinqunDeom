# -*- coding:utf-8 -*-

import requests
from conf import settings
from bs4 import BeautifulSoup
from . import container
from .logger import Log
import os


class oneQun:
    def __init__(self, url, title):
        self.url = url
        self.title = title
        self.htmlStr = ""

    def __str__(self):
        return "url:{} title:{}".format(self.url,self.title)

class qunMgr:
    def __init__(self):
        # 这里不会被消费，因此所有QunObj都在，占空间，可优化，比如使用set只记录url，把其他信息进行消费
        self.qunsDict = dict()

    def addQun(self, url, title):
        # 先假定所有url只能遇见一次
        qunObj = oneQun(url, title)
        self.qunsDict[url] = qunObj

    def crawlAllQun(self):
        # TODO 并发爬取
        for url,QunObj in self.qunsDict.items():
            Log("system").info("crawl qun index [{}] succ".format(url))
            self.crawlOneQun(QunObj)

            # 先爬一个群
            # break

    def crawlOneQun(self,QunObj):
        # 爬取还没爬的
        if not QunObj.htmlStr:
            targetUrl = "{}{}".format(settings.BASE_URL,QunObj.url)
            htm = requests.request("get", targetUrl)
            QunObj.htmlStr = htm.text

        # 放到container里，可以是rabbitMQ，可以是memory。
        container.Container.putQunObj(QunObj)


def ImgDownload(QunInfoObj):
    url = QunInfoObj.imgUrl
    htm = requests.get(url)
    imgName = url.rsplit("/",1)[1]
    imgPath = "{}/{}".format(settings.IMGS_DIR,imgName)
    if not os.path.isfile(imgPath):
        with open(imgPath, "wb") as f:
            f.write(htm.content)
        Log("system").debug("download img[{}] succ".format(url))

    QunInfoObj.imgPath = imgPath


def run():
    # 获取一页，"https://weixinqun.com/group"  # 可考虑获取网页数量再循环去crawl，也可以逐步获取下一页
    htm = requests.request("get", settings.INDEX_URL)
    Log("system").info("crawl qun list[{}] succ".format(settings.INDEX_URL))

    soup = BeautifulSoup(htm.text, features="lxml")
    # 从页面中获取目标atag
    aTagList = soup.select("ul#tab_head li p.goods_name a")

    # 遍历aTagList
    for index, aTag in enumerate(aTagList):
        QunMgrObj.addQun(aTag.attrs["href"], aTag.attrs["title"])

    QunMgrObj.crawlAllQun()


QunMgrObj = qunMgr()

if __name__ == '__main__':
    run()
