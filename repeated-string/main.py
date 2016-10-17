#!/bin/python3

s = input().strip()
n = int(input().strip())

full_repeats = n // len(s)
partial_string = s[:(n % len(s))]

print(full_repeats * s.count('a') + partial_string.count('a'))
