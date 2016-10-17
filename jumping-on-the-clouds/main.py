#!/bin/python3

n = int(input().strip())
c = [int(i) for i in input().split()]

jumps = 0
position = 0

while position < n -1:
    if position == n-2:
        position += 1
    elif c[position + 2]:
        position += 1
    else:
        position += 2
    jumps += 1

print(jumps)
