#!/bin/python3

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

a_points = 0
b_points = 0

for ratings in zip(a,b):
    if ratings[0] > ratings[1]:
        a_points += 1
    elif ratings[1] > ratings[0]:
        b_points +=1

print(' '.join((str(i) for i in (a_points, b_points))))
