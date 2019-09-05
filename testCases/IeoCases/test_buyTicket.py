import unittest
import requests
import ddt
from common.readToken import get_token

testData1 = [{'ticket_id': 33, 'password': '12345678', 'assert': 500}]
testData2 = [{'ticket_id': 3, 'password': '12345678', 'assert': 500},
             {'ticket_id': '', 'password': '12345678', 'assert': 500},
             {'ticket_id': '!@', 'password': '12345678', 'assert': 500},
             {'ticket_id': '汉字', 'password': '12345678', 'assert': 500},
             {'ticket_id': 'a', 'password': '12345678', 'assert': 500},
             {'ticket_id': 33, 'password': '123456789', 'assert': 500},
             {'ticket_id': 33, 'password': '', 'assert': 500},
             {'ticket_id': 33, 'password': 'aa', 'assert': 500},
             {'ticket_id': 33, 'password': '汉字', 'assert': 500},
             {'ticket_id': 33, 'password': '!@#', 'assert': 500}]


@ddt.ddt
class Tickets(unittest.TestCase):
    """入场券"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token()}
        self.url = "https://api.ezbtest.top/ieo/buy/ticket"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_ticket1(self, value):
        """"用户已购买，请求参数正确，符合规范"""
        rs = requests.post(url=self.url, headers=self.headers, data=value).json()
        print(rs)
        self.assertEqual(value['assert'], rs['code'])

    @ddt.data(*testData2)
    def test_ticket2(self, value):
        """请求参数不正确，不符合规范"""
        rs = requests.post(url=self.url, headers=self.headers, data=value).json()
        print(rs)
        self.assertEqual(value['assert'], rs['code'])


if __name__ == "__main__":
    unittest.main()
