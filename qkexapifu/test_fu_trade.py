# -*- coding: utf-8 -*-
import allure
import json
import requests
from qkexapifu.logutil import Logsv
logger = Logsv()


url = "http://localhost:9999/v1/admin/manager/action/record/page?startDate=202304210000&endDate=202306301600&conditionUid=10122479"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'source': 'api',
  'Accept-Language': 'zh-CN',
  'X-Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxYTEzZTNlMi1kOGMzLTQ3MzYtYmMwOS0yOTJiMzBhNWIzOWMiLCJ1aWQiOiJDbVp5QzdaV0thUTZEaHlRQ2NlSmh3PT0iLCJiaWQiOiJXWFAxUS8xa2s5NVQxTjRxOWxuSFRBPT0iLCJpcCI6IkdwdHl4M01ZbzBJemNsL3pwN0ZiNXc9PSIsImRldiI6InAva3BIckF3RkJjSUZleXg0U2xkZGc9PSIsInN0cyI6MCwiaWF0IjoxNjcyNTAyNDAwLCJleHAiOjE3MDEzNjAwMDAsImlzcyI6InFrZXgifQ.lcBeU_9i80bo-RA3TfrK4C8P8eSYl-0HzwI8NYSamqU'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
