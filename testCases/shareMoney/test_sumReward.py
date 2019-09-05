import unittest
import requests
import ddt
from common.readToken import get_token


class SumRewards(unittest.TestCase):
    """用户BAR锁仓"""

    def setUp(self):
        self.headers = {"x-auth-token":get_token(),
                        "Accept-Language":"zh-CN",
                        "Content-Type":"application/x-www-form-urlencoded"}
        self.url = "https://api.ezbtest.top/uc/bar-lock/sum-reward"

    def tearDown(self):
        print('test over')

    def test_sumReward1(self):
        """"用户锁仓数量查询"""
        rs = requests.post(url=self.url, headers=self.headers).json()
        print(rs)
        self.assertIn(rs['message'],'成功')





if __name__ =="__main__":
    unittest.main()