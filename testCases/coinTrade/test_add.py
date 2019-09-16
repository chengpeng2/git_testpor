import unittest

import ddt
import requests

from common.readToken import get_token

testData1 = [
    {'direction': 'BUY', 'symbol': 'BTC/USDT', 'price': 1, 'amount': 1, 'type': 'LIMIT_PRICE', 'assert': 'success'},
    {'direction': 'SELL', 'symbol': 'BTC/USDT', 'price': 1, 'amount': 1, 'type': 'MARKET_PRICE', 'assert': 'success'},
    {'direction': 'SELL', 'symbol': 'BTC/USDT', 'amount': 1, 'type': 'MARKET_PRICE', 'assert': 'success'}]
testData2 = [{'symbol': 'BTC/USDT', 'price': 1, 'amount': 1, 'type': 'MARKET_PRICE', 'assert': 'Invalid parameter'},
             {'direction': 'SELL', 'price': 1, 'amount': 1, 'type': 'MARKET_PRICE', 'assert': 'Unsupported coin!'},
             {'direction': 'BUY', 'symbol': 'BTC/USDT', 'price': 1, 'amount': 1, 'assert': 'Invalid parameter'},
             {'direction': 'SELL', 'symbol': 'BTC/USDT', 'price': 1, 'type': 'MARKET_PRICE',
              'assert': 'Invalid number'}]


@ddt.ddt
class Add(unittest.TestCase):
    """下单"""

    def setUp(self):
        self.headers = {"x-auth-token":get_token()}
        self.url = "https://api.ezbtest.top/exchange/order/add"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_add1(self, value):
        """请求参数合法"""
        res = requests.post(self.url, headers=self.headers, data=value).json()
        print(res)
        self.assertIn(value['assert'], res['message'])

    @ddt.data(*testData2)
    def test_add2(self, value):
        """请求参数不合法"""
        res = requests.post(self.url, headers=self.headers, data=value).json()
        print(res)
        self.assertIn(value['assert'], res['message'])


if __name__ == '__main__':
    unittest.main()
