quant_p=0
quant_i=0
for n in range(5):
    num=int(input('Digite seu número: '))
    if num%2 == 1:
        quant_i+=1
    if num%2 == 0:
        quant_p+=1
print(f'\nDos 5 número apresentados, foram digitados:\n{quant_i} número impáres\n{quant_p} números pares.\
    \nFim de programa, Até a proxima.\n')