#!/bin/python3

b_r, b_c = map(int, input().split())
h, w = map(int, input().split())
dirty = set()
for row_num in range(h):
    row = list(input())
    for spot in range(row.count('d')):
        dirty.add((row_num, row.index('d')))
        row[row.index('d')] = 0

row_dirty = set(((b_r, c) for c in range(w))).intersection(dirty)

if (b_r, b_c) in dirty:
    print('CLEAN')
    target = None
elif row_dirty:
    target = row_dirty.pop()
else:
    target = dirty.pop()

if not target:
    pass
elif target[0] == b_r:
    if target[1] > b_c:
        print('RIGHT')
    elif target[1] < b_c:
        print('LEFT')
elif target[0] > b_r:
    print('DOWN')
elif target[0] < b_r:
    print('UP')
