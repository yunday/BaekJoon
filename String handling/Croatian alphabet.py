string = input()
cnt = 0
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = string
for i in lst:
    if i in s:
        s = s.replace(i, ' ')

print(len(s))
