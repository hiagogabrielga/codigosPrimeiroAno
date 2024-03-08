'''pip install mysql-connector-python'''
import mysql.connector
def conectar():
    conexao = mysql.connector.connect(
        host= "containers-us-west-109.railway.app",
        port = '7189',
        user='root',
        password='ekJxD1gEL8SdCOfgwrEr',
        database='railway',
    )
    return conexao

def mostrar():
    linha='|==================================================='
    resultado_p=[linha]
    conexao=conectar()
    cursor = conexao.cursor()

    comando = f'SELECT * FROM dados_da_agenda'

    cursor.execute(comando)

    resultado = cursor.fetchall()
    if resultado == []:
        resultado_p='\nVocê não tem atividades nesta agenda.'
    else:
        n=len(resultado)
        for i in range(n):
            atv=resultado[i]
            atv=list(atv)
            atv[0]=i+1
            atv=tuple(atv)
            resultado_p.append(f'|Atividade de Número: {atv[0]}|Título: {atv[1]}|Descrição: {atv[2]}|Status: {atv[3]}{linha}')
        resultado_p=str(resultado_p).replace("'",'')
        resultado_p=str(resultado_p).replace("[",'')
        resultado_p=str(resultado_p).replace("]",'')
        resultado_p=str(resultado_p).replace(", ",'')
        resultado_p=str(resultado_p).replace("|",'\n')
    cursor.close()
    conexao.close()
    return resultado,resultado_p

def id():
    while True:
        try:
            iddados_da_agenda = int(input('\nDigite o número de sua atividade: '))-1

            while iddados_da_agenda > len(resultado) or iddados_da_agenda < 0:
                print('\nOps, Você adicionou um número de uma atividade que não existe. \nTente outro número.')
                iddados_da_agenda = int(input('\nDigite o número de sua atividade: '))-1

            atv=resultado[iddados_da_agenda]
            iddados_da_agenda = int(list(atv)[0])
            return iddados_da_agenda
            
        except:
            print('\nOps, Você adicionou uma letra ao inves de um número de uma atividade. \nTente outro número.')

def encontrar_semelhantes(indice,bloco):
    contador=0
    n=len(resultado)
    for i in range(n):
    
        if str(resultado[i][indice]).split('(')[0] == bloco:
            contador=contador+1
    return contador

def adicionar():
    conexao=conectar()
    cursor = conexao.cursor()
    
    atividade = input('\nDigite o título da sua atividade: ')
    

    while True: 
        if atividade == '':
            print('\nVocê não adicionou um título a sua atividade') 
            atividade = input('Digite o título da sua atividade: ')
        else:
              break 
        
    
    while True:
        if encontrar_semelhantes(1,atividade) > 0:
            alerta=input('Você tem outra atividade com o mesmo título, gostaria de mudar o nome dessa atividade? (S/N): ').upper()
            if alerta == 'N' or alerta == 'NÃO' or alerta == 'NAO':
                atividade=f'{atividade}({encontrar_semelhantes(1,atividade)})'
                print(f'Sua atividade foi salva com o título de {atividade}')
                break
            elif alerta == 'S' or alerta == "SIM":
                atividade = input('Digite o título da sua atividade: ')
        else:
            break
        
    descricao = input('Digite a descrição da sua atividade: ')

    while True: 
        if descricao == '':
            alerta=input('Você não adicionou uma descrição à sua atividade. Deseja adicionar uma descrição? (S/N): ').upper()
            if alerta == 'S' or alerta == "SIM":
                descricao = input('Digite a descrição da sua atividade: ')
            elif alerta == 'N' or alerta == 'NÃO' or alerta == 'NAO':
                  break
        else:
              break

    status='Pendente'

    comando = f'INSERT INTO dados_da_agenda (atividade, descricao, status) VALUES ("{atividade}", "{descricao}","{status}")'

    cursor.execute(comando)

    conexao.commit()

    cursor.close()
    conexao.close()
    return'\nAlteração feita com sucesso'


    
def marcarcar_C_e_P():
    if resultado == []:
        return'\nVocê não tem atividades nesta agenda.'
    else:
        conexao=conectar()
        cursor = conexao.cursor()

        iddados_da_agenda = id()
        if iddados_da_agenda == False:
            return'\nSua atividade não foi encontrada.'
        else:
            if per == '3':
                status='Concluida'
            elif per == '4':
                status='Pendente'

            comando = f'UPDATE dados_da_agenda SET status = "{status}" WHERE iddados_da_agenda = "{iddados_da_agenda}"'
            cursor.execute(comando)
                
            conexao.commit()
            cursor.close()
            conexao.close()
            return'\nAlteração feita com sucesso'


def deletar():
    if resultado == []:
        return'\nVocê não tem atividades nesta agenda.'
    else:
        conexao=conectar()
        cursor = conexao.cursor()

        iddados_da_agenda=id()
        if iddados_da_agenda == False:
            return '\nSua atividade não foi encontrada.'
        
        else:
            comando = f'DELETE FROM dados_da_agenda WHERE iddados_da_agenda = "{iddados_da_agenda}"'

            cursor.execute(comando)

            conexao.commit() 

            cursor.close()
            conexao.close()
            return'\nAlteração feita com sucesso'


print('===================================================\
    \n| Bem Vindo(a) ao Gerenciador de tarefas Ametista |\
      \n===================================================')
while True:
    print('\n=============================\
          \n| Escolha uma Opção:        |\
          \n|===========================|\
          \n| 1 = Mostrar atividades    |\
          \n| 2 = Adicionar tarefa      |\
          \n| 3 = Marcar como concluída |\
          \n| 4 = Marcar como pendente  |\
          \n| 5 = Retirar atividades    |\
          \n| 6 = Fechar o programa     |\
          \n=============================\n')
    
    per=input('Qual função deseja fazer? ')
    
    if per=='1':
        print('\nAguarde alguns segundos.')
        resultado=mostrar()[0]
        print(mostrar()[1])     

    elif per == '2':
        print('\nAguarde alguns segundos.')
        resultado=mostrar()[0]
        print(adicionar())

    elif per == '3':
        print('\nAguarde alguns segundos.')
        resultado=mostrar()[0]
        print(marcarcar_C_e_P())

    elif per == '4':
        print('\nAguarde alguns segundos.')
        resultado=mostrar()[0]
        print(marcarcar_C_e_P())

    elif per == '5':
        print('\nAguarde alguns segundos.')
        resultado=mostrar()[0]
        print(deletar())

    elif per == '6':
        print('\n===========================================================\
    \n| Obrigado por utilizar o Gerenciador de tarefas Ametista |\
      \n===========================================================')
        break
    else:
        print('\nOps, O número não corresponde a nenhuma função.')
    
