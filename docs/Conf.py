#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_NAME=os.path.basename(BASE_DIR)

if __name__=='__main__':
    print(BASE_DIR)
    print(BASE_NAME)