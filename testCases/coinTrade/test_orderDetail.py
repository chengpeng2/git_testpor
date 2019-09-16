import unittest

import requests

from common.readOrderId2 import get_orderId2
from common.readToken import get_token


class Adds(unittest.TestCase):
    """订单成交详情"""

    def setUp(self):
        self.headers = {"x-auth-token":get_token()}


    def tearDown(self):
        print('test over')

    def test_adds2(self):
        """请求参数合法"""
        self.url = "https://api.ezbtest.top/exchange/order/detail/"
        res = requests.post(self.url+get_orderId2(), headers=self.headers).json()
        print(res)
        self.assertEqual(res[0]['price'],1)


if __name__ == '__main__':
    unittest.main()
