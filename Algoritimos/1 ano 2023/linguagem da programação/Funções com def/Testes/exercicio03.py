def comp_d_idades(idade):
        lista_d_n=[str(idade) for idade in range (10)]

        for i in idade:
                if lista_d_n.count(i) == 0: return "Número Inválido"
        
        idade = int(idade)

        if idade > 17: return'Maior de idade'
        else:return'Menor de idade'

print(comp_d_idades(input('Digite sua idade: ')))
        