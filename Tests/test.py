S = input()
longest = 0
acgts = 0
for s in S:
    if s in ["A","C","G","T"]:
        acgts += 1
    else:
        acgts = 0
    if longest < acgts:
        longest = acgts

print(longest)