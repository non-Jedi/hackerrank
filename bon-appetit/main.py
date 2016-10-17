#!/bin/python3

n, k = map(int, input().split())
c = [int(i) for i in input().split()]
b = int(input().strip())

agreed = sum(c[:k] + c[k+1:])//2

if agreed == b:
    print('Bon Appetit')
else:
    print(b - agreed)
