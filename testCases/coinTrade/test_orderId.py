import unittest

import requests

from common.readOrderId import get_orderId
from common.readToken import get_token


class Adds(unittest.TestCase):
    """取消下单"""

    def setUp(self):
        self.headers = {"x-auth-token":get_token()}


    def tearDown(self):
        print('test over')

    def test_adds1(self):
        """请求参数合法"""
        self.url = "https://api.ezbtest.top/exchange/order/cancel/"
        res = requests.post(self.url+get_orderId(), headers=self.headers).json()
        print(res)
        self.assertIn('success', res['message'])


if __name__ == '__main__':
    unittest.main()
