use Curso;

/*a) Listar nomes de professores e alunos utilizando o like e ordennando de a - z e de z - a (Crescente e Decrescente)*/
select nome from professor where nome like '%A%' order by nome Asc;
select nome from aluno where nome like '%A%' order by nome Asc;

select nome from professor where nome like '%A%' order by nome Desc;
select nome from aluno where nome like '%A%' order by nome Desc;


/*b) Usar função e somar e calcular a média dos salários de todos os professor.*/

select avg(salario) from professor;


/*c) Usar a função MAX e MIN consultar o menor e maior salário dos professores.*/

select nome, salario from professor where salario = (select max(salario) from professor); 
select nome, salario from professor where salario = (select min(salario) from professor); 




