from appium import webdriver
import requests
import unittest
import time
from selenium.webdriver.common.by import By
import os
import allure
import pytest
from pytest_testconfig import config
# @allure.environment(OPERATING_SYSTEM="Windows", BROWSER="Chrome", PYTHON_VERSION="3.8.10"

# @allure.feature('首页接口api')
class Testmonqkex():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "dev"
        caps["udid"] = "127.0.0.1:5555"
        caps["appPackage"] = "com.qkex.dev"
        caps["appActivity"] = "com.coin.ex.main.SplashActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        caps["skipDeviceInitialization"] = "true"
        caps["dontStopAppOnReset"] = "true"
        caps["unicodeKeyBord"] = "true"
        caps["resetKeyBord"] = "true"
        caps['app'] = f'{os.path.abspath(os.curdir)}/app/QKEx_dev_3.0.15-dev.apk'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
        self.clickupdate()


    def teardown(self):
        self.driver.quit()

    def clickupdate(self):
        el1 = self.driver.find_element(By.XPATH,
        "/hierarchy/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView")
        if el1 is None:
            pass
        else:
            el1.click()

    def test_clickspots(self):
        el2 = self.driver.find_element(By.ID, "com.qkex.dev:id/ll_coin")
        el2.click()

    # def test_api_sy_exchange(self):
    #     r = requests.get("https://public-rest.qkex.com/foundation/indexes/exchange-rate", headers={"authority": "public-rest.qkex.com", "content-type": "application/json", "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.0.1693296055.0.0.0", "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_instruments(self):
    #     r = requests.get("https://futures-rest.qkex.com/v1/public/web/instruments?tradeType=linearPerpetual", headers={"authority": "futures-rest.qkex.com", "content-type": "application/json", "cookie": "_ga=GA1.1.1569607884.1692244572; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_favorite(self):
    #     r = requests.get("https://public-rest.qkex.com/exchange/favorite/list",
    #                      headers={"authority": "public-rest.qkex.com", "content-type": "application/json",
    #                               "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "x-authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ",
    #                               "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_user_balance(self):
    #     r = requests.get("https://public-rest.qkex.com/wallet/user-balance",
    #                      headers={"authority": "public-rest.qkex.com", "content-type": "application/json",
    #                               "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "x-authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ",
    #                               "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_currencies(self):
    #     r = requests.get("https://public-rest.qkex.com/wallet/currencies",
    #                      headers={"authority": "public-rest.qkex.com", "content-type": "application/json",
    #                               "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "x-authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ",
    #                               "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_assets(self):
    #     r = requests.get("https://public-rest.qkex.com/exchange/assets",
    #                      headers={"authority": "public-rest.qkex.com", "content-type": "application/json",
    #                               "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "x-authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ",
    #                               "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_icons(self):
    #     r = requests.get("https://public-rest.qkex.com/exchange/public/currency/icons", headers={"authority": "public-rest.qkex.com", "content-type": "application/json", "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_queryRate(self):
    #     r = requests.get("https://public-rest.qkex.com/exchange/public/queryRate/BTC", headers={"authority": "public-rest.qkex.com", "content-type": "application/json", "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_kyc_status(self):
    #     r = requests.get("https://public-rest.qkex.com/user/kyc/kyc-status",
    #                      headers={"authority": "public-rest.qkex.com", "content-type": "application/json",
    #                               "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "x-authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ",
    #                               "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_detail(self):
    #     r = requests.get("https://public-rest.qkex.com/user/detail",
    #                      headers={"authority": "public-rest.qkex.com", "content-type": "application/json",
    #                               "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "x-authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ",
    #                               "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_riskWarning(self):
    #     r = requests.get("https://public-rest.qkex.com/user/public/riskWarning",
    #                      headers={"authority": "public-rest.qkex.com", "content-type": "application/json",
    #                               "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "x-authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ",
    #                               "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_otc_advertiser_type(self):
    #     r = requests.get("https://public-rest.qkex.com/otc/advertiser/type",
    #                      headers={"authority": "public-rest.qkex.com", "content-type": "application/json",
    #                               "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "x-authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ",
    #                               "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_banners(self):
    #     r = requests.get("https://public-rest.qkex.com/foundation/cms/banners",
    #                      headers={"authority": "public-rest.qkex.com", "content-type": "application/json",
    #                               "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "x-authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ",
    #                               "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
    #
    # def test_api_sy_news(self):
    #     r = requests.get("https://public-rest.qkex.com/foundation/cms/news",
    #                      headers={"authority": "public-rest.qkex.com", "content-type": "application/json",
    #                               "cookie": "_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0", "x-authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ",
    #                               "source": "web", "x-lang": "en", "x-locale": "en-US"})
    #     print(r.json())
    #     assert r.status_code == 200
if __name__ == '__main__':
    pytest.main()
    # os.system('allure generate ./result1/ -o ./result1/ --clean')
    # os.system('allure serve ./resuit1/')
# if __name__ == '__main__':
#     path = os.path.dirname(__file__)
#     tempath = os.path.join(path, "./temp")
#     repotpath = os.path.join(path, "./report")
#     Casepath = os.path.join(patallure serve ./resuit1/h, "test_mon_qkex")
#     pytest.main(["Casepath", "-vs", "--alluredir", "tempath"])
#     os.system(f"allure generate {tempath} -o {repotpath}  --clean")
    # pytest.main(["test_qkexapi.py", "-vs", "--alluredir=report3/", "./report3"])
    # time.sleep(2)
    # os.system("allure generate ./report3 -o ./report3  --clean")