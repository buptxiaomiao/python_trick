#########################################################################
# coding: utf-8
#!/usr/bin/python
# File Name: singleton.py
# Author: buptxiaomiao
# mail: buptwjh@outlook.com
# Created Time: 四  8/30 10:48:24 2018
#########################################################################

# 使用__new__
class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# 使用装饰器

def singleton(cls):
    instance = dict()
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance

@singleton
class TEST(object):
    pass



if __name__ == '__main__':
    o1 = Singleton()
    o2 = Singleton()
    print id(o1), id(o2)

    m1 = TEST()
    m2 = TEST()
    print id(m1), id(m2)
