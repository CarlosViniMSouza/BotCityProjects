-- Criar o banco de dados
create database bot_eleitor_dev;

-- Atribuir os privilégios de acesso aos objetos do banco para o usuário root
GRANT ALL PRIVILEGES ON bot_eleitor_dev.* TO 'root' @'localhost';

-- Acesar o banco de dados: banco
USE bot_eleitor_dev;

-- Criar a tabela: usuario
CREATE TABLE voter(
    cpf varchar(11) NOT NULL,
    nome varchar(100) NOT NULL,
    data_nascimento varchar(10) NOT NULL,
    nome_mae varchar(100) NOT NULL,
    cep varchar(8) NOT NULL,
    nro_endereco varchar(10) NOT NULL,
    PRIMARY KEY (cpf)
);
