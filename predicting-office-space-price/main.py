#!/bin/python3
import numpy as np

f, n = map(int, input().split())
x = np.empty((n, f+1), dtype = float)
for i in range(n):
    x[i] = [float(i) for i in input().split()]
t = int(input().strip())
tests = np.empty((t, f), dtype = float)
for i in range(t):
    tests[i] = [float(i) for i in input().split()]

y = x[:,-1]
x = x[:,:-1]

a = np.matmul(np.matmul(np.linalg.inv(np.matmul(x.transpose(), x)), x.transpose()), y)

out = np.matmul(tests, a)
for line in out:
    print(line)
