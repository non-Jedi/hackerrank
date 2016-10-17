#!/bin/python3
n = int(input().strip())
m_r, m_c = map(int, input().split())
for i in range(n):
    row = list(input())
    if 'p' in row:
        p_r = i
        p_c = row.index('p')

if m_r == p_r:
    if m_c > p_c:
        print('LEFT')
    elif m_c < p_c:
        print('RIGHT')
elif m_r > p_r:
    print('UP')
elif m_r < p_r:
    print('DOWN')
