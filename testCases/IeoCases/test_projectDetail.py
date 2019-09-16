import unittest

import ddt
import requests

from common.readToken import get_token

testData1 = [{'project_id': '', 'assert': 'request parameter error.'}, {'project_id': 'aa', 'assert': '失败'},
             {'project_id': '!', 'assert': '失败'}, {'project_id': '测试', 'assert': '失败'},
             {'project_id': ' ', 'assert': '失败'}, {'project_id': 11111111, 'assert': '失败'}]
testData2=[{'project_id': 1, 'assert': '失败'},{'project_id': 25, 'assert': '成功'}]

@ddt.ddt
class ProjectDetail(unittest.TestCase):
    """项目详情"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token()}
        self.url = "https://api.ezbtest.top/ieo/project/detail"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_detail1(self, value):
        """project_id类型为空、特殊字符、汉字、字母、空字符串"""
        res = requests.post(url=self.url, headers=self.headers, params=value,verify=False).json()
        print(res)
        self.assertIn(value['assert'], res['message'])

    @ddt.data(*testData2)
    def test_detail2(self, value):
        """project_id类型为空、特殊字符、汉字、字母、空字符串"""
        res = requests.post(url=self.url, headers=self.headers, params=value, verify=False).json()
        print(res)
        self.assertIn(value['assert'], res['message'])



if __name__ == '__main__':
    unittest.main()
