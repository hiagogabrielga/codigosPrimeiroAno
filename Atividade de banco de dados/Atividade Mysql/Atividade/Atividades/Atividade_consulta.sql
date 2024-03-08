/*1. Faça uma consulta na tabela professor que liste em ordem de menor para o 
maior salário e de maior para menor*/
use Curso;
select * from professor order by salario desc;
select * from professor order by salario asc;

/*2. Faça uma consulta na tabela aluno que coloque em ordem decrescente por 
nome, cpf e estado.*/
use Curso;
select * from aluno order by nome desc;
select * from aluno order by cpf desc;
select * from aluno order by estado desc;

/*3. Faça uma consulta na tabela professor e apresente os professores que ganham 
mais de 1250 reais.*/
use Curso;
select * from professor where salario > 1250;

/*4. Faça uma consulta no banco de dados que apresente professores que ganhem 
salários 1000, 1200 e 1210 reais.*/
use Curso;
select * from professor where salario in ('1000', '1200', '1210');

/*5. Faça uma consulta no banco de dados que apresente professores que ganhem 
em 1500 e 1900 reais. (Faça com between e operador de comparação)*/
use Curso;
select nome, salario from professor where salario between 1500 and 1900;
