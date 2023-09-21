# -*- coding: utf-8 -*-
import allure
import json
import requests
from qkexapifu.logutil import Logsv
logger = Logsv()
headers = {
  'source': 'api',
  'Accept-Language': 'zh-CN',
  'X-Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxMDgzZGVhYi1iMTA3LTQ4ZDMtOTIzMC00ODMwZGI0NWFmM2QiLCJ1aWQiOiJPNEVwbXJhZWJLRFdxbzF6U2l6cnJRPT0iLCJiaWQiOiJXWFAxUS8xa2s5NVQxTjRxOWxuSFRBPT0iLCJpcCI6IkdwdHl4M01ZbzBJemNsL3pwN0ZiNXc9PSIsImRldiI6InAva3BIckF3RkJjSUZleXg0U2xkZGc9PSIsInN0cyI6MCwiaWF0IjoxNjcyNTAyNDAwLCJleHAiOjE3MTk4MDI1MTAsImlzcyI6InFrZXgifQ.MEuydGH6Kt94o8mm90WFlmSvs17LEClcFQrYt4d7l74',
  'Content-Type': 'application/json'
}

@allure.feature("订单相关接口")
class TestContractOrdersAPI:
    @allure.step("步骤1：针对单个跟单进行平仓")
    def test_create_follow_user(self):
        logger.info('***************订单相关接口测试开始***************')
        url = "http://test-futures-rest.qkex.com/v1/follow/order/closePosition"
        payload = json.dumps({
            "tradeType": "linearPerpetual",
            "orderId": "108234",
            "symbol": "BTCUSDT"
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        logger.info('针对单个跟单进行平仓返回信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":"0"' in response.text


@allure.feature("跟单用户接口")
class TestFollowUsersAPI:
    @allure.step("步骤1：添加或更新个人信息")
    def test_create_follow_user(self):
        logger.info('***************跟单用户接口测试开始***************')
        url = "http://test-futures-rest.qkex.com/v1/follow/user/upsert"
        payload = json.dumps({
            "name": "owen1",
            "sign": "浪打浪",
            "photo": "gxc3ih"
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        logger.info('添加或更新个人信息返回信息：{%s}' % response.text)
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤2：查询跟单用户信息")
    def test_follow_user(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/user"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询跟单用户信息返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤3：查询用户收益汇总")
    def test_follow_user_income(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/user/income"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询用户收益汇总返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤4：查询用户分润汇总")
    def test_follow_user_divideInto(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/user/divideInto"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询用户分润汇总返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤5：查询用户跟随收益信息")
    def test_follow_user_followerTradeIncome(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/user/followerTradeIncome"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询用户跟随收益信息返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤6：查询用户当前跟单信息")
    def test_follow_user_current(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/user/current"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询用户当前跟单信息返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤7：查询用户历史跟单信息")
    def test_follow_user_history(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/user/history"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询用户历史跟单信息返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤8：查询跟单用户的交易员信息")
    def test_follow_user_traders(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/user/traders"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询跟单用户的交易员信息返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text
        logger.info('***************跟单用户接口测试结束***************')

@allure.feature("跟单配置接口")
class TestFollowConfigAPI:
    @allure.step("步骤1：查询跟单配置")
    def test_update_follow_config(self):
        logger.info('***************跟单配置接口测试开始***************')
        url = "http://test-futures-rest.qkex.com/v1/follow/setting?tradeType=linearPerpetual&traderUid=10122479"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询跟单配置返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤2：跟单或更新跟单")
    def test_follow_user_upsert(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/setting/upsert"
        payload = json.dumps({
            "traderUid": 10122479,
            "tradeType": "linearPerpetual",
            "marginType": 2,
            "leverage": 0,
            "orderType": 1,
            "orderMargin": 645,
            "orderMarginRatio": 30,
            "marginAmount": 899,
            "triggerTpRatio": 60,
            "triggerSlRatio": 58,
            "positionMarginMax": 1025,
            "symbol": "BTCUSDT"
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('跟单或更新跟单返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤3：跟单用户取消跟随")
    def test_follow_user_cancelFollow(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/setting/cancelFollow"
        payload = json.dumps({
            "tradeType": "linearPerpetual",
            "traderUid": 10122479
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('跟单用户取消跟随返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤4：空位提醒")
    def test_follow_remind(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/setting/remind"
        payload = json.dumps({
            "tradeType": "linearPerpetual",
            "traderUid": 10122479
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('空位提醒返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤5：交易员踢出跟随者")
    def test_follow_kick(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/setting/kick/10122165"
        payload = json.dumps({
            "tradeType": "linearPerpetual",
            "traderUid": 10122479
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('交易员踢出跟随者返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text
        logger.info('***************跟单配置接口测试结束***************')

@allure.feature("交易员跟单首页接口")
class TestTraderHomePageAPI:
    @allure.step("步骤1：交易员申请")
    def test_follow_trader_apply(self):
        logger.info('***************交易员跟单首页接口测试开始***************')
        url = "http://test-futures-rest.qkex.com/v1/follow/trader/apply"
        payload = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('交易员申请返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤2：查询交易员详细信息")
    def test_follow_trader_detail(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/trader/detail"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询交易员详细信息返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤3：查询交易员当前带单")
    def test_follow_trader_order(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/trader/order"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询交易员当前带单返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤4：查询交易员历史带单")
    def test_follow_trader_history_order(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/trader/history/order"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询交易员历史带单返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤5：查询交易员跟随者")
    def test_follow_trader_followers(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/trader/followers"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询交易员跟随者返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤6：查询交易员交易数据")
    def test_follow_trader_data(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/trader/data?period=577"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('查询交易员交易数据返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text

    @allure.step("步骤7：跟单首页 - 交易员信息统计")
    def test_follow_index(self):
        url = "http://test-futures-rest.qkex.com/v1/follow/index?pageNum=1&pageSize=10&name=randy.leuschke&sortRule=92p67l"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info('跟单首页 - 交易员信息统计返回信息：{%s}' % response.text)
        allure.step("步骤2：验证响应信息")
        assert response.status_code == 200
        assert '"code":"0"' in response.text
        logger.info('***************交易员跟单首页接口测试结束**************')

