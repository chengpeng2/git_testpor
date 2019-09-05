import unittest
import requests
import ddt
from common.readToken import get_token

# 测试数据
testData1 = [{'type': '', 'pageNo': '', 'pageSize': '', 'assert': '成功'},
             {'type': '0', 'pageNo': 1, 'pageSize': 5, 'assert': '成功'},
             {'type': '1', 'pageNo': 2, 'pageSize': 6, 'assert': '成功'},
             {'type': '1', 'pageNo': '1', 'pageSize': -6, 'assert': '成功'},
             {'type': '2', 'pageNo': 3, 'pageSize': 3, 'assert': '成功'}]
testData2 = [{'type': '3', 'pageNo': 1, 'pageSize': 5, 'assert': 0},
             {'type': 'a', 'pageNo': 1, 'pageSize': 5, 'assert': 0},
             {'type': '!', 'pageNo': 1, 'pageSize': 5, 'assert': 0},
             {'type': '-1', 'pageNo': 1, 'pageSize': 5, 'assert': 0},
             {'type': '1.2', 'pageNo': 1, 'pageSize': 5, 'assert': 0},
             {'type': '测试', 'pageNo': 1, 'pageSize': 5, 'assert': 0}]
testData3 = [{'type': '1', 'pageNo': 'b', 'pageSize': 6, 'assert': 'request parameter error.'},
             {'type': '1', 'pageNo': '!@', 'pageSize': 6, 'assert': 'request parameter error.'},
             {'type': '1', 'pageNo': '测试', 'pageSize': 6, 'assert': 'request parameter error.'},
             {'type': '2', 'pageNo': 3, 'pageSize': 'c', 'assert': 'request parameter error.'},
             {'type': '2', 'pageNo': 3, 'pageSize': '*&%', 'assert': 'request parameter error.'},
             {'type': '2', 'pageNo': 3, 'pageSize': '测试', 'assert': 'request parameter error.'}]
testData4 = [{'type': '1', 'pageNo': '-9', 'pageSize': 6, 'assert': []}]


#
#
@ddt.ddt
class ProjectLists(unittest.TestCase):
    """项目列表"""

    def setUp(self):
        self.headers = {"x-auth-token": get_token()}
        self.url = "https://api.ezbtest.top/ieo/project/list"

    def tearDown(self):
        print('test over')

    # @unittest.skip('pass')
    @ddt.data(*testData1)
    def test_list1(self, value):
        """请求参数符合接口规范，返回成功"""
        rs = requests.post(url=self.url, headers=self.headers, params=value,verify=False).json()
        print(rs)
        self.assertTrue(value['assert'] in rs['message'])

    #@unittest.skip('pass')
    @ddt.data(*testData2)
    def test_list2(self, value):
        """type参数为3或a或特殊字符，返回项目数量页数为0"""
        rs1 = requests.post(url=self.url, headers=self.headers, params=value,verify=False).json()
        print(rs1)
        self.assertEqual(value['assert'], rs1['data']['total'])

    #@unittest.skip('pass')
    @ddt.data(*testData3)
    def test_list3(self, value):
        """pageNo、pageSize参数为汉字、负数、特殊字符，提示请求参数错误"""
        rs2 = requests.post(url=self.url, headers=self.headers, params=value,verify=False).json()
        print(rs2)
        self.assertIn(value['assert'], rs2['message'])

    @ddt.data(*testData4)
    def test_list4(self, value):
        """pageSize参数负数，返回数据为空"""
        rs3 = requests.post(url=self.url, headers=self.headers, params=value,verify=False).json()
        print(rs3)
        self.assertEqual(value['assert'], rs3['data']['content'])


if __name__ == "__main__":
    unittest.main()
