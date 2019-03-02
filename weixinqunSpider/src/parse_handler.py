# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from . import container
from . import spider
from .logger import Log

class qunInfo():
    def __init__(self, url, title):
        self.url = url
        self.title = title
        self.description = ""
        self.hangye = ""
        self.district = ""
        self.buildTime = ""
        self.tags = ""
        self.weixinhao = ""
        self.imgUrl = ""
        self.imgPath = ""


def parse(QunObj):
    QunInfoObj = qunInfo(QunObj.url,QunObj.title)

    soup = BeautifulSoup(QunObj.htmlStr,features="lxml")
    # 以下未做错误处理
    desc = soup.select("div.des_info > div.clearfix > ul > li")[2].select_one("span").text.strip()
    otherInfo = soup.select_one("div.des_info > div.clearfix > ul > ul.other-info")
    hangye = otherInfo.select("> li")[0].select_one("a").text.strip()
    district = otherInfo.select("> li")[1].select_one("a").text.strip()
    buildTime = otherInfo.select("> li")[2].text.strip().split(" ",1)[1].lstrip()
    tags = otherInfo.select("> li")[3].text.strip().split(" ",1)[1].lstrip()
    weixinhao = soup.select("div.des_info > div.clearfix > ul > li")[3].select("span")[1].text.strip()
    imgUrl = soup.select("span.shiftcode > img")[0].attrs["src"]

    QunInfoObj.description = desc
    QunInfoObj.hangye = hangye
    QunInfoObj.district = district
    QunInfoObj.buildTime = buildTime
    QunInfoObj.tags = tags
    QunInfoObj.weixinhao = weixinhao
    QunInfoObj.imgUrl = imgUrl

    Log("system").debug("parse QunObj succ, url:{}".format(QunInfoObj.url))
    return QunInfoObj



