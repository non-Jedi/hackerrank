n, m = [int(i) for i in input().split()]
array = (int(i) for i in input().split())
A = set((int(i) for i in input().split()))
B = set((int(i) for i in input().split()))

happiness = 0

for num in array:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)
