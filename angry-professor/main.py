#!/bin/python3

t = int(input().strip())
test_cases = list()
for i in range(t):
    n, k = map(int, input().split())
    a = map(int, input().split())
    test_cases.append((n, k, a))

for case in test_cases:
    if len([i for i in case[-1] if i <= 0]) >= case[1]:
        print('NO')
    else:
        print('YES')
