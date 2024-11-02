a=int(input('Digite o seu primeiro número: '))
b=int(input('Digite o seu segundo número: '))
c=int(input('Digite o seu terceiro número: '))
if a>b and b>c and a>c:
    print('A ordem crescente é', c, b, a)
elif b>a and a>c and b>c:
    print('A ordem crescente é', c, a, b)
elif c>a and a>b and c>b:
    print('A ordem crescente é', b, a ,c)
elif c>b and b>a and c>a:
    print('A ordem crescente é', a, b, c)
elif a>c and c>b and a>b:
    print('a ordem crescente é', b, c ,a)
elif b>c and c>a and b>a:
    print('A ordem crescente é', a, c, b)
elif a==b and b>c:
    print('A ordem crescente é', c, b, a)
elif a==c and c>b:
    print('A ordem crescente é', b, c, a)
elif b==c and c>a:
    print('A ordem crescente é', a, c, b)
elif a==b and b<c:
    print('A ordem crescente é', a, b, c)
elif a==c and c<b:
    print('A ordem crescente é', a, c, b)
elif b==c and c<a:
    print('A ordem crescente é', b, c, a)
else:
    print('A ordem crescente é', c, b, a)
