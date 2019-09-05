import unittest
import requests
import ddt
from common.readToken import get_token

data1 = [{'assert': '成功'}, {'sysAdvertiseLocation': '0', 'language': 'zh-CN', 'assert': '成功'},
         {'sysAdvertiseLocation': '1', 'language': 'zh-CN', 'assert': '成功'},
         {'sysAdvertiseLocation': '2', 'language': 'zh-CN', 'assert': '成功'},
         {'sysAdvertiseLocation': '3', 'language': 'en-US', 'assert': '成功'},
         {'sysAdvertiseLocation': '4', 'language': 'en-US', 'assert': '成功'}]
@ddt.ddt
class adver(unittest.TestCase):
    """系统广告"""

    def setUp(self):
        self.url = "https://api.ezbtest.top/uc/ancillary/system/advertise"

    def tearDown(self):
        print('test over')

    @ddt.data(*data1)
    def test_ad1(self, value):
        res = requests.get(url=self.url, params=value).json()
        print(res)
        self.assertIn('success', res['message'])

    @ddt.data(*data1)
    def test_ad2(self, value):
        res = requests.post(url=self.url, data=value).json()
        print(res)
        self.assertIn('success', res['message'])


if __name__ == '__main__':
    unittest.main()
