import unittest
import requests
import ddt
testData=[{'assert':'SUCCESS'},
          {'id':1,'assert':'SUCCESS'},
          {'state':0,'assert':'SUCCESS'},
          {'state':1, 'assert':'SUCCESS'},
          {'state':2, 'assert':'SUCCESS'},
          {'tradeType':'BUY','assert':'SUCCESS'},
          {'tradeType': 'SELL', 'assert':'SUCCESS'},
          {'startDate': '2019-07-19', 'endDate': '2019-08-19','assert':'SUCCESS'},
          {'id':2,'state':0,'tradeType':'BUY','startDate': '2019-07-19', 'endDate': '2019-08-19', 'assert': 'SUCCESS'}]
@ddt.ddt
class Find(unittest.TestCase):
    """市值机器人查询"""

    def setUp(self):
        self.url = "https://api.admin.ezbtest.top/admin/changeOtcPlus"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData)
    def test_chart(self, value):
        rs = requests.post(url=self.url, data=value).json()
        print(rs)
        self.assertEqual(value['assert'], rs['message'])


if __name__ == "__main__":
    unittest.main()
