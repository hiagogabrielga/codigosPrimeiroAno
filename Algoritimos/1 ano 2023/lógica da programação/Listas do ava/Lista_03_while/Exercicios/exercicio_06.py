media=0
soma=0
num=int(input('Digite um número:'))
while num%2 == 1:
    soma+=1
    media+=num
    num=int(input('Digite um número:'))
print(f'A média é de {media/soma}')
print('Fim de programa.')