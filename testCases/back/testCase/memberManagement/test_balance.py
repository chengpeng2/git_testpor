import unittest

import ddt
import requests

from testCases.back.config import get_cookie

testData1 = [{'assert':'成功!'},
             {'account':'2585683','assert':'成功!'},
             {'account': 'tester', 'assert': '成功!'},
             {'account': '测试徐群节', 'assert': '成功!'},
             {'account': '55555555', 'assert': '成功!'},
             {'account': '13026005868a', 'assert': '成功!'},
             {'unit':'USDT','assert':'成功!'},
             {'walletAddress':'ezbeoswallet', 'assert': '成功!'},
             {'minBalance': 200, 'assert': '成功!'},
             {'maxBalance':10000, 'assert': '成功!'},
             {'minFrozenBalance':10,'assert':'成功!'},
             {'maxFrozenBalance':100,'assert':'成功!'},
             {'minAllBalance': 2, 'assert': '成功!'},
             {'maxAllBalance':200, 'assert': '成功!'}]

@ddt.ddt
class Balances(unittest.TestCase):
    """yue管理"""

    def setUp(self):
        self.headers = {'Cookie':get_cookie()}
        self.url = "https://api.admin.ezbtest.top/admin/member/member-wallet/balance"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_chart(self, value):
        rs = requests.post(url=self.url, headers=self.headers,data=value).json()
        print(rs)
        self.assertEqual(value['assert'], rs['message'])



if __name__ == "__main__":
    unittest.main()
