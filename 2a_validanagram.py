s = "anagram"
t = "nagaram"
s_dist = {}
t_dist = {}
if len(s) != len(t):
    print(False)
else:
    for x in s:
        s_dist[x] = s_dist.get(x, 0) + 1
    for y in t:
        t_dist[y] = t_dist.get(y, 0) + 1

    if s_dist == t_dist:
        print(True)
    else:
        print(False)
