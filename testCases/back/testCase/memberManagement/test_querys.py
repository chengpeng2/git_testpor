import unittest

import ddt
import requests

from testCases.back.config import get_cookie

testData1 = [{'assert':'SUCCESS'},
             {'account':'2585683','assert':'SUCCESS'},
             {'account': 'tester', 'assert': 'SUCCESS'},
             {'account': '测试徐群节', 'assert': 'SUCCESS'},
             {'account': '55555555', 'assert': 'SUCCESS'},
             {'account': '13026005868a', 'assert': 'SUCCESS'},
             {'auditStatus':0,'assert':'SUCCESS'},
             {'auditStatus': 1, 'assert': 'SUCCESS'},
             {'auditStatus': 2, 'assert': 'SUCCESS'},
             {'cardNo':'55555555','assert':'SUCCESS'},
             {'validationType':1,'assert':'SUCCESS'},
             {'validationType': 2, 'assert': 'SUCCESS'},
             {'registryStartDate':'2019-07-19', 'assert': 'SUCCESS'},
             {'registryEndDate':'2019-08-19', 'assert': 'SUCCESS'}]

@ddt.ddt
class PagesQuerys(unittest.TestCase):
    """实名管理"""

    def setUp(self):
        self.headers = {'Cookie':get_cookie()}
        self.url = "https://api.admin.ezbtest.top/admin/member/member-application/page-query"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_chart(self, value):
        rs = requests.post(url=self.url, headers=self.headers,data=value).json()
        print(rs)
        self.assertEqual(value['assert'], rs['message'])



if __name__ == "__main__":
    unittest.main()
