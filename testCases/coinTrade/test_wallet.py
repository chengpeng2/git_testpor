import unittest
import requests
from common.readToken import get_token
from common.readOrderId2 import get_orderId2

class Adds(unittest.TestCase):
    """订单成交详情"""

    def setUp(self):

      pass

    def tearDown(self):
        print('test over')

    def test_adds2(self):
        """获取所有资产不为0的钱包信息"""
        self.url = "https://api.ezbtest.top/exchange/order/wallet?apiKey=a1f960b9-6f75-429c-adf6-faf52a11f4e1-829157c9fa8e14a398fa5e47520d39a9"
        res = requests.get(self.url).json()
        print(res)
        self.assertEqual('success',res['message'])


if __name__ == '__main__':
    unittest.main()
