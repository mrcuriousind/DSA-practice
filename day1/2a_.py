s = "anagram"
t = "nagaram"
s_dist = {}
t_dist = {}
i=1
j=1
if len(s) == len(t):
    for x in s:
        s_dist(x)=i
        i+1
    for y in t:
        t_dist(y)=j
        j+1

print(s_dist)