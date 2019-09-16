import unittest
import requests


class Excel(unittest.TestCase):
    """账户盈利统计导出次数统计"""

    def setUp(self):
        self.url = "https://api.admin.ezbtest.top/admin/profit/total-assets/out/excel"

    def tearDown(self):
        print('test over')


    def test_excel(self):
        code = requests.get(url=self.url).status_code
        print(code)
        self.assertEqual(code,200)


if __name__ == "__main__":
    unittest.main()
