#!/usr/bin/python
# _*_ coding=utf-8 _*_

#打印水仙花数

for n in range(100,1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i **3 + j ** 3 + k ** 3:
         print n,
