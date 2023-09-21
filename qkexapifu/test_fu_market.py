# -*- coding: utf-8 -*-
import allure
import json
import requests
from qkexapifu.logutil import Logsv
logger = Logsv()


url = "https://test-futures-rest.qkex.com/v1/market/depth?tradeType=linearPerpetual&symbol=BTCUSDT&limit=1000&gear=0.1"

payload = {}
headers = {
  'source': 'api',
  'Accept-Language': 'zh-CN',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
