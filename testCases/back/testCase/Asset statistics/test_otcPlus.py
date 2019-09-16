import unittest
import requests
import ddt


testData1 = [{'assert':'SUCCESS'},
             {'startDate':'2019-07-01','endDate':'2019-09-01','assert':'SUCCESS'},
             {'zones':3,'assert':'SUCCESS'},
             {'zones': 0, 'assert':'SUCCESS'},
             {'zones':{0,3}, 'assert':'SUCCESS'},
             {'area':{'USDT','BAR'},'assert':'SUCCESS'},
             {'baseSymbols': 'BAR', 'assert':'SUCCESS'},
             {'startDate':'2019-07-19','endDate':'2019-08-19','zones':[0,3],'baseSymbols':'USDT,BAR','assert':'SUCCESS'}]



@ddt.ddt
class Charts(unittest.TestCase):
    """币币交易统计查询"""

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
