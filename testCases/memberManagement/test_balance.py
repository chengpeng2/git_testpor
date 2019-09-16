import unittest

import ddt
import requests

from common.readCookie import get_cookie

testData1 = [{'assert':'Success!'},
             {'account':'2585683','assert':'Success!'},
             {'account': 'tester', 'assert': 'Success!'},
             {'account': '测试徐群节', 'assert': 'Success!'},
             {'account': '55555555', 'assert': 'Success!'},
             {'account': '13026005868a', 'assert': 'Success!'},
             {'unit':'USDT','assert':'Success!'},
             {'walletAddress':'ezbeoswallet', 'assert': 'Success!'},
             {'minBalance': 200, 'assert': 'Success!'},
             {'maxBalance':10000, 'assert': 'Success!'},
             {'minFrozenBalance':10,'assert':'Success!'},
             {'maxFrozenBalance':100,'assert':'Success!'},
             {'minAllBalance': 2, 'assert': 'Success!'},
             {'maxAllBalance':200, 'assert': 'Success!'}]

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
