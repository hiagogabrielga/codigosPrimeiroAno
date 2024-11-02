#Hiago Gabriel Gonçalves André | Vitor Gabriel Capelleto

linha='='*30
class Livro:
    def __init__(self, titulo, autor, ano, disponivel = True) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel
        pass
    
    def emprestar(self):
        if self.disponivel ==  True:
            self.disponivel = False
            print('\nEmpréstimo foi realizado com sucesso.')
        else:
            print('\nO livro já está emprestado')

    def devolver(self):
        if self.disponivel ==  False:
            self.disponivel = True
            print(f'\nDevolução do livro foi concluída com êxito.')
        else:
            print(f'\nO livro não está emprestado.')

livro = (Livro('Jojo', 'Hirorico Araki','1979'))

def main():
    while True:
        print(f'\n{linha}\
                   \nBIBLIOTECA DO XERJÃO \
                   \n{linha}')
        print(f'Livros catálogados\
                  \n{linha}\nNome do Livro: {livro.titulo}\nAutor: {livro.autor}\nAno: {livro.ano}\n{linha}')
        per= input(f'\n{linha}\nQual função deseja realizar?\
                \n(1) Alugar Livro.\
                \n(2) Devover Livro.\
                \n(3) Fechar programa.\
                \n{linha}\nRespota:')
        
        if per == '1':
            titulo=input('\nDigite o nome do livro que deseja alugar: ')
            if titulo == livro.titulo:
                livro.emprestar()
            else:
                print('\nLivro inexistente')

        elif per == '2':
            selec_l=input('\nDigite o nome do livro que deseja devolver: ')
            if selec_l == livro.titulo:
                livro.devolver()
            else:
                print('\nLivro inexistente')

        elif per == '3':
            print('\nObrigado por fazer parte da nossa familía :).')
            break
        else:
            print('\nFunção inexistente.')
    
main()
print('HAHAHAHAHAAHHAA SOU DO MALLLLLLLLLLLLLLLLLLLLLL \n MALLLLLLLLLLLLLLLLLLLLLL MALLLLLLLLLLLLLLLLLLLLLL\n MALLLLLLLLLLLLLLLLLLLLLL MALLLLLLLLLLLLLLLLLLLLLL')