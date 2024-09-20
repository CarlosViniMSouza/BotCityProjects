-- Banco de Dados MySQL
-- Apagar o banco de dados
drop database banco_desafio;

-- Criar o banco de dados
create database banco_desafio;

-- Atribuir os privilégios de acesso aos objetos do banco
-- para o usuário root
GRANT ALL PRIVILEGES ON banco_desafio.* TO 'root' @'localhost';

-- Acesar o banco de dados: banco
USE banco_desafio;

-- Criar a tabela: produto
CREATE TABLE product(
    id int AUTO_INCREMENT,
    description varchar(50) NOT NULL,
    unit varchar(5) NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    real_price DECIMAL(10,2) NOT NULL,
    dolar_price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id)
);