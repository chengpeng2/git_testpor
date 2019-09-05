import unittest
import requests
import ddt
import json
from common.readToken import get_token
data1=[{"month":3,"amount":"1","assert":"Operation successful"},{"amount": "1", "assert": "Operation successful"},{"month":4,"amount":"1","assert":"Operation successful"}]
data2=[{"month":"","amount": "1", "assert": "Parameter error"},{"month":"汉字","amount":"","assert":"Parameter error"},{"month":'aa',"amount":"1","assert":"Parameter error"},
       {"month":"","amount":"","assert":"Parameter error"},{"month":"3","amount":"","assert":"Parameter error"}]
@ddt.ddt
class Tickets(unittest.TestCase):
    """用户BAR锁仓"""

    def setUp(self):
        self.headers = {"x-auth-token":get_token(),
                        "Accept-Language":"en-US",
                        #en-US
                        "Content-Type":"application/json"}
        self.url = "https://api.ezbtest.top/uc/bar/lock"

    def tearDown(self):
        print('test over')
    @ddt.data(*data1)
    def test_lock1(self,value):
        """"请求参数正确，用户锁仓成功"""
        rs = requests.post(url=self.url, headers=self.headers, data=json.dumps(value)).json()
        print(rs)
        self.assertIn(rs['message'],value['assert'])

    @ddt.data(*data2)
    def test_lock2(self, value):
        """"请求参数错误，用户锁仓失败"""
        rs = requests.post(url=self.url, headers=self.headers, data=value).json()
        print(rs)
        self.assertIn(rs['message'], value['assert'])


if __name__ =="__main__":
    unittest.main()