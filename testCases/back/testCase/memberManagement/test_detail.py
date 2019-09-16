import unittest

import ddt
import requests

testData1 = [{'id':'2585683','assert':'SUCCESS'},
             {'unit':'USDT','assert':'SUCCESS'},
             {'balanceType':0,'assert':'SUCCESS'},
             {'balanceType': 1, 'assert':'SUCCESS'},
             {'balanceType':2, 'assert':'SUCCESS'}]



@ddt.ddt
class Charts(unittest.TestCase):
    """会员详情"""

    def setUp(self):
        self.url = "https://api.admin.ezbtest.top/admin/changeOtcPlus"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_chart(self, value):
        rs = requests.post(url=self.url, data=value).json()
        print(rs)
        self.assertEqual(value['assert'], rs['message'])



if __name__ == "__main__":
    unittest.main()
