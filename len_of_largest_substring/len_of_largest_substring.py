s = "abcbiefgh"
seen = {}
start = l = 0
for i, e in enumerate(s):
    if e in seen and seen[e] >= start:
        start = seen[e] + 1
    seen[e] = i
    l = max(l, i - start + 1)
print(l)
