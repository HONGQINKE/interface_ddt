import os 
import unittest
import requests 
from common.getToken import *
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://120.234.18.2:56109/hes/dologin'
        #self.cookies = {'sid':'ddf4ffef-eb15-4be6-a04a-42e0a28db02e'}
        #self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        #               'X-Requested-With':'XMLHttpRequest',
        #                'Accept':'application/json, text/javascript, */*; q=0.01'}

 
    def tearDown(self):
        #print(self.result)
        print('over')

    def login_success(self, username, password):
        payload = {'username': username, 'password': password, 'url': '', 'locale': 'en_US'}
        r = requests.post(self.url, data=payload)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
