/*Aluno: Hiago Gabriel gonçalves andré   | 1° A Informática */

use prova;

/*Questão A*/
insert into fornecedor(nome,cpnj,endereco) values ("João Pedro", "11111111111","casa 1234 Rua 405 bairro Jardim das Oliveiras"),("Ane Carol", "22222222222","casa 9012 Rua 867 bairro Jardim Eldorado"), ("Otávio", "33333333333","casa 7239 Rua 535 bairro Alto Alegre"); 

/*Questão B*/
insert into produto(nome,valor,quantidade,fornecedor_idfornecedor) values ("Ração",50.00,30,1),("Filtro de linha",80.00,50,3),("Panela",75.00,10,2),("Coleira",20.00,40,1),("Notebook",1500.00,10,3);

/*Questão C*/
alter table produto add peso float;

/*Questão D*/
update produto set peso = 10.000 where idproduto = 1;
update produto set peso = 0.200 where idproduto = 2;
update produto set peso = 0.500 where idproduto = 3;
update produto set peso = 0.010 where idproduto = 4;
update produto set peso = 0.500 where idproduto = 5;

/*Questão E*/
select nome,valor from produto order by valor;

/*Questão F*/
select nome from produto where nome like "R%";
select nome from produto where nome like "%e%";
select nome from produto where nome like "%a";
select nome from fornecedor where nome like "J%";
select nome from fornecedor where nome like "%a%";
select nome from fornecedor where nome like "%o";

/*Questão G*/
select nome,valor,peso from produto where valor > 1000;
select nome,valor,peso from produto where valor < 50;
select nome,valor,peso from produto where valor = 80;
select nome,valor,peso from produto where valor < 70 or peso > 1;
select nome,valor,peso from produto where valor < 60 and peso = 10;

/*Questão H*/
select produto.nome,produto.valor,fornecedor.nome from produto inner join fornecedor where produto.fornecedor_idfornecedor = fornecedor.idfornecedor;