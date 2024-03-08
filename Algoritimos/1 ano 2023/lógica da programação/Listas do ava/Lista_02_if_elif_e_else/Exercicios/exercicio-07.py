peso_p=int(input('Digite o peso em Kg:'))
if peso_p-50 <= 0:
    print('O peso está no regulamento.')
else:
    print(f'O peso exedeu o limite, a cada quilogramas a mais sera cobrado R$ 4.00 de multa.\
          \nO preço a pagar é de R$ {(peso_p-50)*4.00:.2f}')