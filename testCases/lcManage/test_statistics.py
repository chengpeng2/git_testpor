import unittest

import ddt
import requests

from common.readCookie import get_cookie


class Pages(unittest.TestCase):
    """后台统计"""
 
    def setUp(self):
        self.headers = {'Cookie':get_cookie()}
        self.url = "https://api.admin.ezbtest.top/admin/otc/advertise/statistics"

    def tearDown(self):
        print('test over')


    def test_pages(self):
        rs = requests.post(url=self.url, headers=self.headers).json()
        print(rs)
        self.assertEqual('SUCCESS', rs['message'])



if __name__ == "__main__":
    unittest.main()
