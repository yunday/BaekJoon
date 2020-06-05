word = input()
lst = [-1]*26
for i in word:
    lst[ord(i)-97] = word.index(i)
for j in lst:
    print(j, end=' ')
