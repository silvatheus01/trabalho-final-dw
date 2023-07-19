CREATE DATABASE db_beneficios_tangua;
USE db_beneficios_tangua;

CREATE TABLE tb_mes (
	id_mes INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    mes DATETIME
);

CREATE TABLE tb_beneficiario (
	id_beneficiario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(20),
    nis VARCHAR(20),
    nome VARCHAR(100)
);

CREATE TABLE tb_tipo_beneficio (
	id_tipo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50)
);

CREATE TABLE tb_valor_disponibilizado (
	id_valor INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_mes int NOT NULL,
    id_tipo_beneficio INT NOT NULL,
    ds_beneficio VARCHAR(50),
    qt_beneficiarios INT,
    valor VARCHAR(15),
    FOREIGN KEY (id_tipo_beneficio) REFERENCES tb_tipo_beneficio(id_tipo),
    FOREIGN KEY (id_mes) REFERENCES tb_mes(id_mes)
);

CREATE TABLE tb_pagamento_disponibilizado_ab (
    id_pagamento_liberado int NOT NULL primary key auto_increment, 
    id_mes int NOT NULL,
    id_beneficiario int not null,
    valor varchar(10),
    FOREIGN KEY (id_beneficiario) REFERENCES tb_beneficiario(id_beneficiario),
    FOREIGN KEY (id_mes) REFERENCES tb_mes(id_mes)
); 

CREATE TABLE tb_pagamento_disponibilizado_bf (
    id_pagamento_liberado int NOT NULL primary key auto_increment, 
    id_mes int NOT NULL,
    id_beneficiario int not null,
    qt_dependentes varchar(10),
    valor varchar(10),
    FOREIGN KEY (id_beneficiario) REFERENCES tb_beneficiario(id_beneficiario),
    FOREIGN KEY (id_mes) REFERENCES tb_mes(id_mes)
); 

CREATE TABLE tb_pagamento_disponibilizado_ae (
    id_pagamento_liberado int NOT NULL primary key auto_increment, 
    id_mes int NOT NULL,
    id_beneficiario int not null,
    observacao varchar(200),
    enquadramento varchar(200),
    parcela varchar(200),
    valor varchar(10),
    FOREIGN KEY (id_beneficiario) REFERENCES tb_beneficiario(id_beneficiario),
    FOREIGN KEY (id_mes) REFERENCES tb_mes(id_mes)
); 

CREATE TABLE tb_pagamento_disponibilizado_bpc (
    id_pagamento_liberado int NOT NULL primary key auto_increment, 
    id_mes int NOT NULL,
    id_beneficiario int not null,
    nome_representante_legal varchar(100),
    bt_concedido_judicialmente bool,
    bt_menor_16 bool,
    valor varchar(10),
    FOREIGN KEY (id_beneficiario) REFERENCES tb_beneficiario(id_beneficiario),
    FOREIGN KEY (id_mes) REFERENCES tb_mes(id_mes)
); 