#########################################################################
# coding: utf-8
#!/usr/bin/python
# File Name: fab.py
# Author: buptxiaomiao
# mail: buptwjh@outlook.com
# Created Time: 三  8/29 23:19:20 2018
#########################################################################

def fab(max_num=100):
    i, j = 0, 1
    while j < max_num:
        yield j
        i, j = j, i+j

if __name__ == '__main__':
    print [x for x in fab()]
