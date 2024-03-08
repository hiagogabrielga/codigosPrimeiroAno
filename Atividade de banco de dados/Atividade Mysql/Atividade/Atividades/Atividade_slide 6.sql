/*
CRIANDO O BANDO DE DADOS CURSO (linha 7 a linha 50)
ADICIONANDO DADOS (linha 51 a linha 91)
ALTERANDO E ADICIONANDO NOVOS DADOS A TABELA (linha 92 a linha 110)
CONSULTANDO DADOS (linha 111 a linha 123)
*/
/*======================================= CRIANDO O BANDO DE DADOS CURSO =======================================================*/
create database Curso;
use Curso;
create table professor (
idprofessor int auto_increment primary key,
nome varchar(45),
email varchar(45),
cpf bigint,
endereco varchar(45),
numero int,
complemento varchar(45),
cidade varchar(45),
estado varchar(45)
);

create table curso (
idcurso int auto_increment primary key,
nome varchar(45),
professor_id int,
constraint fk_professorcurso foreign key (professor_id)
references professor(idprofessor)
);

create table aluno(
idaluno int auto_increment primary key,
nome varchar(45),
email varchar(45),
cpf bigint,
endereco varchar(45),
numero int,
complemento varchar(45),
cidade varchar(45),
estado varchar(45)
);

create table cursoaluno (
curso_idcurso int,
aluno_idaluno int,
constraint fk_curso_cursoaluno foreign key (curso_idcurso)
references curso(idcurso),
constraint fk_cursocursoaluno foreign key (aluno_idaluno)
references aluno(idaluno)
);

/*======================================= ADICIONANDO DADOS =====================================================================*/
use Curso;
/*Adicionando Professores*/
insert into professor(nome,email,cpf,endereco,numero,complemento,cidade,estado) values ("José","jose123@gmail.com",11111111111,"rua sebastião batista",1502,"rua perto da esquina","Járu","RO");
insert into professor(nome,email,cpf,endereco,numero,complemento,cidade,estado) values ("João Corso","corsinha_rei_dela_1243@gmail.com",22222222222,"Avenida Zacarias Rocha",1045,"rua perto do mercado","Vilhena","RO");
insert into professor(nome,email,cpf,endereco,numero,complemento,cidade,estado) values ("Carlos","carlistosplay@gmail.com",33333333333,"Rua Dezenove",2454,"rua perto da papelaria","Vilhena","RO");
insert into professor(nome,email,cpf,endereco,numero,complemento,cidade,estado) values ("Maria","maria123@gmail.com",44444444444,"Rua Vinte",1503,"rua perto da padaria","Vilhena","RO");
insert into professor(nome,email,cpf,endereco,numero,complemento,cidade,estado) values ("Ana","ana123@gmail.com",55555555555,"Avenida Vinte e Um",1046,"rua perto do açougue","Vilhena","RO");
insert into professor(nome,email,cpf,endereco,numero,complemento,cidade,estado) values ("Paulo","paulo123@gmail.com",66666666666,"Rua Vinte e Dois",2455,"rua perto da farmácia","Vilhena","RO");
insert into professor(nome,email,cpf,endereco,numero,complemento,cidade,estado) values ("Pedro","pedro123@gmail.com",77777777777,"Avenida Vinte e Três",1504,"rua perto do restaurante","Vilhena","RO");
insert into professor(nome,email,cpf,endereco,numero,complemento,cidade,estado) values ("Lucas","lucas123@gmail.com",88888888888,"Rua Vinte e Quatro",1047,"rua perto do supermercado","Vilhena","RO");

/*Adicionando Cursos*/
insert into curso(nome,professor_id) values ("Engenharia",1),("Farmácia",2),("Robótica",3),("IMC",4),("Banco de Dados",5),("Humanas",6),("Exatas",7),("Inglês",8);

