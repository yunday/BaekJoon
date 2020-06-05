import sys

string = sys.stdin.readline().strip('\n')
d = {}

for i in string.upper():
    d[i] = d.setdefault(i, 0) + 1

sd = sorted(d.items(), key=lambda x: x[1], reverse=True)

if len(sd) != 1 and sd[0][1] == sd[1][1]:
    print("?")
else:
    print(sd[0][0])
