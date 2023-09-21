# -*- coding: utf-8 -*-
import subprocess
from time import sleep

import requests
import os

# 要搜索的文件名
filename = "qkqk.ovpn"
filepath = ""
# 搜索文件
for root, dirs, files in os.walk('C:\\qkex20230901\\qkexapifu'):
    if filename in files:
        filepath = os.path.join(root, filename)
        print("找到文件:", filepath)
        break

else:
    print("未找到指定文件:", filename)

# VPN 配置和登录信息（请根据实际情况进行修改）
vpn_config_file = filepath
print(vpn_config_file)
vpn_username = "yaocansen"
vpn_password = "Yaocansen@123"
vpn_gateway_url = "122.9.208.76"

login_url = "https://test-public-rest.qkex.com"
username = "yaocansen708@gmail.com"
password = "Asdf@1234.com"
verifyCode = '111111'
path='/user/logi'
# # 启动 VPN 连接n'
# univpn_executable = r'C:\Program Files (x86)\UniVPN\UniVPN.exe'
# vpn_process = subprocess.Popen([univpn_executable, 'connect', 'vpn_config_file'], stdout=subprocess.PIPE)
# sleep(10)
# 列出通过 VPN 连接的网络接口
list_interfaces_command = "ipconfig"
interfaces_output = subprocess.check_output(list_interfaces_command)
interfaces_output = interfaces_output.decode("gbk") # 使用 gbk 编码解码接口输出

print(interfaces_output)

# 获取 VPN 网络接口名称
vpn_interface = ""
for line in interfaces_output.split("\n"):
    if "SSTAP" in line:
        vpn_interface = line.split(":")[0]
        break

# 检查是否成功连接到 VPN
if vpn_interface:
    print("VPN 已连接，接口名称:", vpn_interface)
else:
    print("无法连接到 VPN")

# 构建登录请求
payload = {
    "username": username,
    "password": password,
    "verifyCode": verifyCode
}
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
           "Accept": "application/json, text/plain, */*",
           "Content-Type": "application/json",
           "Connection": "close",
           "Accept-Language": "zh-CN",
           "language": "zh-CN",
           "Cookie": "_gid=GA1.2.202881581.1694662746; _ga=GA1.1.807430899.1693379699; _ga_BC2SP908YM=GS1.1.1694727723.20.1.1694727724.0.0.0",
           "X-Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkZWY0NWEwNS02ZWE1LTQzMzUtOGQ2Ni0zMDUzYjUyNmRhNmM3Mjk4MDkwNTAiLCJ1aWQiOiJ2ZnFnbFMxNkdRQmd4Sk5yTHhKZExBPT0iLCJiaWQiOiJtV09PN0YyenNOMFR3UkF5UURsaytBPT0iLCJpcCI6IjR2WHh5NW5xU3Q0VVF6aDhmdno1cmc9PSIsImRldiI6IkE4b0xOZVJWdkZHb3hMOVBaZWhrcEE9PSIsInN0cyI6MCwiaWF0IjoxNjk0NjYyNjEyLCJleHAiOjE2OTQ3NDkwMTIsImlzcyI6IndjcyJ9"
           }
sleep(5)
# 发送登录请求
response = requests.post(login_url+path, json=payload, headers=headers, verify=False)

# 解析登录响应
if response.status_code == 200:
    # 提取返回的 token
    token = response.json().get("token")
    if token:
        print("成功获取 Token:", token)
    else:
        print("登录成功，但未获取到 Token")
else:
    print("登录失败，HTTP 错误码:", response.status_code)

# 断开 VPN 连接
# vpn_process.terminate()