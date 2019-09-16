import unittest

import ddt
import requests

data1 = [{'assert': 'coin content not exist'}, {'unit': 'BAR','assert': 'success'},
         {'unit': 'BAR','assert': 'success'}]
@ddt.ddt
class Details(unittest.TestCase):
    """币种资料详情"""

    def setUp(self):
        self.headers={'language': 'zh-CN',}
        self.url = "https://api.ezbtest.top/ancillary/coin-content/detail"

    def tearDown(self):
        print('test over')

    @ddt.data(*data1)
    def test_ad1(self, value):
        res = requests.post(url=self.url, headers=self.headers,data=value).json()
        print(res)
        self.assertIn(value['assert'], res['message'])

if __name__ == '__main__':
    unittest.main()
