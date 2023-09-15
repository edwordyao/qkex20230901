# -*- coding: utf-8 -*-
import pytest
from page.app import qkexapp
from page.main import Main
from page.pagepnomon import PnoMon
from page.logutil import Logsv
logger = Logsv()
class Testmonqkex:
    def setup(self):
        self.dr = qkexapp()
        logger.info('***************监控测试开始***************')




    def teardown(self):
        self.dr.quit()
        logger.info('***************监控测试结束***************')
    '''现货下单'''

    # @pytest.mark.run(order=1)
    def test_spotspnomon(self):
        ma = Main(self.dr)
        pn = PnoMon(self.dr)
        ma.clickupdate()
        pn.spotspnomon()
    '''合约下单'''

    # @pytest.mark.run(order=2)
    def test_conpnomon(self):
        ma = Main(self.dr)
        pn = PnoMon(self.dr)
        ma.clickupdate()
        pn.conpnomon()

if __name__ == '__main__':
    pytest.main()
