import os 
import unittest
from datetime import datetime
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('./db_fixture')
from db_fixture import test_data

if __name__ == '__main__':
    print('====AutoTest Start====')
    test_data.init_data()
    test_dir = './test_case'
    test_report_dir = './report'

    discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
    now = datetime.now().strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir + '/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='KuaiGou Test Report',description='Result')
    runner.run(discover)
    fp.close()

    print('====AutoTest Over====')


