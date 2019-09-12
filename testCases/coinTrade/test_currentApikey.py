import unittest
import requests
import ddt
from common.readToken import get_token

testData1 = [{'symbol': 'BTC/USDT','pageNo':1,'pageSize':10,'assert':10},
             {'pageNo': 1, 'pageSize': 10, 'assert': 10},
             {'symbol': 'BTC/USDT','pageSize': 10, 'assert': 10},
             {'symbol': 'BTC/USDT', 'pageNo': 1,'assert':10}]



@ddt.ddt
class CurrentApi(unittest.TestCase):
    """当前委托"""

    def setUp(self):
        self.headers = {"x-auth-token":get_token()}
        self.url = "https://api.ezbtest.top/exchange/order/current?apikey=a1f960b9-6f75-429c-adf6-faf52a11f4e1-829157c9fa8e14a398fa5e47520d39a9"

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
