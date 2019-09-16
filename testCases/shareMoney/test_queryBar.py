import unittest

import ddt
import requests

from common.readToken import get_token

data1=[{"assert":"success"},{"pageNo":1,"assert":"success"},{"pageSize":11,"assert":"success"},
       {"pageNo": "", "pageSize": "", "assert": "success"},{"pageNo":1,"pageSize":11,"assert":"success"}]
data2=[{"pageNo":"aa","assert":"错误的参数"},
       {"pageNo": "汉字", "assert": "错误的参数"},{"pageNo": "!@", "assert": "错误的参数"},
       {"pageSize": "!@", "assert": "错误的参数"},{"pageSize": "aa", "assert": "错误的参数"},
       {"pageSize": "汉字", "assert": "错误的参数"}]
@ddt.ddt
class QueryBars(unittest.TestCase):
    """分页查询用户用户锁仓记录（不包含已解锁）"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token(),
                        "Accept-Language":"zh-CN",
                        # en-US
                        "Content-Type":"application/x-www-form-urlencoded"}
        self.url = "https://api.ezbtest.top/uc/bar/queryBar"

    def tearDown(self):
        print('test over')
    @ddt.data(*data1)
    def test_lock1(self,value):
        """"请求参数正确，用户锁仓成功"""
        rs = requests.post(url=self.url, headers=self.headers, data=value).json()
        print(rs)
        self.assertIn(rs['message'],value['assert'])

    @ddt.data(*data2)
    def test_lock2(self, value):
        """"请求参数错误，用户锁仓失败"""
        rs = requests.post(url=self.url, headers=self.headers, data=value).json()
        print(rs)
        self.assertIn(rs['message'], value['assert'])


if __name__ =="__main__":
    unittest.main()