#!/bin/python3
import numpy as np

n, m = map(int, input().split())
a = np.empty((n, m), dtype = int)
for i in range(n):
    for j, entry in enumerate(map(int, input().split())):
        a[i][j] = entry

print(a.transpose())
print(a.flatten())
