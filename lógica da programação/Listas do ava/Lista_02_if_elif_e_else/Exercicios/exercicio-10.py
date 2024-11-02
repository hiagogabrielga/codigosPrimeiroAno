import math
a=int(input('Digite o valor de A: '))
b=int(input('Digite o valor de B: '))
c=int(input('Digite o valor de C: '))
delta=(b*b)-4*a*c
if delta < 0:
    print('Não tem raizes reais')
elif delta == 0:
    x = -b / (2*a)
    print('A raiz é do valor',x)
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'O resultado é de duas raizes, X1={x1} e X2 {x2}')