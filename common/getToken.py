import requests
#from test_case.login_test import LoginTest



def get_session():

    s = requests.session()

    #headers = {
    #   "X-Requested-With": "XMLHttpRequest",
        # "Content-Type":"application/x-www-form-urlencoded",
    #}

    url_login="http://120.234.18.2:56109/hes/dologin"

    login_data = {
        'username': 'PQ001',
        'password': 12345678,
        'url': '',
        'locale': 'en_US'
    }


    '''302 response need to add allow_redirect=False to forbid redirect'''
    cookie = s.post(url_login, data=login_data, allow_redirects=False).cookies
    return cookie


if __name__=='__main__':
    get_session()