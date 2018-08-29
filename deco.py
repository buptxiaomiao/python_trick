#########################################################################
# coding: utf-8
#!/usr/bin/python
# File Name: deco.py
# Author: buptxiaomiao
# mail: buptwjh@outlook.com
# Created Time: 四  8/30 01:50:37 2018
#########################################################################
import time

def timeit(msg):
    def out_wraper(func):
        def in_wraper(*args, **kargs):
            a = time.time()
            res = func(*args, **kargs)
            b = time.time()
            print 'msg: %s' % msg
            print u'%s run %s seconds...' % (func.__name__, b - a)
            return res
        return in_wraper
    return out_wraper

@timeit('hahaha')
def f():
    x = [x for x in xrange(10000)]
    print x[:201:2]

if __name__ == '__main__':
    f()

