import unittest
import requests
import ddt

data1 = [{'assert': '成功'}, {'pageNo': 0, 'assert': 'success'},
         {'pageNo': 1, 'assert': 'success'},
         {'pagesize': 0, 'assert': 'success'},
         {'pageSize': 3,'assert': 'success'},
         {'platform': 10, 'assert': 'sucess'},
         {'type':10,'asssert':'success'}]
@ddt.ddt
class page(unittest.TestCase):
    """公告列表"""

    def setUp(self):
        self.headers = {"Accept-Language":"zh-CN"}
        self.url = "https://api.ezbtest.top/uc/announcement/page"

    def tearDown(self):
        print('test over')



    @ddt.data(*data1)
    def test_pages(self,value):
        res = requests.post(url=self.url,headers=self.headers,params=value).json()
        print(res)
        self.assertIn('success', res['message'])


if __name__ == '__main__':
    unittest.main()
