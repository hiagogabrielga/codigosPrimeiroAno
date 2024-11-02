soma=0
quant=0
while True:
    ida=int(input())
    if ida < 0:
        break
    else:
        soma+=ida
        quant+=1
print(f'{soma/quant:.2f}')