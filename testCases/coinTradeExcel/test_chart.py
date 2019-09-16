import unittest
import requests
import ddt


testData1 = [{'assert':0},
             {'startDate':'2019-07-01','endDate':'2019-09-01','assert': 0},
             {'zones':3,'assert':0},
             {'zones': 0, 'assert': 0},
             {'zones':{0,3}, 'assert':0},
             {'baseSymbols':{'BAR','USDT'},'assert':0 },
             {'baseSymbols': 'BAR', 'assert':0},
             {'startDate':'2019-07-19','endDate':'2019-08-19','zones':[0,3],'baseSymbols':'USDT,BAR','assert':0 }]



@ddt.ddt
class Charts(unittest.TestCase):
    """币币交易成交量价格"""

    def setUp(self):

        self.url = "https://api.admin.ezbtest.top/admin/index/statistics/exchange-statistics-turnover-chart-new"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_chart(self, value):
        rs = requests.post(url=self.url, data=value).json()
        print(rs)
        self.assertEqual(value['assert'], rs['code'])



if __name__ == "__main__":
    unittest.main()
