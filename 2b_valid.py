s = "anagram"
t = "nagarim"
s_dist = {}
if len(s) != len(t):
    print(False)
else:
    for x in s:
        s_dist[x] = s_dist.get(x, 0) + 1
    for x in t:
        s_dist[x] = s_dist.get(x, 0) -1
    print(s_dist)
    total_diff = sum(abs(v) for v in s_dist.values())
    print(total_diff)
    if total_diff <=2:
        print(True)