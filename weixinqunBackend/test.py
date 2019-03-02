# -*- coding:utf-8 -*-

import requests
import json

url = "http://127.0.0.1:8000/api/quns/"

htm = requests.get(url)

res = json.loads(htm.text)
for qun in res:
    print(type(qun),qun)