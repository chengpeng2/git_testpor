import unittest

import requests


class anId(unittest.TestCase):
    """公告详情"""

    def setUp(self):
        self.headers = {"Accept-Language":"zh-CN"}
        self.url = "https://api.ezbtest.top/ancillary/announcement/121"

    def tearDown(self):
        print('test over')

    def test_announcementId(self):
        res = requests.get(url=self.url,headers=self.headers).json()
        print(res)
        self.assertIn('success', res['message'])


if __name__ == '__main__':
    unittest.main()
