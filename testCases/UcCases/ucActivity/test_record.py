import unittest
import requests
import ddt
from common.readToken import get_token


class Record(unittest.TestCase):
    """用户推广好友记录"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token()}
        self.url = "https://api.ezbtest.top/uc/promotion/record"

    def tearDown(self):
        print('test over')

    def test_records(self):
        res = requests.post(url=self.url, headers=self.headers,verify=False).json()
        print(res)
        self.assertIn('success', res['message'])

if __name__ =='__main__':
    unittest.main()