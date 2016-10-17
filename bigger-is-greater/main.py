#!/bin/python3

t = int(input().strip())
cases = [0]*t
for i in range(t):
    cases[i] = input().strip()

def gen_unique_perms(string):
    perms = [string]
    if len(string) == 1:
        return [string]
    for index, char in enumerate(string):
        for perm in gen_unique_perms(string[:index] + string[index+1:]):
            if char + perm not in perms:
                perms.append(char + perm)
    return perms

for c in cases:
    p = sorted(gen_unique_perms(c))
    if p.index(c) < len(p) - 1:
        print(p[p.index(c)+1])
    else:
        print('no answer')
