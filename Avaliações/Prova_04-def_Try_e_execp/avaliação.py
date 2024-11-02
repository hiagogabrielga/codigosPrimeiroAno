#Hiago Gabriel Gonçalves André 
#Lívia Darold
#Data: 05/09/2023  Turma: 1°A Informática

#Questão: Software de pagamento de prestações

def ler_valores():
    vlr_prestacao=input('Qual é o valor de sua prestação? ')
    nr_dias_atraso=input('Quantos o número de dias atrassado? ')
    while True:
        try:
            vlr_prestacao=vlr_prestacao.replace(',','.')
            vlr_prestacao=float(vlr_prestacao)
            while True:    
                if vlr_prestacao <= 0:
                    if vlr_prestacao == 0:
                        msg= 'igual a'
                    elif vlr_prestacao < 0:
                        msg = 'menor que'
                    print(f'O valor apresentado é {msg} zero, adicione outro valor maior que zero.') 
                    vlr_prestacao=input('Qual é o valor de sua prestação? ')
                    vlr_prestacao.replace(',', '.')
                    vlr_prestacao=float(vlr_prestacao)
                else:
                    break
            break            
        except:
            print('Valor da prestação apresentado é invalido, tente outro valor.')
            vlr_prestacao=input('Qual é o valor de sua prestação? ')
    while True:
        try:        
            nr_dias_atraso=int(nr_dias_atraso)
            while True:
                if nr_dias_atraso < 0:
                    print('O número de dias apresentados é inválido, tente novamente.')
                    nr_dias_atraso=input('Quantos o número de dias atrassado? ')
                    nr_dias_atraso=int(nr_dias_atraso)
                else:
                    break
            break
        except:
            print('Número de dias de atraso apresentado é inválido, tente novamente.')
            nr_dias_atraso=input('Quantos o número de dias atrassado? ')
    dados=(f'{vlr_prestacao},{nr_dias_atraso}')
    return dados

def calcular_juros(dados):
    dados=str(dados)
    vlr_prestacao=dados.split(',')[0]
    nr_dias_atraso=dados.split(',')[1]
    vlr_prestacao=float(vlr_prestacao)
    nr_dias_atraso=int(nr_dias_atraso)
    if nr_dias_atraso == 0:
        vlr_a_pagar=vlr_prestacao
    elif nr_dias_atraso > 0:
        vlr_a_pagar=vlr_prestacao + ((5+ nr_dias_atraso)/100*vlr_prestacao)
    return vlr_a_pagar

while True:
    dados=ler_valores()
    vlr_a_pagar=calcular_juros(dados)
    print(f'O Valor a pagar de sua prestação é de {vlr_a_pagar:.2f}')
    per=input('Deseja continuar?(Sim/Não):')
    if per.upper == 'NÃO':
        print('Obrigado pelo acesso')
        break
