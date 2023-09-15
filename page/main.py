# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage
class Main(BasePage):
        def __init__(self, driver):
            BasePage.__init__(self, driver=driver)
        def clickupdate(self):
            try:
                self.logger.info('点击取消更新')
                el1 = self.findid("com.qkex:id/resetTv")
                WebDriverWait(self.dr, 10, 0.5).until(EC.presence_of_element_located(el1))
                el1.click()
            except:
                self.logger.info('不用点击取消更新')
                pass

