#!/bin/python3

n = int(input().strip())
c = [int(i) for i in input().split()]

uniques = set(c)

pairs = 0

for unique_int in uniques:
    pairs += c.count(unique_int)//2

print(pairs)
