#!/usr/bin/env python3

from multiprocessing import Pool


def count(n):
    while n > 0:
        n -= 1


p = Pool()
p.map(count, [10 ** 8, 10 ** 8])
