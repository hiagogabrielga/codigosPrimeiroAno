num1=1
num=int(input('Digite um número maior que 1 e positivo: '))
while num <=1:
    print('você digitou um número menor ou igual a 1 tente novamente')
    num=int(input('Digite um número maior que 1 e positivos: '))
while num > 1:
    print(num1)
    num1+=1
    if num1==num:
        print(num1)
        break
