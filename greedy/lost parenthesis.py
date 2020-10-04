equ = input()+'-'
a = sum(list(map(int, equ[:equ.index('-')].replace('+', ' ').split())))
b = sum(list(map(int, equ[equ.index('-')+1:].replace('+', ' ').replace('-', ' ').split())))
print(a - b)
