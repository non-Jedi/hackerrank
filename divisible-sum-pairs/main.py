#!/bin/python3

n, k = map(int, input().split())
a = map(int, input().split())

remainders = [i % k for i in a]

count = 0
for index, ai in enumerate(remainders):
    for aj in remainders[index+1:]:
        if (ai + aj == k) or (ai + aj == 0):
            count += 1

print(count)
