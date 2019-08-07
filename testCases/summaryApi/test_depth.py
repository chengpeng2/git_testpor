import unittest
import requests


class MarketPair(unittest.TestCase):
    def setUp(self):
        self.url=' https://api.ezbtest.top/thirdparty/v1/depth/USDT_BTC'
    def tearDown(self):
        print('test over')
    def test_assert(self):
        res=requests.get(self.url).json()
        print(res)
        self.assertIn(res['message'],'success')

if __name__ == "__main__":
    unittest.main()
