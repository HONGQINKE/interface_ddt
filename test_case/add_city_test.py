import os
import requests
import unittest
import sys
sys.path.append('/home/jane/p3_project/kuaigou/db_fixture')
from db_fixture import test_data

class AddCityTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://staging.wechat.kuaigou.co/index.php/Fuwu/ManageCity/addCity.html'
        self.cookies = {'PHPSESSID':'qm82jggp1n1fcrb2g5hddqon50', 'nick_name':'admin', 'username':'admin'}

    def tearDown(self):
        print(self.result)


    def test_add_city_exists(self):
        '''Add exists city'''
        payload = {'city_name':'长沙市','addregion_id':'218'}
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        #self.result = r.text
        self.result = r.json()
        self.assertEqual(self.result['code'],'000002')
        self.assertEqual(self.result['message'],'该城市已经存在')


    def test_add_city_success(self):
        '''Add city success'''
        payload = {'city_name':'衡阳市','addregion_id':'221'}
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        #self.result = r.text
        self.result = r.json()
        self.assertEqual(self.result['code'],'000000')
        self.assertEqual(self.result['message'],'保存成功')

if __name__ == '__main__':
    test_data.init_data()
    unittest.main()
