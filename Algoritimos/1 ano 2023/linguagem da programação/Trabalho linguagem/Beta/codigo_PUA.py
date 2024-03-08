#pip install mysql-connector-python

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

def adicionar():
    conexao=conectar()
    cursor = conexao.cursor()
    
    atividade = input('Digite sua atividade: ')
    

    while True: 
        if atividade == '':
            print('Você não adicionou um nome a sua atividade') 
            atividade = input('Digite o nome de sua atividade: ')
        else:
              break 
        
    
    while True:
        if enumerar(1,atividade) > 0:
            alerta=input('Você tem outra atividade com o mesmo nomes, gostaria de mudar o nome dessa atividade? (S/N): ')
            if alerta.upper() == 'N':
                atividade=f'{atividade}({enumerar(1,atividade)})'
                print(f'Sua atividade sera salva com o nome de {atividade}')
                break
            elif alerta.upper() == 'S':
                atividade = input('Digite o nome de sua atividade: ')
        else:
            break
        
    descricao = input('Digite a descrição da sua atividade: ')

    while True: 
        if descricao == '':
            alerta=input('Você não adicionou uma descrição a sua atividade, deseja deixar este campo vazio? (S/N): ')
            if alerta.upper() == 'N':
                descricao = input('Digite a descrição da sua atividade: ')
            elif alerta.upper() == 'S':
                  break
        else:
              break

    status='Pendente'

    comando = f'INSERT INTO dados_da_agenda (atividade, descricao, status) VALUES ("{atividade}", "{descricao}","{status}")'

    cursor.execute(comando)

    conexao.commit()

    cursor.close()
    conexao.close()
    return'Alterações feita com sucesso'

def mostrar():
    resultado_p=[]
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
            resultado_p.append(f'Id: {atv[0]} | Atividade: {atv[1]} | Descrição: {atv[2]} | Status: {atv[3]}')
        resultado_p=str(resultado_p).replace("'",'')
        resultado_p=str(resultado_p).replace("[",'')
        resultado_p=str(resultado_p).replace("]",'')
        resultado_p=str(resultado_p).replace(", ",'\n')
    cursor.close()
    conexao.close()
    return resultado,resultado_p
    
def atualizar():
    if resultado == []:
        return'\nVocê não tem atividades nesta agenda.'
    else:
        conexao=conectar()
        cursor = conexao.cursor()

        iddados_da_agenda = id()
        if iddados_da_agenda == 'Não foi encontrado a atividade':
            return'\nNão foi encontrado a atividade.'
        else:
            if per == '4':
                status='Concluida'
            elif per == '5':
                status='Pendente'

            comando = f'UPDATE dados_da_agenda SET status = "{status}" WHERE iddados_da_agenda = "{iddados_da_agenda}"'
            cursor.execute(comando)
                
            conexao.commit()
            cursor.close()
            conexao.close()
            return'Alterações feitas com sucesso'


def deletar():
    if resultado == []:
        return'\nVocê não tem atividades nesta agenda.'
    else:
        conexao=conectar()
        cursor = conexao.cursor()

        iddados_da_agenda=id()
        if iddados_da_agenda == 'Não foi encontrado a atividade':
            return '\nNão foi encontrado a atividade.'
        
        else:
            comando = f'DELETE FROM dados_da_agenda WHERE iddados_da_agenda = "{iddados_da_agenda}"'

            cursor.execute(comando)

            conexao.commit() 

            cursor.close()
            conexao.close()
            return'Alterações feita com sucesso'

def id():
    iddados_da_agenda = int(input('\nDigite o numero da tarefa: '))-1
    try:
        atv=resultado[iddados_da_agenda]
        iddados_da_agenda = int(list(atv)[0])
        return iddados_da_agenda
    except:
        return 'Não foi encontrado a atividade'

def enumerar(indice,bloco):
    contador=0
    n=len(resultado)
    for i in range(n):
    
        if str(resultado[i][indice]).split('(')[0] == bloco:
            contador=contador+1
    return contador

while True:
    print('\nEscolha uma Opção:\
          \n1 = Adicionar tarefa\
          \n2 = Mostrar atividades\
          \n3 = Retirar atividades\
          \n4 = Marcar como concluida\
          \n5 = Marcar como pendente\
          \n6 = Fechar o programa\n')
    
    per=input('Qual função deseja fazer?')
    print('\nAguarde alguns segundos.\n')
    resultado=mostrar()[0]
    if per=='1':
        print(adicionar())
    elif per == '2':
        print(mostrar()[1])
    elif per == '3':
        print(deletar())
    elif per == '4':
        print(atualizar())
    elif per == '5':
        print(atualizar())
    elif per == '6':
        print('Obrigado por utilizar o programa')
        break
    else:
        print('Ops, O número não corresponde a nenhuma função.')