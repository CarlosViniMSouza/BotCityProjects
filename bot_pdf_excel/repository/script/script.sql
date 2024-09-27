-- Apagar o banco de dados
drop database bank_bot_pdf_excel;

-- Criar o banco de dados
create database bank_bot_pdf_excel;

-- Atribuir os privilégios de acesso aos objetos do banco para o usuário root
GRANT ALL PRIVILEGES ON bank_bot_pdf_excel.* TO 'root' @'localhost';

-- Acesar o banco de dados: banco
USE bank_bot_pdf_excel;

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

-- Criar a tabela: usuario
CREATE TABLE user(
    id int AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    login varchar(20) NOT NULL,
    password varchar(20) NOT NULL,
    email varchar(50) NOT NULL,
    PRIMARY KEY (id)
);