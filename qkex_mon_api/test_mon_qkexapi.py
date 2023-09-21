# -*- coding: utf-8 -*-
import allure
import json
import requests
from qkex_mon_api.logutil import Logsv
logger = Logsv()

@allure.feature("首页相关接口")
class TestHometPageAPI:
    @allure.step("接口：exchange-rate")
    def test_foundation_indexes_exchange_rate(self):
        logger.info('***************首页相关接口测试开始***************')
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
        logger.info('接口exchange-rate返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：instruments")
    def test_public_web_instruments(self):
        url = "https://futures-rest.qkex.com/v1/public/web/instruments?tradeType=linearPerpetual"
        payload = ""
        headers = {
            'authority': 'futures-rest.qkex.com',
            'source': 'web',
            'x-authorization': '',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口instruments返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("接口：favorite/list")
    def test_exchange_favorite_list(self):
        url = "https://public-rest.qkex.com/exchange/favorite/list"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口favorite/list返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：user-balance")
    def test_wallet_user_balance(self):
        url = "https://public-rest.qkex.com/wallet/user-balance"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口user-balance返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：currencies")
    def test_wallet_currencies(self):
        url = "https://public-rest.qkex.com/wallet/currencies"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口currencies返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：assets")
    def test_exchange_assets(self):
        url = "https://public-rest.qkex.com/exchange/assets"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口assets返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：icons")
    def test_exchange_public_currency_icons(self):
        url = "https://public-rest.qkex.com/exchange/public/currency/icons"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': '',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口icons返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：queryRate/BTC")
    def test_exchange_public_queryRate_BTC(self):
        url = "https://public-rest.qkex.com/exchange/public/queryRate/BTC"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': '',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口queryRate/BTC返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：kyc-status")
    def test_user_kyc_kyc_status(self):
        url = "https://public-rest.qkex.com/user/kyc/kyc-status"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口kyc-status返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：detail")
    def test_user_detail(self):
        url = "https://public-rest.qkex.com/user/detail"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口detail返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：embeddable/config")
    def test_embeddable_config(self):
        url = "https://qkexcrypto.zendesk.com/embeddable/config"

        payload = {}
        headers = {
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口embeddable/config返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert 'moduleFederation' in response.text

    @allure.step("接口：riskWarning")
    def test_user_public_riskWarning(self):
        url = "https://public-rest.qkex.com/user/public/riskWarning"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口riskWarning返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":0' in response.text

    @allure.step("接口：otc/advertiser/type")
    def test_otc_advertiser_type(self):
        url = "https://public-rest.qkex.com/otc/advertiser/type"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口otc/advertiser/type返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":0' in response.text

    @allure.step("接口：news")
    def test_foundation_cms_news(self):
        url = "https://public-rest.qkex.com/foundation/cms/news"

        payload = ""
        headers = {
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-locale': 'en-US',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口news返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":0' in response.text

    @allure.step("接口：banners")
    def test_foundation_cms_banners(self):
        url = "https://public-rest.qkex.com/foundation/cms/banners"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693296043.31.1.1693296057.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口banners返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":0' in response.text
        logger.info('***************首页相关接口测试结束***************')

@allure.feature("行情相关接口")
class TestMarketsAPI:
    @allure.step("接口：currencies")
    def test_exchange_public_currencies(self):
        logger.info('***************行情相关接口测试开始***************')
        url = "https://public-rest.qkex.com/exchange/public/currencies"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1MTEyMWQ0ZC0wNTU4LTQzMWItOTkyYy0wMTZlN2ZiZjIyYzExNTIxNjA1NzA5IiwidWlkIjoiWUVUK1BaS1JURVIrR2dnMDdtKytpQT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5MzI3NTAwNCwiZXhwIjoxNjkzMzYxNDA0LCJpc3MiOiJ3Y3MifQ.X2_uX5F5KxXos-I7-zDbU8JgRaVZU6fVXEf0TXwO9jw',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1689060671.12.0.1689060671.0.0.0; _ga=GA1.1.779387238.1686556881; locale=en-US; _ga_BC2SP908YM=GS1.1.1693295355.121.1.1693295355.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口currencies返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：tickers")
    def test_exchange_public_tickers(self):
        url = "https://public-rest.qkex.com/exchange/public/tickers"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1MTEyMWQ0ZC0wNTU4LTQzMWItOTkyYy0wMTZlN2ZiZjIyYzExNTIxNjA1NzA5IiwidWlkIjoiWUVUK1BaS1JURVIrR2dnMDdtKytpQT09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5MzI3NTAwNCwiZXhwIjoxNjkzMzYxNDA0LCJpc3MiOiJ3Y3MifQ.X2_uX5F5KxXos-I7-zDbU8JgRaVZU6fVXEf0TXwO9jw',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1689060671.12.0.1689060671.0.0.0; _ga=GA1.1.779387238.1686556881; locale=en-US; _ga_BC2SP908YM=GS1.1.1693295355.121.1.1693295355.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口tickers返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text
        logger.info('***************行情相关接口测试结束***************')

@allure.feature("C2C相关接口")
class TestC2CAPI:
    @allure.step("接口：otc/public/orders")
    def test_otc_public_orders(self):
        logger.info('***************C2C相关接口测试开始***************')
        url = "https://public-rest.qkex.com/otc/public/orders?page=1&pageSize=1000&legalSymbol=CNY&symbol=USDT&side=sell"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693360044.34.1.1693360328.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口otc/public/orders返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：otc/advertiser/type")
    def test_otc_advertiser_type(self):
        url = "https://public-rest.qkex.com/otc/advertiser/type"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693360044.34.1.1693360328.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口otc/advertiser/type返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text


    @allure.step("接口：otc/public/getRiskInfo")
    def test_otc_public_getRiskInfo(self):
        url = "https://public-rest.qkex.com/otc/public/getRiskInfo"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693360044.34.1.1693360328.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口otc/public/getRiskInfo返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：fiat-setting/detail")
    def test_fiat_setting_detail(self):
        url = "https://public-rest.qkex.com/user/fiat-setting/detail"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693360044.34.1.1693360328.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口fiat-setting/detail返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：otc/public/configFiatSetting")
    def test_otc_public_configFiatSetting(self):
        url = "https://public-rest.qkex.com/otc/public/configFiatSetting?legalSymbol=CNY"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693360044.34.1.1693360328.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口otc/public/configFiatSetting返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：otc/public/legalCurrencies")
    def test_otc_public_legalCurrencies(self):
        url = "https://public-rest.qkex.com/otc/public/legalCurrencies"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmMzM5NGQ2Yi04YWNlLTQ1ZjQtYTQ1Ny04MWIzZjNkMDA3OTcyMjg5NTg5MiIsInVpZCI6IkhYallkUjBKNmY4TkhzeHhXTVlOS0E9PSIsImJpZCI6Im1XT083RjJ6c04wVHdSQXlRRGxrK0E9PSIsImlwIjoiSzgvZmJrSmVVZkU1RlkwUWwzVXRadz09IiwiZGV2IjoiQThvTE5lUlZ2RkdveEw5UFplaGtwQT09Iiwic3RzIjowLCJpYXQiOjE2OTMyODg1NDEsImV4cCI6MTY5MzM3NDk0MSwiaXNzIjoid2NzIn0.4bwzcUEqEvl1yksVJOHYXn2pslcy9UVKgAI5U4F-XsQ',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693360044.34.1.1693360328.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口otc/public/legalCurrencies返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：otc/userInfo/overview")
    def test_otc_userInfo_overview(self):
        url = "https://public-rest.qkex.com/otc/userInfo/overview"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'en',
            'x-locale': 'en-US',
            'Cookie': '_ga=GA1.1.1569607884.1692244572; locale=en-US; _ga_BC2SP908YM=GS1.1.1693360044.34.1.1693360328.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口otc/userInfo/overview返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：otc/pendings-我的订单")
    def test_otc_pendings(self):
        url = "https://public-rest.qkex.com/otc/pendings?status=98&page=1&pageSize=10"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'pragma': 'no-cache',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; locale=en-US; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693547483.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口otc/pendings-我的订单返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text


    @allure.step("接口：detail--收付款設定")
    def test_user_fiat_setting_detail(self):
        url = "https://public-rest.qkex.com/user/fiat-setting/detail"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'pragma': 'no-cache',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; locale=en-US; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693547483.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口detail--收付款設定返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：update-收付款新增")
    def test_user_fiat_setting_update(self):
        url = "https://public-rest.qkex.com/user/fiat-setting/update"

        payload = json.dumps({
            "userId": 168910,
            "status": 1,
            "payType": 4,
            "verifyCode": "539747",
            "fiatSetting": {
                "0": "sam",
                "1": "sam787"
            }
        })
        headers = {
            'authority': 'public-rest.qkex.com',
            'pragma': 'no-cache',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; locale=en-US; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693547483.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('接口update-收付款新增返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":4076' in response.text
        logger.info('***************C2C相关接口测试结束***************')

@allure.feature("现货相关接口")
class TestSpotAPI:
    @allure.step("接口：transfer")
    def test_wallet_transfer(self):
        logger.info('***************现货相关接口测试开始***************')
        url = "https://public-rest.qkex.com/wallet/transfer"

        payload = json.dumps({
            "from": "exchange",
            "to": "otc",
            "symbol": "USDT",
            "currency": "USDT",
            "pairCode": "P_R_USDT_USD",
            "amount": "1"
        })
        headers = {
            'authority': 'public-rest.qkex.com',
            'pragma': 'no-cache',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; locale=en-US; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693548094.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('接口transfer返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text



    @allure.step("接口：orders-下单")
    def test_exchange_ADA_USDT_orders(self):
        url = "https://public-rest.qkex.com/exchange/ADA_USDT/orders"

        payload = json.dumps({
            "systemOrderType": "limit",
            "side": "buy",
            "price": "0.24",
            "volume": "50",
            "source": "web",
            "quoteVolume": "0"
        })
        headers = {
            'authority': 'public-rest.qkex.com',
            'pragma': 'no-cache',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; locale=en-US; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693548322.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('接口orders-下单返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":1055' in response.text



    @allure.step("接口：orders-取消订单")
    def test_exchange_ADA_USDT_orders_NO(self):
        url = f"https://public-rest.qkex.com/exchange/ADA_USDT/orders/183103837510784"
        payload = json.dumps({})
        headers = {
            'authority': 'public-rest.qkex.com',
            'pragma': 'no-cache',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; locale=en-US; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693548322.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)
        logger.info('接口orders-取消订单返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":1059' in response.text



    @allure.step("接口：orders-当前委托")
    def test_exchange_orders_now(self):
        url = "https://public-rest.qkex.com/exchange/orders?page=1&pageSize=10"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'pragma': 'no-cache',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; locale=en-US; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693548322.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口orders-当前委托返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：fulfillment-历史委托")
    def test_exchange_ADA_USDT_fulfillment(self):
        url = "https://public-rest.qkex.com/exchange/ADA_USDT/fulfillment?page=1&pageSize=10"

        payload = ""
        headers = {
            'authority': 'public-rest.qkex.com',
            'pragma': 'no-cache',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; locale=en-US; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693548322.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口fulfillment-历史委托返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text
        logger.info('***************现货相关接口测试结束***************')

@allure.feature("理财相关接口")
class TestEarnAPI:
    @allure.step("接口：product_list_理财产品列表")
    def test_earn_product_list(self):
        logger.info('***************理财相关接口测试开始***************')
        url = "https://financial.qkex.com/api/earn/product_list"

        payload = ""
        headers = {
            'authority': 'financial.qkex.com',
            'pragma': 'no-cache',
            'source': 'web',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693548848.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('接口product_list_理财产品列表返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：order-活跃理财")
    def test_earn_order(self):
        url = "https://financial.qkex.com/api/earn/order"

        payload = json.dumps({
            "product_id": 1,
            "type": 1,
            "plat_form": "pc",
            "application_loan_qty": "0.1"
        })
        headers = {
            'authority': 'financial.qkex.com',
            'pragma': 'no-cache',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693548848.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('接口order-活跃理财返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"msg":"success"' in response.text

    @allure.step("接口：userRegularOrders--活期列表")
    def test_earn_userRegularOrders(self):
        url = "https://public-rest.qkex.com/earn/api/userRegularOrders?userId=168910"

        payload = json.dumps({})
        headers = {
            'authority': 'public-rest.qkex.com',
            'pragma': 'no-cache',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; locale=en-US; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693548848.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('接口userRegularOrders--活期列表返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":200' in response.text

    @allure.step("接口：redemption--赎回")
    def test_earn_redemption(self):
        url = "https://financial.qkex.com/api/earn/redemption"

        payload = json.dumps({
            "amount": "1",
            "currency": "USDT"
        })
        headers = {
            'authority': 'financial.qkex.com',
            'pragma': 'no-cache',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693548848.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('接口redemption--赎回返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":400' in response.text

    @allure.step("接口：userBills--流水")
    def test_earn_userBills(self):
        url = "https://public-rest.qkex.com/earn/api/userBills?userId=168910"

        payload = json.dumps({
            "startTime": "2023-09-01 00:00:00",
            "endTime": "2023-09-01 23:59:59",
            "symbol": "",
            "transType": "71",
            "orderType": "1",
            "pageIndex": 1,
            "pageSize": 10,
            "userId": 168910
        })
        headers = {
            'authority': 'public-rest.qkex.com',
            'pragma': 'no-cache',
            'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGMxZmIyMS1jNzI5LTQ4YWQtYWZiMi0wODg5OTFhNTBlMmUxNzI5OTMyNDg1IiwidWlkIjoiWlR3dldUNElUQVpLdzd5bW53NTB5Zz09IiwiYmlkIjoibVdPTzdGMnpzTjBUd1JBeVFEbGsrQT09IiwiaXAiOiJLOC9mYmtKZVVmRTVGWTBRbDNVdFp3PT0iLCJkZXYiOiJBOG9MTmVSVnZGR294TDlQWmVoa3BBPT0iLCJzdHMiOjAsImlhdCI6MTY5NTE5NjM4OCwiZXhwIjoxNjk1MjgyNzg4LCJpc3MiOiJ3Y3MifQ.c-Y7BcKOwAe4JVkwgdt6jEvZUT_s3jX7p0Xtzc0eG50',
            'x-lang': 'zh-HK',
            'x-locale': 'zh-HK',
            'Cookie': '_ga_R83JEZS8YW=GS1.1.1687789380.154.0.1687789380.0.0.0; _ga=GA1.1.1799156164.1678413378; locale=en-US; _ga_BC2SP908YM=GS1.1.1693547481.17.1.1693548848.0.0.0',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('接口userBills--流水返回的信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":200' in response.text
        logger.info('***************理财相关接口测试结束***************')