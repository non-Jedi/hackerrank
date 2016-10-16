#!/bin/python3

n, m, k = map(int, input().split())
t = [0] * n
a = [[]] * n
for i in range(n):
    a[i] = [int(a) for a in input().split()]
    t[i] = a[i].pop(0)
roads = [0] * m
for i in range(m):
    roads[i] = [int(a) for a in input().split()]
