quant_d_aluno=int(input('Quantos alunos fizeram a prova? '))
soma=0
quant=0
quant_d_aluno_a=0
quant_d_aluno_r=0
while quant_d_aluno != quant:
    nota=float(input('\nDigite a nota: '))
    while nota > 100:
        nota=float(input('Nota inválida\nDigite a nota novamente: '))
    if nota >= 60 and nota <= 100:
        quant+=1
        soma+=nota
        quant_d_aluno_a+=1
    else:
        quant+=1
        soma+=nota
        quant_d_aluno_r+=1
print(f'\nA média da turma foi de {soma/quant_d_aluno:.2f}\
    \nA quantidade de alunos aprovados foi de {quant_d_aluno_a}\
    \nA quantidade de alunos Reprovados foi de {quant_d_aluno_r}\n')