#########################################################################
# coding=utf-8
# File Name: xiaochong.py
# Author: buptxiaomiao
# mail: buptwjh@outlook.com
# Created Time: 三  8/15 01:05:01 2018
#########################################################################
#!/usr/bin/python

import requests

def func():
    url = 'https://www.jianshu.com/p/ead5db32f402'
    for x in range(10):
        r = requests.get(url)
        if r.ok:
            print x


if __name__ == '__main__':
    func()
