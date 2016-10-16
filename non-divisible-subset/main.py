#!/bin/python3

n, k = [int(i) for i in input().split()]
vals = set([int(i) for i in input().split()])

remainders = dict()

for integer in vals:
    try:
        remainders[integer % k] += 1
    except KeyError:
        remainders[integer % k] = 1

count = 0

if 0 in remainders:
    count += 1
    remainders.pop(0)

for key in remainders:
    try:
        if key == k-key:
            count += 1
            remainders[key] = 0
        elif remainders[key] >= remainders[k-key]:
            count += remainders[key]
            remainders[key], remainders[k-key] = (0,0)
    except KeyError:
        count += remainders[key]

print(count)
