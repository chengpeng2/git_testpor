import unittest
import requests


class MarketPair(unittest.TestCase):
    """交易所最近成交"""

    def setUp(self):
        self.url = ' https://api.ezbtest.top/thirdparty/v1/trades/USDT_BTC'

    def tearDown(self):
        print('test over')

    def test_assert(self):
        res = requests.get(self.url,verify=False).json()
        print(res)
        self.assertIn(res['message'], 'success')


if __name__ == "__main__":
    unittest.main()
