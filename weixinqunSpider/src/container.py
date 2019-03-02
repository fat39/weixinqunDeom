# -*- coding:utf-8 -*-

from queue import Queue
from conf import settings

# rabbitmq存放群网页
class rabbitMQContainer():
    pass


# 内存存放群网页
class memoryContainer():
    def __init__(self):
        self.storage = Queue()

    def putQunObj(self,QunObj):
        self.storage.put(QunObj)

    def getQunObj(self):
        try:
            # QunObj = self.storage.get()
            QunObj = self.storage.get_nowait()
            return QunObj
        except:
            return


class container():
    @classmethod
    def getContainer(self):
        if settings.CONTAINER == "memory":
            return memoryContainer()
        if settings.CONTAINER == "rabbitMQ":
            return rabbitMQContainer()


Container = container.getContainer()