num=int(input('Digite seu número: '))
if num%3 == 0 and num%7 == 0:
     print('Seu número é mútiplo por 3 e 7.')
elif num%3 == 0:
    print('Seu número é mútiplo por 3.')
elif num%7 == 0:
    print('Seu número é mútiplo por 7.')
else:
    print('Seu número não é multipol de 3 e nem de 7.')