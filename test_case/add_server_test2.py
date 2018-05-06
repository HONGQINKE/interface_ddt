# -*- coding: UTF-8 -*-

import requests

if __name__ == "__main__":

    s = requests.session()

    headers = {
        "X-Requested-With":"XMLHttpRequest",
        #"Content-Type":"application/x-www-form-urlencoded",
        }

    url_login,url_test = "http://120.234.18.2:56109/hes/dologin",\
                         "http://120.234.18.2:56109/hes/fep/adds"
    login_data = {
        'username': '001',
        'password': 123456,
        'url': '',
        'locale': 'en_US'
    }

    f = s.post(url_login,data=login_data,allow_redirects=False)

    test_data = {
        "svrName": "ServerA",
        'svrIp':'11.11.11.11',
        'svrUport': '1111',
        'svrType':'1',
        'svrStatus':'0',
        'svrDesc':'test'
    }

    r = s.post(url_test,data=test_data,headers=headers)

    res_value = r.text

    print(res_value)