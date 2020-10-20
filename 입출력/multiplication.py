a = int(input())
b = input()
lst = [a*int(b[2]), a*int(b[1]), a*int(b[0])]
for _ in lst:
    print(_)
print(lst[0]+lst[1]*10+lst[2]*100)