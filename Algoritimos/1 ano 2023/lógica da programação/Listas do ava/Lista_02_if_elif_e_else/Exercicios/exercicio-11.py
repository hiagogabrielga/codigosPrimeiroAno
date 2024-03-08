a=int(input('Digite o seu primeiro número: '))
b=int(input('Digite o seu segundo número: '))
c=int(input('Digite o seu terceiro número: '))
d=int(input('Digite o seu quarto número: '))
if a>b and a>c and a>d:
     print(f'O maior número é {a}')
elif b>a and b>c and b>d:
     print(f'O maior número é {b}')
elif c>a and c>b and c>d:
     print(f'O maior número é {c}')
elif d>a and d>b and d>c:
     print(f'O maior número é {d}')