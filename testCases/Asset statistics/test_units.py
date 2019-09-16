import unittest
import requests
import ddt

class Units(unittest.TestCase):
    """主币种查询"""

    def setUp(self):
        self.url = "https://api.admin.ezbtest.top/admin/changeOtc/units"

    def tearDown(self):
        print('test over')

    def test_chart(self):
        rs = requests.post(url=self.url).json()
        print(rs)
        self.assertEqual('SUCCESS', rs['message'])


if __name__ == "__main__":
    unittest.main()
