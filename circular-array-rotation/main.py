#!/bin/python3

def rotate(l, rotation_units):
    if len(l) <= rotation_units:
        rotation_units = rotation_units % len(l)
    return l[-rotation_units:] + l[:-rotation_units]

n, k, q = [int(i) for i in input().split()]
array = [int(i) for i in input().split()]

array = rotate(array, k)

index = list()
for count in range(q):
    index.append(int(input().strip()))

for i in index:
    print(array[i])
