import unittest

import ddt
import requests

from common.readToken import get_token

testData1 = [{'remark': '测试', 'assert': 'success'}, {'remark': 'aaa', 'assert': 'success'},
            {'remark': '123', 'assert': 'success'}]
testData2=[{'remark': '', 'assert': 'Parameter error'}]


@ddt.ddt
class FeedBack(unittest.TestCase):
    """创建用户反馈"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token()}
        self.url = "https://api.ezbtest.top/uc/feedback"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_records1(self, value):
        """请求参数合法"""
        res = requests.post(self.url,headers=self.headers, data=value,verify=False).json()
        print(res)
        self.assertIn(value['assert'], res['message'])
    @ddt.data(*testData2)
    def test_records2(self, value):
        """请求参数合法"""
        res = requests.post(self.url, headers=self.headers, data=value, verify=False).json()
        print(res)
        self.assertIn(value['assert'], res['message'])


if __name__ == '__main__':
    unittest.main()
