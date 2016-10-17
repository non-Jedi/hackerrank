#!/bin/python3

t = int(input())
cases = [0]*t
for i in range(t):
    cases[i] = input()

def next_perm(string):
    '''Starting from the end of a string with length n, finds the first
    occurrence of x(i) < x(i+1) where i increases from beginning to end
    of string.

    x(i) is then replaced with the smallest number x(j) that satisfies:
    1) j > i
    2) x(j) > x(i)

    The next permutation is constructed as 
    
    [x(0), x(1), ..., x(j), sorted(x(i), x(i+1), x(i+2), ..., x(n-1))] 
    
    where the sorted values exclude x(j).'''

    end = [string[-1]]
    for index, char in enumerate(reversed(string[:-1])):
        if char >= string[-1-index]:
            end.append(char)
        else:
            output = string[:-2-index]
            output += end.pop(end.index(min([i for i in end if i > char])))
            output += ''.join(sorted(end + [char]))
            return output
    return 'no answer'

for c in cases:
    print(next_perm(c))
