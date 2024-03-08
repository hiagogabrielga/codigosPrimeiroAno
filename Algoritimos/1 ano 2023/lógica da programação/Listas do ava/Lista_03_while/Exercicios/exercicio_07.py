Pedro=150
Lucas=110
soma=0
while True:
    Pedro+=2
    Lucas+=3
    soma+=1
    if Pedro == Lucas:
        print(f'Lucas e Pedro estão com a mesma altura, Lucas tem {Lucas/100:.2f}m e Pedro tem {Pedro/100:.2f}m\nForam necessarios {soma} anos')
    if Lucas > Pedro:
         print(f'Lucas e Pedro estão com altura diferentes, Lucas tem {Lucas/100:.2f}m e Pedro tem {Pedro/100:.2f}m\nForam necessarios {soma} anos')
         break