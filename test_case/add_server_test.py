import os 
import unittest
import requests 

class AddCarTypeTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://120.234.18.2:56109/hes/fep/adds'
        self.cookies = {'sid':'d9db6779-10d5-437d-b62b-930ef021dcad'}
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                        'X-Requested-With':'XMLHttpRequest',
                        'Accept':'application/json, text/javascript, */*; q=0.01'}

 
    def tearDown(self):
        #print(self.result)
        print('over')

    def test_add_car_type_success(self):
        payload = {'svrName':'ServerA','svrIp':'11.11.11.11','svrUport':1111,'svrType':1,'svrStatus':0,'svrDesc':'test'}
        r = requests.post(self.url,data=payload,cookies=self.cookies,headers=self.headers)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result['success'], True)

if __name__ == '__main__':
    unittest.main()
