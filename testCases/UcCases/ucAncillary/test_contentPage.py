import unittest
import requests
import ddt
from common.readToken import get_token

data1 = [{'assert': '成功'}, {'pageNo': 0, 'assert': 'success'},
         {'pageNo': 1, 'assert': 'success'},
         {'pagesize': 0, 'assert': 'success'},
         {'pageSize': 3,'assert': 'success'}]
data2 = [{'pageSize': 'a','assert': 'Invalid parameter'},
       {'pageNo':'b','assert':'Invalid parameter'}]
@ddt.ddt
class conPage(unittest.TestCase):
    """币种资料列表"""

    def setUp(self):
        self.headers = {"Accept-Language":"zh-CN"}
        self.url = "https://api.ezbtest.top/uc/announcement/page"

    def tearDown(self):
        print('test over')

    @ddt.data(*data1)
    def test_pages(self,value):
        res = requests.post(url=self.url,headers=self.headers,data=value).json()
        print(res)
        self.assertIn('success', res['message'])

    @ddt.data(*data2)
    def test_pages2(self, value):
        res = requests.post(url=self.url, headers=self.headers, data=value).json()
        print(res)
        self.assertIn('Invalid parameter', res['message'])

if __name__ == '__main__':
    unittest.main()
