import unittest
import requests
from common.readToken import get_token
testData1=[{'orderId':'E224931084918333440','assert':'success'},{'orderId':'E224931084918333440','assert':'success'}]
class Adds(unittest.TestCase):
    """取消下单"""

    def setUp(self):
        self.headers = {"x-auth-token":"860dbe4f-1441-43c8-8f66-5390bc2bba79"}


    def tearDown(self):
        print('test over')

    def test_adds1(self,value):
        """请求参数合法"""
        self.url = "https://api.ezbtest.top/exchange/order/cancel/"
        res = requests.post(self.url+'value[]', headers=self.headers).json()
        print(res)
        self.assertIn('success', res['message'])


if __name__ == '__main__':
    unittest.main()
