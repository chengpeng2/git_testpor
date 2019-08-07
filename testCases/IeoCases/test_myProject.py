# import unittest
# import requests
# import ddt
#
# testData=[{'project':'','pageNo':'','pageSize':'','assert': 'success'},
#           {'project':1,'pageNo':'','pageSzie':'','assert': 'success'},
#           {'project':100000,'pageNo':2,'pageSzie':2,'assert': 0},
#           {'project': '测试', 'pageNo': '', 'pageSize': ''},
#           {'project': 'a', 'pageNo': 2, 'pageSzie': 3},
#           {'project': 1.5, 'pageNo': 2, 'pageSzie': 2},
#           {'project': '@#', 'pageNo': '', 'pageSize': ''},
#           {'project': 1, 'pageNo': 2, 'pageSzie': 3},
#           {'project': 100000, 'pageNo': 2, 'pageSzie': 2},
#           {'project': '', 'pageNo': '', 'pageSize': ''},
#           {'project': 1, 'pageNo': 2, 'pageSzie': 3},
#           {'project': 100000, 'pageNo': 2, 'pageSzie': 2},
#           ]
# @ddt.data
# class MyProject(unittest.TestCase):