/*Adicionando Alunos*/
insert into aluno(nome, email, cpf, endereco, numero, complemento, cidade, estado) VALUES
("João", "joao@example.com", 98765432102, "Rua das Flores", 123, "Apto 4A", "Vilhena", "RO"),
("Maria", "maria@example.com", 65432198703, "Avenida Central", 456, "Bloco B", "Vilhena", "RO"),
("Carlos", "carlos@example.com", 32198765404, "Rua dos Passarinhos", 789, "Casa Verde", "Vilhena", "RO"),
("Ana", "ana@example.com", 78901234505, "Alameda das Árvores", 101, "Casa Amarela", "Vilhena", "RO"),
("Pedro", "pedro@example.com", 54321098706, "Travessa da Praia", 222, "Andar 5", "Vilhena", "RO"),
("Isabel", "isabel@example.com", 21098765407, "Rua dos Coqueiros", 333, "Casa Azul", "Vilhena", "RO"),
("Miguel", "miguel@example.com", 87654321008, "Avenida Principal", 789, "Bloco C", "Vilhena", "RO"),
("Larissa", "larissa@example.com", 10987654309, "Rua da Liberdade", 654, "Apartamento 7", "Vilhena", "RO"),
("Ricardo", "ricardo@example.com", 76543210910, "Avenida Central", 567, "Casa Laranja", "Vilhena", "RO"),
("Juliana", "juliana@example.com", 54321098711, "Rua da Praça", 432, "Apto 9B", "Vilhena", "RO"),
("Lucas", "lucas@example.com", 21098765412, "Alameda dos Pinheiros", 654, "Casa Verde", "Vilhena", "RO"),
("Fernanda", "fernanda@example.com", 98765432113, "Rua da Esquina", 123, "Apartamento 2", "Vilhena", "RO"),
("Gustavo", "gustavo@example.com", 65432198714, "Avenida dos Girassóis", 456, "Bloco D", "Vilhena", "RO"),
("Amanda", "amanda@example.com", 32198765415, "Rua das Palmeiras", 789, "Casa Amarela", "Vilhena", "RO"),
("Paulo", "paulo@example.com", 78901234516, "Travessa do Bosque", 101, "Casa Azul", "Vilhena", "RO"),
("Patricia", "patricia@example.com", 54321098717, "Alameda das Rosas", 222, "Andar 8", "Vilhena", "RO"),
("André", "andre@example.com", 21098765418, "Rua das Montanhas", 333, "Casa Vermelha", "Vilhena", "RO"),
("Camila", "camila@example.com", 87654321019, "Avenida dos Pássaros", 789, "Bloco E", "Vilhena", "RO"),
("Eduardo", "eduardo@example.com", 10987654320, "Rua da Praia", 654, "Apartamento 5A", "Vilhena", "RO"),
("Carolina", "carolina@example.com", 76543210921, "Alameda dos Cactos", 567, "Casa Lilás", "Vilhena", "RO"),
("Roberto", "roberto@example.com", 54321098722, "Travessa do Sol", 432, "Apto 3B", "Vilhena", "RO"),
("Mariana", "mariana@example.com", 21098765423, "Rua das Estrelas", 123, "Casa Marrom", "Vilhena", "RO"),
("Sergio", "sergio@example.com", 98765432124, "Avenida dos Planetas", 456, "Bloco F", "Vilhena", "RO"),
("Laura", "laura@example.com", 65432198725, "Rua do Universo", 789, "Casa Dourada", "Vilhena", "RO"),
("Angelo","Angelo123@gmail.com",12345678901,"rua sebastião batista",1502,"rua perto da esquina","Vilhena","RO");

/*Adicionando id dos alunos e id do curso a tabela curso aluno*/
insert into cursoaluno(curso_idcurso,aluno_idaluno) values (1,1),(1,2),(1,3),(1,4),(1,5),(2,6),(2,7),(2,8),(2,9),(2,10),(3,11),(3,12),(3,13),(3,14),(3,15),(4,16),(4,17),(4,18),(4,19),(4,20),(5,21),(5,22),(5,23),(5,24),(5,25);

/*================================================================ ALTERANDO E ADICIONANDO NOVOS DADOS A TABELA ===========================================================================*/
use Curso;
/*alterando dados*/
alter table professor add salario double;
alter table curso add valor double;
alter table curso add cargahoraria float;

/*Adicionando salário aos professores*/
update professor set salario= 4000 where idprofessor=3;
update professor set salario= 3700 where idprofessor=1;
update professor set salario= 5000 where idprofessor=2;
update professor set salario= 4500 where idprofessor=4;
update professor set salario= 4200 where idprofessor=5;
update professor set salario= 5500 where idprofessor=6;
update professor set salario= 4800 where idprofessor=7;
update professor set salario= 5300 where idprofessor=8;

/*Adicionando valor e carga horária ao curso*/
update curso set valor=300, cargahoraria=40 where idcurso=2;
update curso set valor=350, cargahoraria=20 where idcurso=1;
update curso set valor=200, cargahoraria=35 where idcurso=3;
update curso set valor=120, cargahoraria=30 where idcurso=4;
update curso set valor=150, cargahoraria=10 where idcurso=5;
update curso set valor=500, cargahoraria=30 where idcurso=6;
update curso set valor=400, cargahoraria=35 where idcurso=7;
update curso set valor=200, cargahoraria=50 where idcurso=8;

/*============================================================== CONSULTANDO DADOS ======================================================================================================================
/*Consultar todos os alunos e professores*/
use Curso;
select idprofessor,nome,email,cpf,endereco,numero,complemento,cidade,estado from professor union select * from aluno;

/*Consultar alunos 1 aluno por cpf, cidade, estado*/
select * from aluno where cpf = 54321098711 and cidade = 'Vilhena' and estado = 'RO';

/*Consultar 2 cursos pelo id e nome*/
select * from curso where idcurso = 4 or nome = "Farmácia";

/*Consultar 2 professor pelo cpf e salario*/
select * from professor where idprofessor = 1 or salario = 4000;
