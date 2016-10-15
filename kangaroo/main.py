#!/bin/python3

x1, v1, x2, v2 = [int(i) for i in input().split()]

if v1 == v2:
    if x1 == x2:
        print('YES')
    else:
        print('NO')

elif not (x1-x2)%(v2-v1) and ((x1-x2)/(v2-v1) >= 0):
    print('YES')
else:
    print('NO')
