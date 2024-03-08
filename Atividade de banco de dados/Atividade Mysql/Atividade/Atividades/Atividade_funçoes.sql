/*1.     Calcule a media do salario do professores usando a função AVG;*/

use Curso;
select avg(salario) from professor;

/*2.     Calcule  a soma total dos salarios dos professores usando função sun;*/

select sum(salario) from professor;

/*3.     Consulte o maior salario de professores usando max e o minomo usando mim.*/

select max(salario) from professor;
select min(salario) from professor;


/*4.     Altere a tabela professor inserindo uma coluna chamada data_cadastro do tipo data.*/
use Curso;
alter table professor add data_cadastro date;


/*5.     Faça atualização da tabela professor inserindo a data com a função curdate()*/

update professor set data_cadastro = curdate() where idprofessor between 1 and 8;
