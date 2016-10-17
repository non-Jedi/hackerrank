#!/bin/python3
import numpy as np

a = np.array([int(i) for i in input().split()])

print(a.reshape(3,3))
