n = int(input())

if (n % 2) or ((n >= 6) and (n <= 20)):
    weirdness = 'Weird'
else:
    weirdness = 'Not Weird'

print(weirdness)
