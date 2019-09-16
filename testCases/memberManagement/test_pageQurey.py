import unittest

import ddt
import requests

from common.readCookie import get_cookie

testData1 = [{'assert':'SUCCESS'},
             {'account':'2585683','assert':'SUCCESS'},
             {'account': '徐群节', 'assert': 'SUCCESS'},
             {'account': '13026005868a', 'assert': 'SUCCESS'},
             {'startTime':'2019-07-19','assert':'SUCCESS'},
             {'endTime':'2019-08-19','assert':'SUCCESS'},
             {'commonStatus':0,'assert':'SUCCESS'},
             {'commonStatus':1, 'assert': 'SUCCESS'},
             {'releaseMultiple':1.5,'assert':'SUCCESS'},
             {'memberLevel':0,'assert':'SUCCESS'},
             {'memberLevel': 1, 'assert': 'SUCCESS'},
             {'memberLevel': 2, 'assert': 'SUCCESS'},
             {'memberLevel': 3, 'assert': 'SUCCESS'},
             {'inviteAccount':'2585683','assert': 'SUCCESS'},
             {'inviteAccount': '徐群节', 'assert': 'SUCCESS'},
             {'unit':'USDT','assert':'SUCCESS'},
             {'startNumber':222.2,'assert':'SUCCESS'},
             {'endNumber':2222.2,'assert':"SUCCESS"},
             {'eqNumber':333.3,'assert':'SUCCESS'}]

@ddt.ddt
class Pages(unittest.TestCase):
    """会员管理查询"""

    def setUp(self):
        self.headers = {'Cookie': get_cookie()}
        self.url = "https://api.admin.ezbtest.top/admin/member/page-query"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_chart(self, value):
        rs = requests.post(url=self.url, headers=self.headers,data=value).json()
        print(rs)
        self.assertEqual(value['assert'], rs['message'])



if __name__ == "__main__":
    unittest.main()
