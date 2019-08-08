import unittest
import requests
import ddt


class Ticker(unittest.TestCase):
    """交易所行情"""

    def setUp(self):
        self.url = ' https://api.ezbtest.top/thirdparty/v1/ticker'

    def tearDown(self):
        print('test over')

    def test_assert(self):
        res = requests.get(self.url).json()
        print(res)
        self.assertIn(res['message'], 'success')


if __name__ == "__main__":
    unittest.main()
