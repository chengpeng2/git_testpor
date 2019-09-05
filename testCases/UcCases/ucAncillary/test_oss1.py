import requests
from urllib3 import encode_multipart_formdata
from common.readToken import get_token
import unittest, base64


class Os(unittest.TestCase):
    def setUp(self):
        self.file_name = "BAR.png"
        self.file_path = "C:\\Users\Administrator\Desktop\BAR.png"

    def tearDown(self):
        print('over')

    def test_up2(self):
        with open(self.file_path, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            print(base64_data)
            data = {'base64Data': 'data:image/png;base64,' + base64.b64encode(f.read()).decode()}
            header = {'client': 'web', 'Content-Type': "application/x-www-form-urlencoded",
                      "x-auth-token": get_token}
            url = "https://api.ezbtest.top/uc/upload/oss/base64"
            res = requests.post(url, headers=header, data=data).json()
            print(res)

    def test_up3(self):
        with open(self.file_path, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            print(base64_data)
            data = {'base64Data': 'data:image/png;base64,' + base64.b64encode(f.read()).decode()}
            header = {'client': 'web', 'Content-Type': "application/x-www-form-urlencoded",
                      "x-auth-token": get_token}
            url = "https://api.ezbtest.top/ancillary/upload/oss/base64"
            res = requests.post(url, headers=header, data=data).json()
            print(res)


if __name__ == '__main__':
    unittest.main()
