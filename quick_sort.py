#########################################################################
# coding: utf-8
# File Name: quick_sort.py
# Author: buptxiaomiao
# mail: buptwjh@outlook.com
# Created Time: 五  8/17 12:36:04 2018
#########################################################################
#!/usr/bin/python

def quick_sort_(arr, l, r):
    if l >= r:
        return 
    low = l
    high = r
    key = arr[low]
    while l < r:
        while l < r and arr[r] > key:
            r -= 1
        arr[l] = arr[r]
        while l < r and arr[l] <= key:
            l += 1
        arr[r] = arr[l]
    arr[r] = key
    quick_sort_(arr, low, l-1)
    quick_sort_(arr, r+1, high)

if __name__ == '__main__':
    a = [4, 2, 5, 2, 3, 8, 10, 5, 1]
    print a
    quick_sort_(a, 0, len(a) -1)
    print a
