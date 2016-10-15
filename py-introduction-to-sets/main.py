num_plants = int(input())
heights = set((int(i) for i in input().strip().split()))

print(sum(heights)/len(heights))
