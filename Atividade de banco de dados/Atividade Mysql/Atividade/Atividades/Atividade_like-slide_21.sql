/*========================================================== Slide 21 ======================================================================================================================*/

/*LIKE – 5 consultas diferentes*/
use Curso; 
select nome,salario from professor where salario like '4%';
select nome from aluno where nome like '%S%';
select nome,valor from curso where valor like '1_%_%';
select nome,cpf from aluno where cpf like '%8';
select nome,valor from curso where valor like '_5%0';

/*Usando between – 3 consultas*/
select nome,valor from curso where valor between 100 and 200;
select nome, cargahoraria from curso where cargahoraria between 10 and 30;
select nome, salario from professor where salario between 3000 and 5000;


/*Operadores AND e OU - 5 consultas diferentes;*/
/*Operador or */
select nome, salario from professor where salario between 2000 and 3000 or nome like 'C%';
select nome,cargahoraria from curso where nome like '%m%' or cargahoraria > 30;

/*Operador and */
select nome,cpf from aluno where nome like 'R%' and cpf like '%7%';
select nome, salario from professor where salario > 3000 and nome like '%e%';

/*Operador And e or*/
select nome,valor,cargahoraria from curso where nome like '%c%' and (valor like '2%' or cargahoraria > 20);


/*IN – 2 consultas diferentes*/
select idaluno,nome from aluno where idaluno in (6, 18, 20, 23);
select idprofessor,nome from professor where idprofessor in (2,5,6,7);