#########################################################################
# coding: utf-8
#!/usr/bin/python
# File Name: practice_redis.py
# Author: buptxiaomiao
# mail: buptwjh@outlook.com
# Created Time: 五  9/14 00:26:42 2018
#########################################################################

import redis

# 建立redis 连接
r_db = redis.Redis(host='127.0.0.1', port=6379, db=0)

# 字符串
r_db.set('name', '123')
print r_db.get('name')
# 获取不存在的键 返回None
print r_db.get('123')


# 哈希表(字典)
r_db.hset('i_am_user_id','user_name', 'xiaomiao' )
print r_db.hget('i_am_user_id', 'user_name')
try:
    # hget should has 2 args(except 'self')
    print r_db.hget('i_am_user_id')
except:
    pass
# return None
print r_db.hget('i_am_user_id', 'user_age')


