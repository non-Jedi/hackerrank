#!/bin/python3

n = int(input().strip())
a = [int(i) for i in input().split()]

while True:
    if not a:
        break
    print(len(a))
    a = [i - min(a) for i in a if (i - min(a)) > 0]
