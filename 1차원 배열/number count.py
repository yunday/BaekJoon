a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
for _ in range(10):
    print(result.count(str(_)))