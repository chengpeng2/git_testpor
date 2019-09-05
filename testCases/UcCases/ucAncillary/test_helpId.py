import unittest
import requests
import ddt
from common.readToken import get_token

data1 = [{'assert': '成功'}, {'sysHelpClassification': '0', 'assert': '成功'},
         {'sysHelpClassification': '1', 'assert': '成功'},
         {'sysHelpClassification': '2', 'assert': '成功'},
         {'sysHelpClassification': '3','assert': '成功'},
         {'sysHelpClassification': '4', 'assert': '成功'}]
@ddt.ddt
class helpId(unittest.TestCase):
    """帮助详情"""

    def setUp(self):
        self.headers = {"Accept-Language":"zh_CN"}
        self.url = "https://api.ezbtest.top/uc/ancillary/system/help/6"

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
