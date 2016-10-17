#!/bin/python3

n = int(input().strip())
grid = list()
for i in range(n):
    grid.append(list(input()))

for row_num, row in enumerate(grid):
    if 'm' in row:
        m_row = row_num
        m_col = row.index('m')
    if 'p' in row:
        p_row = row_num
        p_col = row.index('p')

def left(m_col):
    print('LEFT')
    m_col -= 1
    return m_col
def right(m_col):
    print('RIGHT')
    m_col += 1
    return m_col
def up(m_row):
    print('UP')
    m_row -= 1
    return m_row
def down(m_row):
    print('DOWN')
    m_row += 1
    return m_row

while True:
    if m_row == p_row:
        if m_col == p_col:
            break
        elif m_col > p_col:
            m_col = left(m_col)
        elif m_col < p_col:
            m_col = right(m_col)
    elif m_row > p_row:
        m_row = up(m_row)
    elif m_row < p_row:
        m_row = down(m_row)
