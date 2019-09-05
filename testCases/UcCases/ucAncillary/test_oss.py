import requests
from urllib3 import encode_multipart_formdata
from common.readToken import get_token
import unittest


class Os(unittest.TestCase):
    def setUp(self):
         self.file_name = "BAR.png"
         self.file_path = "C:\\Users\Administrator\Desktop\BAR.png"


    def tearDown(self):
        print('over')

    def test_up1(self):
        with open(self.file_path, 'rb') as f:
            file = {"file": (self.file_name, f.read())}
            encode_data = encode_multipart_formdata(file)
            file_data = encode_data[0]
            header = {'Content-Type': encode_data[1],"x-auth-token":get_token}
            url = "https://api.ezbtest.top/uc/upload/oss/image"
            res = requests.post(url, headers=header, data=file_data).json()
            print(res)

    def test_up2(self):
        with open(self.file_path, 'rb') as f:
            file = {"file": (self.file_name, f.read())}
            encode_data = encode_multipart_formdata(file)
            file_data = encode_data[0]
            header = {'Content-Type': encode_data[1], "x-auth-token": get_token}
            url = "https://api.ezbtest.top/ancillary/upload/oss/image"
            res = requests.post(url, headers=header, data=file_data).json()
            print(res)
if __name__ =='__main__':
    unittest.main()