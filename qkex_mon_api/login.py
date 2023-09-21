from time import sleep

import requests
url = "https://public-rest.qkex.com/user/login"
headers = {
    "authority": "public-rest.qkex.com",
    "accept": "application/json",
    "accept-language": "zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "cookie": "_ga=GA1.1.807430899.1693379699; locale=zh-HK; _ga_BC2SP908YM=GS1.1.1695175053.31.1.1695175624.0.0.0",
    "origin": "https://www.qkex.com",
    "referer": "https://www.qkex.com/",
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "x-lang": "zh-HK",
    "x-locale": "zh-HK"
}
data = {
    "account": "san2070@gmail.com",
    "password": "aa123456",
    "verifyCode": "057178"
}

response = requests.post(url, headers=headers, json=data, verify=False)
print(response.json())  # 打印登录请求的返回结果

url = "https://www.qkex.com/"
headers = {
    "authority": "www.qkex.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "_ga=GA1.1.807430899.1693379699; locale=zh-HK; _ga_BC2SP908YM=GS1.1.1695175053.31.1.1695175624.0.0.0; token=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4MGI5ODlkMy02NTAyLTQwMDktYjJiOS0yOTNmNWYwZDJmMjc0NTc3MDUyNjMiLCJ1aWQiOiJaVHd2V1Q0SVRBWkt3N3ltbnc1MHlnPT0iLCJiaWQiOiJtV09PN0YyenNOMFR3UkF5UURsaytBPT0iLCJpcCI6Iks4L2Zia0plVWZFNUZZMFFsM1V0Wnc9PSIsImRldiI6IkE4b0xOZVJWdkZHb3hMOVBaZWhrcEE9PSIsInN0cyI6MCwiaWF0IjoxNjk1MTc1NjQ3LCJleHAiOjE2OTUyNjIwNDcsImlzcyI6IndjcyJ9.6V9LvpY2BOb5qScAwJVFeEGiz71mB68gu3mtVkwuU0k",
    "if-modified-since": "Thu, 14 Sep 2023 10:27:34 GMT",
    "referer": "https://www.qkex.com/",
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers, verify=False)
print(response.text)  # 打印获取 Token 请求的返回结果
token = response.text.get("accessToken")
print(token)
