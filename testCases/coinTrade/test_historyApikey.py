import unittest

import ddt
import requests

from common.readToken import get_token

testData1 = [{'assert': 10},
             {'symbol': 'BTC/USDT', 'assert': 10},
             {'symbol': 'BTC/USDT', 'pageNo': 1, 'assert': 10},
             {'symbol': 'BTC/USDT', 'pageSize': 20, 'assert': 10},
             {'symbol': 'BTC/USDT', 'pageNo':1,'pageSize': 20, 'assert': 20},
             {'pageNo': 1, 'pageSize': 20, 'assert': 20}]
testData2 = [{'pageNo': 'a', 'pageSize': 'b', 'assert': "Invalid parameter"},
             {'pageNo': 1, 'pageSize': 'b', 'assert': "Invalid parameter"},
             {'pageNo': 'q', 'pageSize': 1, 'assert': "Invalid parameter"}]


@ddt.ddt
class HistoryApikey(unittest.TestCase):
    """历史委托"""

    def setUp(self):
        self.headers = {"x-auth-token":get_token()}
        self.url = "https://api.ezbtest.top/exchange/order/history?apikey=a1f960b9-6f75-429c-adf6-faf52a11f4e1-829157c9fa8e14a398fa5e47520d39a9"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_history(self, value):
        """请求参数符合接口规范"""
        res = requests.post(self.url, headers=self.headers, data=value).json()
        print(res)
        self.assertEqual(value['assert'], res['size'])

    @ddt.data(*testData2)
    def test_history2(self, value):
        """请求参数不符合接口规范"""
        res = requests.post(self.url, headers=self.headers, data=value).json()
        print(res)
        self.assertEqual(value['assert'], res['message'])


if __name__ == '__main__':
    unittest.main()
