import unittest
import requests
from common.readToken import get_token
import ddt

testData1 = [{'project_id': '', 'pageNo': '', 'pageSize': '', 'assert': '成功'},
            {'project_id': 95, 'pageNo': 1, 'pageSzie': '2', 'assert': '成功'},
             {'project_id': 95, 'pageNo': 1, 'pageSzie': '-2', 'assert': '成功'},
             {'project_id': 95, 'pageNo': -1, 'pageSzie': '2', 'assert': '成功'}
             ]
testData2 = [{'project_id': 100000, 'pageNo': 2, 'pageSize': 2, 'assert': '失败'},
             {'project_id': '测试', 'pageNo': 1, 'pageSize': 4, 'assert': 'Incoming data error'},
             {'project_id': 'a', 'pageNo': 2, 'pageSize': 3, 'assert': 'Incoming data error'},
             {'project_id': 1.5, 'pageNo': 2, 'pageSize': 2, 'assert': 'Incoming data error'},
             {'project_id': '@#', 'pageNo': '', 'pageSize': '', 'assert': 'Incoming data error'}]
testData3 = [{'project_id': 95, 'pageNo': 'aa', 'pageSize': 3, 'assert': 'Incoming data error'},
             {'project_id': 95, 'pageNo': '测试', 'pageSize': 2, 'assert': 'Incoming data error'},
             {'project_id': 95, 'pageNo': '2,5', 'pageSize': 2, 'assert': 'Incoming data error'},
             {'project_id': 95, 'pageNo': '!@#', 'pageSize': 1, 'assert': 'Incoming data error'}]
testData4 = [{'project_id':'95' , 'pageNo':'1' , 'pageSize': 'q', 'assert': 'Incoming data error'},
             {'project_id': 95, 'pageNo': 1, 'pageSize': '测试', 'assert': 'Incoming data error'},
             {'project_id': 95, 'pageNo': 1, 'pageSize': '2.5', 'assert': 'Incoming data error'},
             {'project_id': 95, 'pageNo': 1, 'pageSize': '！@#', 'assert': 'Incoming data error'}]


@ddt.ddt
class MyProject(unittest.TestCase):
    """我的申购"""

    def setUp(self):
        self.url = 'https://api.ezbtest.top/ieo/project/apply/history'
        self.headers = {"x-auth-token": get_token()}

    def tearDown(self):
        print('test over')

    @ddt.data(*testData1)
    def test_project1(self, value):
        """请求参数合法，返回success"""
        res = requests.post(url=self.url, headers=self.headers, params=value, verify=False).json()
        print(res)
        self.assertIn(value['assert'], res['message'])

    @ddt.data(*testData2)
    def test_project2(self, value):
        """请求参数project_id不合法，返回Internal Error或失败"""
        res = requests.post(url=self.url, headers=self.headers, params=value, verify=False).json()
        print(res)
        self.assertIn(value['assert'], res['message'])

    @ddt.data(*testData3)
    def test_project3(self, value):
        """请求参数pageNo不合法，返回Internal Error"""
        res = requests.post(url=self.url, headers=self.headers, params=value, verify=False).json()
        print(res)
        self.assertIn(value['assert'], res['message'])

    @ddt.data(*testData4)
    def test_project4(self, value):
        """请求参数pageSize不合法，返回Internal Error"""
        res = requests.post(url=self.url, headers=self.headers, params=value, verify=False).json()
        print(res)
        self.assertIn(value['assert'], res['message'])

if __name__== '__main__':
    unittest.main()
