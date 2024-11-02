quantidade = 0
M=0
for i in range(6):
    num = float(input())
    if num > 0:
        quantidade = quantidade + 1
        M=M+num
print(f'{quantidade} valores positivos\n{M/quantidade:.1f}')