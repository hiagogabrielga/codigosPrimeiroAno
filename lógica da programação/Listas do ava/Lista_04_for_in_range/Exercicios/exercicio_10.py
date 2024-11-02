num = int(input('Digite um número: '))
quant=0
for i in range(num):
    i+=1
    if num%i == 0:
        quant+=1
if quant > 2:
    print('Seu número não é primo.')
else:
    print('Seu número é primo.')