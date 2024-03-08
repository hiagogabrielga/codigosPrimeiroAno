nome_d_t=input('Digite o nome do time: ')
quant_d_g=int(input('Digite a quantidade de gols: '))
nome_d_t2=input('Digite o nome do outro time: ')
quant_d_g2=int(input('Digite a quantidade de gols do outro time: '))
if quant_d_g > quant_d_g2:
    print(f'{nome_d_t} ganhou do {nome_d_t2}\nPlacar {quant_d_g} X {quant_d_g2}')
elif quant_d_g < quant_d_g2:
    print(f'{nome_d_t2} ganhou do {nome_d_t}\nPlacar {quant_d_g2} X {quant_d_g}')
else:
    print(f'{nome_d_t} empatou com {nome_d_t2}\nPlacar {quant_d_g} X {quant_d_g2}')
