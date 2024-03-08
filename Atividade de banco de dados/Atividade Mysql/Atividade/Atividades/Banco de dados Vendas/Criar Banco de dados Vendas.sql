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