import requests
from test_case.login_test import LoginTest


class my_session():

    def get_session(self):
        '''get session id after login successfully'''
        r = requests.post(url='http://120.234.18.2:56109/hes/dologin',
                          data={'username': '001', 'password': 123456, 'url': '', 'locale': 'en_US'})
        print(r.cookies.get_dict())
        return r.cookies.get_dict()
