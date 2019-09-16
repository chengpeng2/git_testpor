import unittest

import ddt
import requests


@ddt.ddt
class helps(unittest.TestCase):
    """币种资料详情"""

    def setUp(self):
        self.headers = {"Accept-Language":"zh-CN"}
        self.url = "https://api.ezbtest.top/ancillary/coin-content/55"

    def tearDown(self):
        print('test over')


    def test_pages(self):
        res = requests.get(url=self.url,headers=self.headers).json()
        print(res)
        self.assertIn('success', res['message'])


if __name__ == '__main__':
    unittest.main()
