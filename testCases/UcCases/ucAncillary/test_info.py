import unittest
import requests
import ddt
from common.readToken import get_token


class infos(unittest.TestCase):
    """未使用的接口(站点信息)"""

    def setUp(self):
        self.url = "https://api.ezbtest.top/uc/ancillary/website/info"

    def tearDown(self):
        print('test over')

    def test_ad1(self):
        res = requests.get(url=self.url).json()
        print(res)
        self.assertIn('success', res['message'])


    def test_ad2(self):
        res = requests.post(url=self.url).json()
        print(res)
        self.assertIn('success', res['message'])


if __name__ == '__main__':
    unittest.main()
