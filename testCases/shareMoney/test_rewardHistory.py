import unittest
import requests
import ddt
from common.readToken import get_token
data1=[{"assert":"成功"},{"pageNo":1,"assert":"成功"},{"pageSize":11,"assert":"成功"},
       {"pageNo": "", "pageSize": "", "assert": "成功"},{"pageNo":1,"pageSize":11,"assert":"成功"}]
data2=[{"pageNo":"aa","assert":"错误的参数"},
       {"pageNo": "汉字", "assert": "错误的参数"},{"pageNo": "!@", "assert": "错误的参数"},
       {"pageSize": "!@", "assert": "错误的参数"},{"pageSize": "aa", "assert": "错误的参数"},
       {"pageSize": "汉字", "assert": "错误的参数"}]
@ddt.ddt
class Rewards(unittest.TestCase):
    """分页查询用户分红记录"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token(),
                        "Accept-Language":"zh-CN",
                        # en-US
                        "Content-Type":"application/x-www-form-urlencoded"}
        self.url = "https://api.ezbtest.top/uc/bar-lock/reward-history"

    def tearDown(self):
        print('test over')
    @ddt.data(*data1)
    def test_rewardHistory1(self,value):
        """"请求参数正确，返回分红记录"""
        rs = requests.post(url=self.url, headers=self.headers, data=value).json()
        print(rs)
        self.assertIn(rs['message'],value['assert'])

    @ddt.data(*data2)
    def test_rewardHistory2(self, value):
        """"请求参数错误，返回分红记录失败"""
        rs = requests.post(url=self.url, headers=self.headers, data=value).json()
        print(rs)
        self.assertIn(rs['message'], value['assert'])


if __name__ =="__main__":
    unittest.main()