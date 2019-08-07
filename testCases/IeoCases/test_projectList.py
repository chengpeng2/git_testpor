import unittest
import requests
import ddt
from common.readToken import get_token

# 测试数据
testData1 = [{'type': '', 'pageNo': '', 'pageSize': '', 'assert': 'success'},
             {'type': '0', 'pageNo': 1, 'pageSize': 5, 'assert': 'success'},
             {'type': '1', 'pageNo': 2, 'pageSize': 6, 'assert': 'success'},
             {'type': '2', 'pageNo': 3, 'pageSize': 3, 'assert': 'success'}]
testData2 = [{'type': '3', 'pageNo': 1, 'pageSize': 5, 'assert': 0},
              {'type': 'a', 'pageNo': 1, 'pageSize': 5, 'assert': 0},
             {'type':'!',  'pageNo': 1, 'pageSize': 5, 'assert': 0},
             {'type': '-1', 'pageNo': 1, 'pageSize': 5, 'assert': 0},
             {'type': '1.2','pageNo': 1, 'pageSize': 5, 'assert': 0},
             {'type': '测试', 'pageNo': 1, 'pageSize': 5, 'assert': 0}]
testData3 = [{'type': '1', 'pageNo': 'b', 'pageSize': 6, 'assert': '请求参数错误'},
             {'type': '1', 'pageNo': '!@', 'pageSize': 6, 'assert': '请求参数错误'},
             {'type': '1', 'pageNo': '-9', 'pageSize': 6, 'assert': '请求参数错误'},
             {'type': '1', 'pageNo': '测试', 'pageSize': 6, 'assert': '请求参数错误'},
             {'type': '2', 'pageNo': 3, 'pageSize': 'c', 'assert': '请求参数错误'},
             {'type': '2', 'pageNo': 3, 'pageSize': '-2', 'assert': '请求参数错误'},
             {'type': '2', 'pageNo': 3, 'pageSize': '*&%', 'assert': '请求参数错误'},
             {'type': '2', 'pageNo': 3, 'pageSize': '测试', 'assert': '请求参数错误'}]
#
#
@ddt.ddt
class ProjectList(unittest.TestCase):
    """项目列表"""
    def setUp(self):
        self.headers = {"x-auth-token": get_token()}
        self.url = "https://api.ezbtest.top/ieo/project/list"

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_project1(self, value):
        """请求参数符合接口规范，返回success"""
        rs = requests.post(self.url, self.headers, params=value).json()
        #print(rs)
        self.assertTrue(value['assert'] in rs['message'])

    @ddt.data(*testData2)
    def test_project2(self, value):
        """type参数为3或a或特殊字符，返回项目数量页数为0"""
        rs1 = requests.post(self.url, self.headers, params=value).json()
        #print(rs1)
        self.assertEqual(value['assert'], rs1['data']['total'])

    @ddt.data(*testData3)
    def test_project3(self, value):
        """pageNo、pageSize参数为汉字、负数、特殊字符，提示请求参数错误"""
        rs2 = requests.post(self.url, self.headers, params=value).json()
       # print(rs2)
        self.assertIn(value['assert'], rs2['message'])

if __name__ == "__main__":
    unittest.main()
