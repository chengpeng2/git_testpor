import unittest

import ddt
import requests

data1 = [{'assert': '成功'}, {'sysHelpClassification': '0', 'assert': '成功'},
         {'sysHelpClassification': '1', 'assert': '成功'},
         {'sysHelpClassification': '2', 'assert': '成功'},
         {'sysHelpClassification': '3','assert': '成功'},
         {'sysHelpClassification': '4', 'assert': '成功'}]
@ddt.ddt
class helps(unittest.TestCase):
    """系统帮助"""

    def setUp(self):
        self.headers = {"Accept-Language":"zh-CN"}
        self.url = "https://api.ezbtest.top/ancillary/system/help"

    def tearDown(self):
        print('test over')

    @ddt.data(*data1)
    def test_ad1(self,value):
        res = requests.get(url=self.url,headers=self.headers,params=value).json()
        print(res)
        self.assertIn('success', res['message'])

    @ddt.data(*data1)
    def test_ad2(self,value):
        res = requests.post(url=self.url,headers=self.headers,params=value).json()
        print(res)
        self.assertIn('success', res['message'])


if __name__ == '__main__':
    unittest.main()
