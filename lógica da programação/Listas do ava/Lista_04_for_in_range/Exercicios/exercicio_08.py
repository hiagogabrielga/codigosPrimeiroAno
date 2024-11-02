quant=0
for i in range(10):
    num=int(input('Digite o número: '))
    if num > 10:
        quant+=1
print(f'foram digitado {quant} números maiores do que 10')