# -*- coding: UTF-8 -*-

import requests
from common import getToken
import logging
from common import log_print
import unittest


class serverTest:


    def test_add_server(svrName,svrIp,svrUport,svrType,svrStatus,svrDesc,expect_value):

        '''
        payload = {
            "svrName": "AT_ServerA",
            'svrIp': '11.11.11.11',
            'svrUport': '1111',
            'svrType': '1',
            'svrStatus': '0',
            'svrDesc': 'test'
        }

        '''
        cookie = getToken.get_session()
        headers = {
            "X-Requested-With": "XMLHttpRequest",
        }

        url_test = "http://120.234.18.2:56109/hes/fep/adds"

        payload = {
            "svrName": svrName,
            'svrIp': svrIp,
            'svrUport': svrUport,
            'svrType': svrType,
            'svrStatus': svrStatus,
            'svrDesc': svrDesc
        }

        r = requests.post(url_test, data=payload, headers=headers, cookies=cookie)

        result = r.text

        assert result==expect_value



if __name__ == "__main__":
    log_print.log_print()
    serverTest.test_add_server("AT_ServerA",'11.11.11.11','1111','1','0','test','{"success":true}')
    logging.info('Add server successfully')

