dia=int(input())
ano=dia//365
meses=(dia%365)//30
dia=((dia%365)%30)//1
print(f'{ano} ano(s)\n{meses} mes(es)\n{dia} dia(s)')