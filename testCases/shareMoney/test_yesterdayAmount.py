import unittest
import requests
import ddt
from common.readToken import get_token


class Amounts(unittest.TestCase):
    """获取最新统计时间的top1锁仓分红折合usdt数量"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token(),
                        "Accept-Language":"zh-CN",
                        "Content-Type":"application/x-www-form-urlencoded"}
        self.url = "https://api.ezbtest.top/uc/reward-pond/yesterday-amount"

    def tearDown(self):
        print('test over')

    def test_pageQuery(self):
        rs = requests.post(url=self.url, headers=self.headers).json()
        print(rs)
        self.assertIn(rs['message'],'成功')





if __name__ =="__main__":
    unittest.main()