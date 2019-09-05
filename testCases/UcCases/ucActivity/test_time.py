import unittest
import requests
import ddt
from common.readToken import get_token


class times(unittest.TestCase):
    """获取当前时间信息"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token()}
        self.url = "https://api.ezbtest.top/uc/member/time"

    def tearDown(self):
        print('test over')

    def test_records(self):
        res = requests.get(url=self.url, headers=self.headers,verify=False).json()
        print(res)
        self.assertIn('success', res['message'])

if __name__ =='__main__':
    unittest.main()