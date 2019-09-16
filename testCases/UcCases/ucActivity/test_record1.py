import unittest

import requests

from common.readToken import get_token


class Record1(unittest.TestCase):
    """推广奖励记录"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token()}
        self.url = "https://api.ezbtest.top/uc/promotion/reward/record"

    def tearDown(self):
        print('test over')

    def test_records(self):
        res = requests.post(url=self.url, headers=self.headers,verify=False).json()
        print(res)
        self.assertIn('success', res['message'])

if __name__ =='__main__':
    unittest.main()