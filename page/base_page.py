# -*- coding: utf-8 -*-
import warnings
from time import sleep
import time
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from page.logutil import Logsv

class BasePage(object):

    def __init__(self, driver: WebDriver = None):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略一些告警打印
        self.dr = driver
        self.logger = Logsv()
        self.ti = time.strftime("%Y-%m-%d")


    '''等待元素可见'''
    def wait_element_is_visible(self, locator, by="id", timeout=10):
        try:
            wait = WebDriverWait(self.dr, timeout, 1)
            if by == "id":
                wait.until(lambda x: x.find_element_by_id(locator).is_displayed())
            elif by == "xpath":
                wait.until(lambda x: x.find_element_by_xpath(locator).is_displayed())
            elif by == "name":
                wait.until(lambda x: x.find_element_by_name(locator).is_displayed())
            elif by == "class":
                wait.until(lambda x: x.find_element_by_class_name(locator).is_displayed())
            elif by == "css":
                wait.until(lambda x: x.find_element_by_css_selector(locator).is_displayed())
            sleep(1)
            return True
        except Exception:
            return False

    '''等待元素不可见'''
    def wait_element_is_not_visible(self, locator, by="id", timeout=10):
        try:
            wait = WebDriverWait(self.dr, timeout, 1)
            if by == "id":
                wait.until_not(EC.visibility_of_element_located((MobileBy.ID, locator)))
            elif by == "xpath":
                wait.until_not(EC.visibility_of_element_located((MobileBy.XPATH, locator)))
            elif by == "name":
                wait.until_not(EC.visibility_of_element_located((MobileBy.NAME, locator)))
            elif by == "class":
                wait.until_not(EC.visibility_of_element_located((MobileBy.CLASS_NAME, locator)))
            elif by == "css":
                wait.until_not(EC.visibility_of_element_located((MobileBy.CSS_SELECTOR, locator)))

            sleep(1)
            return True
        except Exception:
            return False

    def findid(self, value, by=MobileBy.ID):
        """每一个元素都进行等待,并且进一步简化函数的调用"""
        return WebDriverWait(self.dr, 2).until(lambda x: x.find_element(by=by, value=value))

    def findxpath(self, value, by=MobileBy.XPATH):
        """每一个元素都进行等待,并且进一步简化函数的调用"""
        return WebDriverWait(self.dr, 2).until(lambda x: x.find_element(by=by, value=value))

    def findaccid(self, value, by=MobileBy.ACCESSIBILITY_ID):
        return WebDriverWait(self.dr, 2).until(lambda x: x.find_element(by=by, value=value))

    def finds(self, value, by=MobileBy.XPATH):
        """每一个元素都进行等待,并且进一步简化函数的调用"""
        return WebDriverWait(self.dr, 2).until(lambda x: x.find_elements(by=by, value=value))

    def find_element(self, by, value):
        if by == MobileBy.ID:
            self.dr.find_element(by=MobileBy.ID, value=value)
        elif by == MobileBy.XPATH:
            self.dr.find_element(by=MobileBy.XPATH, value=value)
        elif by == MobileBy.ACCESSIBILITY_ID:
            self.dr.find_element(by=MobileBy.ACCESSIBILITY_ID, value=value)
        return True
