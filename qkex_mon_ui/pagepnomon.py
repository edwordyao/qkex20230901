# -*- coding: utf-8 -*-
from qkex_mon_ui.base_page import BasePage
class PnoMon(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver=driver)


    '"现货下单'

    def spotspnomon(self):
        self.logger.info('【现货下单监控】开始')
        el1 = self.findxpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView")
        el1.click()
        el2 = self.findid("com.qkex:id/current_more")
        el2.click()
        el3 = self.findxpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText")
        el3.click()
        el4 = self.findxpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText")
        el4.click()
        el4.send_keys('0.01')
        el1 = self.findid("com.qkex:id/tv_confirm")
        el1.click()
        el6 = self.findid('com.qkex:id/tv_trade_all_orders')
        el6.click()
        self.logger.info('【订单断言，数据监控】开始')
        if self.wait_element_is_visible('com.qkex:id/tv_order_cancel', by='id', timeout=10):
            el7 = self.dr.findid('com.qkex:id/tv_order_cancel')
            el7.click()
            el8 = self.dr.findid('com.qkex:id/tv_dialog_positive')
            el8.click()
        else:
            self.logger.info('-----现货下单操作失败！！！------')
        el9 = self.findxpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView')
        el9.click()
        el10 = self.findxpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')
        el10.click()
        self.logger.info('【现货下单监控】结束')
        return True

    def conpnomon(self):
        self.logger.info('【合约下单监控】开始')
        el1 = self.findxpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView')
        el1.click()
        el1 = self.findid('com.qkex:id/current_more')
        el1.click()
        el1 = self.findxpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.view.ViewGroup/android.widget.TextView[1]')
        el1.click()
        el1 = self.findid('com.qkex:id/et_quantity')
        el1.click()
        el1.send_keys('0.01')
        el1 = self.findid('com.qkex:id/tv_confirm_more')
        el1.click()
        el2 = self.findid('com.qkex:id/b_confirm')
        el2.click()
        el3 = self.findaccid("當前委託(1)")
        el3.click()
        self.logger.info('【订单断言，数据监控】开始')
        if self.wait_element_is_visible('com.qkex:id/tv_cancel', by='id', timeout=10):
            el4 = self.findid('com.qkex:id/tv_cancel')
            el4.click()
        else:
            self.logger.info('-----现货下单操作失败！！！------')
        el5 = self.findxpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')
        el5.click()
        self.logger.info('【合约下单监控】结束')
        return True

