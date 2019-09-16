import unittest

import requests


class Querys(unittest.TestCase):
    """查询最新的平台前五用户锁仓分红"""

    def setUp(self):
        self.headers = {"x-auth-token":"04547165-b763-49c4-91a4-7239ea88678a",
                        "Accept-Language":"zh-CN",
                        # en-US
                        "Content-Type":"application/x-www-form-urlencoded"}
        self.url = "https://api.ezbtest.top/uc/reward-pond/page-query"

    def tearDown(self):
        print('test over')

    def test_pageQuery(self):
        rs = requests.post(url=self.url, headers=self.headers).json()
        print(rs)
        self.assertIn(rs['message'],'成功')





if __name__ =="__main__":
    unittest.main()