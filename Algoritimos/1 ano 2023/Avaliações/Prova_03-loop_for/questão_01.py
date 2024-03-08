num=1000
quant=0
print('Os número impáres do intervalo de 500 a 1000 na ordem decrecente são:')
for i in range(1000):
    quant+=1
    num2=num-i
    if num2%2 == 1:
        print(f'O {quant}º número impar é: {num2}')
        num2=0
    if quant == 500:
        break
print('Fim de programa, até mais.')
