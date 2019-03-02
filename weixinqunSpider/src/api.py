# -*- coding:utf-8 -*-

import requests
import json

def postToApi(url,obj):
    res = requests.post(url,data=obj.__dict__)
    print(res)

