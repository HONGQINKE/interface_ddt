# -*- coding: UTF-8 -*-

import logging
import sys,os

def log_print():
    #log_file = os.path.join(os.getcwd(), 'liveappapi.log')
    log_file = './liveappapi.log'
    print(log_file)
    log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
    logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)



if __name__=='__main__':
    log_print()