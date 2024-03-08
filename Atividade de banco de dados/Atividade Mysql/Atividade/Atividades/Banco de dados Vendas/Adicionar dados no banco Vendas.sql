/*================================================================= Criando Banco De Dados ==================================================================================*/
create database venda;
use venda;

create table estado(
id int(11) auto_increment primary key,
sigla char(2)
);

create table cidade(
id int(11) auto_increment primary key,
nome varchar(38),
estado_id int(11),
constraint fk_cidadeestado foreign key (estado_id)
references estado(id)
);

create table bairro(
id int(11) auto_increment primary key,
nome varchar(100),
cidade_id int(11),
constraint fk_estadobairro foreign key (cidade_id)
references cidade(id)
);

create table endereco(
id bigint(20) auto_increment primary key,
bairro_id int(11),
constraint fk_bairroendereco foreign key (bairro_id)
references bairro(id),
tipo_local varchar(15),
logradouro varchar(128),
numero int(11),
complemento varchar(255)

);

create table ponto(
id bigint(20) auto_increment primary key,
endereco_id bigint(20),
constraint fk_enderecoponto foreign key (endereco_id)
references endereco(id)
);

create table solicitante(
id bigint(20) auto_increment primary key,
endereco_id bigint(20),
constraint fk_enderecoslicitante foreign key (endereco_id)
references endereco(id)
);

create table servico(
id bigint(20) auto_increment primary key,
endereco_id bigint(20),
constraint fk_enderecoservico foreign key (endereco_id)
references endereco(id),
solicitante_id bigint(20),
constraint fk_solicitanteservico foreign key (solicitante_id)
references solicitante(id)
);

/*===================================================================== Adicionando Dados ========================================================================================================*/
use venda;
insert into estado(sigla) values ("RO");
select * from estado;
insert into cidade(nome, estado_id) values("Vilhena",1),("Ouro Preto",1),("Jiparana",1),("Colorado do oeste",1),("Espigão do Oeste",1);

insert into estado(sigla) values ("SP");
select * from estado;
insert into cidade(nome, estado_id) values("São Paulo",2),("Osasco",2),("Guarulhos",2),("Campinas",2),("Sorocaba",2);

select * from cidade;
insert into bairro(nome, cidade_id) values ("Alto Alegre", 1),("Jardim América", 1),("Jardim Vitória", 1),("João Pedro", 1), ("Jardim Oliveira", 1),("Jardim Eldorado",1),("Bela Vista",1),("Residencial Cidade Verde",1),("Residencial Cidade Verde II",1),("Residencial Cidade Verde III",1),("Residencial Cidade Verde IV",1),("Parque Recreativo",1),("Cristo Rei",1),("Nova Jerusálem",1),("Parque Industrial Tranquedo Neves",1);

select * from bairro;
insert into endereco(bairro_id, tipo_local, logradouro, numero, complemento) values (1,"residencial","rua sebastião batista",1502,"rua perto da esquina"),(1,"comercio","Avenida Paraná",1454,"rua perto do mercado Bela vista"), (1,"comercio","Avenida Paraná",3456,"rua perto da escola"),(1,"residencial","Avenida Paraná",9871,"perto da praça Geraldão"),(1,"comercio","Avenida Paraná",3156,"proximo a farmacia");
insert into endereco(bairro_id, tipo_local, logradouro, numero, complemento) values (7,"residencial","Avenida Zacarias Rocha de Azevedo Avenida Armenio Gasparian",1045,"rua perto do mercado"), (7,"comercio","Rua Dezenove",7593,"perto a escola"), (7,"residencial","Rua Trinta e Dois",2054,"perto ao mercado"), (7,"residencial","Rua Dezenove",2454,"rua perto da papelaria"), (7,"residencial","Avenida Brigadeiro Eduardo Gomes",1064,"rua perto da pastelaria");

insert into ponto(endereco_id) values(2),(3),(4);

insert into solicitante(endereco_id) values (7),(6),(5),(4),(3),(2),(1);

insert into servico(endereco_id,solicitante_id) values (6,1),(7,2),(8,3),(9,4),(10,5);

