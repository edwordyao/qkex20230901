# -*- coding: utf-8 -*-
from appium import webdriver



# class QkexApp:


def qkexapp():
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "qkex"
            caps["udid"] = "127.0.0.1:5555"
            caps["appPackage"] = "com.qkex"
            caps["appActivity"] = "com.coin.ex.main.SplashActivity"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            caps["skipDeviceInitialization"] = "true"
            caps["dontStopAppOnReset"] = "true"
            caps["unicodeKeyBord"] = "true"
            caps["resetKeyBord"] = "true"
            caps["skipServerInitialization"] = "true"
            caps['app'] = r'C:\qkex20230901\app\QKEx_dev_3.0.15-dev.apk'
            dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            dr.implicitly_wait(5)
            return dr
