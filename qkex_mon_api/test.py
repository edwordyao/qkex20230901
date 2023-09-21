import requests
import json

url = "https://public-rest.qkex.com/foundation/indexes/exchange-rate"

payload = ""
headers = {
   'authority': 'public-rest.qkex.com',
   'source': 'web',
   'x-authorization': '',
   'x-lang': 'en',
   'x-locale': 'en-US',
   'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.0.1693296055.0.0.0',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'content-type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)