soma=0
num=int(input('Dite um numero: '))
while num%2 == 0:
    num=int(input('Dite um numero: '))
    soma+=1
    if num < 0 or num%2 == 1:
        break
print(f'fim de programa, número digitados: {soma}')

