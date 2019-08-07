import requests
import unittest
import ddt
from common.readToken import get_token

testData = [{'project_id': '', 'assert': '请求参数错误'}, {'project_id': 'aa', 'assert': '失败'},
            {'project_id': '!', 'assert': '失败'}, {'project_id': '测试', 'assert': '失败'},
            {'project_id': ' ', 'assert': '失败'}, {'project_id': 11111111, 'assert': '失败'},
            {'project_id': '1', 'assert': 'success'}]


@ddt.ddt
class ProjectDetail(unittest.TestCase):
    """项目详情接口"""
    def setUp(self):
        self.headers = {"x-auth-token": get_token()}
        self.url = "https://api.ezbtest.top/ieo/project/detail"


    def tearDown(self):
        print('test over')

    @ddt.data(*testData)
    def test_details(self, value):
      res = requests.post(url=self.url, headers=self.headers, params=value).json()
      #print(res)
      self.assertIn(value['assert'], res['message'])


if __name__ == '__main__':
    unittest.main()
