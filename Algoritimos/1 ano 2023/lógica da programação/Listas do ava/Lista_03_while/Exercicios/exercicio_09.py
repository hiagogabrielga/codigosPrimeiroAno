sucessor=1
fatorial=1
num=int(input('Digite um número maior que 1 e positivo: '))
while num > 1:
    sucessor+=1
    fatorial*=sucessor
    if sucessor==num:
        print(f'{num}! = {fatorial}')
        break