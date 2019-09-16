import unittest

import ddt
import requests

from common.readCookie import get_cookie

testData1 = [{'assert':'SUCCESS'},
             {'advertiseType':0,'assert':'SUCCESS'},
             {'advertiseType':1,'assert': 'SUCCESS'},
             {'complainant': '冷雨潇', 'assert': 'SUCCESS'},
             {'complainant': '18530939843', 'assert': 'SUCCESS'},
             {'complainant': '', 'assert': 'SUCCESS'},
             {'createTimeStart':'2019-07-19','assert':'SUCCESS'},
             {'createTimeEnd':'2019-08-19','assert':'SUCCESS'},
             {'status':0,'assert':'SUCCESS'},
             {'status':1, 'assert': 'SUCCESS'},
             {'status': 2, 'assert': 'SUCCESS'},
             {'unit':'USDT','assert':'SUCCESS'}]

@ddt.ddt
class Pages(unittest.TestCase):
    """后台申诉"""

    def setUp(self):
        self.headers = {'Cookie': get_cookie()}
        self.url = "https://api.admin.ezbtest.top/admin/otc/advertise/page-query"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def pages(self, value):
        rs = requests.post(url=self.url, headers=self.headers,data=value).json()
        print(rs)
        self.assertEqual(value['assert'], rs['message'])



if __name__ == "__main__":
    unittest.main()
