use curso;
/*Listar nomes de professores e alunos utilizando o like, que comecem com determinada letra que terminem e que contenham;*/
select nome from aluno where nome like 'G%';
select nome from aluno where nome like '%r%';
select nome from aluno where nome like '%o';
select nome from professor where nome like 'A%';
select nome from professor where nome like '%g%';
select nome from professor where nome like '%o';

/*Listar os id’s e nomes dos cursos, seguido dos dados do nome do professor e salário correspondentes.*/
select curso.idcurso,curso.nome from curso inner join professor on curso.professor_id = idprofessor where professor.nome like '%c%' and professor.salario between 4500 and 5000;

/*Listar os id’s e nomes dos cursos, seguido dos dados do nome do professor e salário dos professores com nome que contenham as letrar “ma”.*/
select curso.idcurso,curso.nome from curso inner join professor on curso.professor_id = idprofessor where professor.nome like '%Ma%' and professor.salario between 3000 and 5000;

/*Listar os id’s e nomes dos cursos, seguido dos dados do nome do professor e salário dos professores que dão aula em algum curso especifico.*/
select professor.idprofessor, professor.nome, professor.salario from professor inner join curso on curso.professor_id = idprofessor where curso.idcurso = 2;

/*Consultar tabela cursoaluno e listar o nome do curso e do aluno registrado nessa tabela.*/
select curso.nome as curso_nome, aluno.nome as aluno_nome from cursoaluno join curso on cursoaluno.curso_idcurso = curso.idcurso join aluno on cursoaluno.aluno_idaluno = aluno.idaluno;