ida=int(input('Digite a sua idade apenas em anos: '))
a='Seu voto é facultativo, mas sua participação é importante.'
b='Seu voto é obrigátório, participe.'
c='Você não pode votar.'
d='Regularize a situação cadastral do seu título o mais rápido possivel.'
if ida == 16 or ida == 17 or ida > 70:
    per1=input('Você possui título de eleitor? ')
    if per1 == 'sim' or per1 == 'Sim':
        print(f'{a}')
    else:
        print(f'{c}')
elif ida >=18 and ida <=70:
    per2=input('Você possui título de eleitor? ')
    if per2 == 'sim' or per2 == 'Sim':
        print(f'{b}')
    else:
        print(f'{d}')
else:
    print(f'{c}')


