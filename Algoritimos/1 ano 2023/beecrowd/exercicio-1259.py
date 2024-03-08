pares=[]
impares=[]
N = int(input())
for i in range(N):
    numero=int(input())
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort(reverse=True)

for par in pares:
    print(par)
for im in impares:
    print(im)
