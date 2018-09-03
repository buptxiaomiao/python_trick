#########################################################################
# coding: utf-8
#!/usr/bin/python
# File Name: reverse_link_list.py
# Author: buptxiaomiao
# mail: buptwjh@outlook.com
# Created Time: 二  9/ 4 01:29:05 2018
#########################################################################

# 单链表反转
class Node(object):
    """ 节点 """
    def __init__(self, data, node):
        self.data = data
        self.next = node

    def __str__(self):
        return 'id:%s, ' % id(self) + 'data: %s, ' % self.data + 'next: %s' % id(self.next)

def print_link_list(root):
    """打印链表"""
    if not root:
        return 
    while root:
        print root
        root = root.next
    return 

def reverse_link_list(root):
    """反转链表"""
    print 'after reversed link list....'
    head = None
    _head = root
    while _head:
        tmp = _head.next
        _head.next = head
        head = _head
        _head = tmp
    
    print_link_list(head)
    return head

def generate_link_list(num):
    """生成链表"""
    print 'generate link list: ...'
    if num <=0:
        return
    l = [Node(x, None) for x in xrange(num)]
    for x in xrange(len(l)):
        if x + 1 < len(l):
            l[x].next = l[x+1]
    print_link_list(l[0])
    return l

if __name__ == '__main__':
    l = generate_link_list(10)

    reverse_link_list(l[0])
