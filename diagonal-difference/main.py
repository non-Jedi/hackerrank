#!/bin/python3

n = int(input().strip())
a = list()

for i in range(n):
    a.append([int(i) for i in input().split()])

diag_1 = 0
diag_2 = 0

for i in range(n):
    diag_1 += a[i][i]
    diag_2 += a[-1-i][i]

print(abs(diag_1-diag_2))
