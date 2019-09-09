import unittest
import requests
import ddt
from common.readToken import get_token

testData1 = [{'symbol': 'BTC/USDT','pageNo':1,'pageSize':10,'assert':10},
             {'pageNo': 1, 'pageSize': 10, 'assert': 10},
             {'symbol': 'BTC/USDT','pageSize': 10, 'assert': 10},
             {'symbol': 'BTC/USDT', 'pageNo': 1,'assert': 10}]



@ddt.ddt
class History(unittest.TestCase):
    """历史委托"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token()}
        self.url = "https://api.ezbtest.top/exchange/order/history"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_add1(self, value):
        """请求参数符合接口规范"""
        res = requests.post(self.url, headers=self.headers, data=value).json()
        print(res)
        self.assertEqual(value['assert'], res['size'])


if __name__ == '__main__':
    unittest.main()
