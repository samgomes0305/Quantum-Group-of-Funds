SELECT * FROM moedasdigitais.all_coin;

CREATE TABLE all_coin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    simbolo VARCHAR(10),
    valor DECIMAL(20, 10),
    volume_negociacao DECIMAL(20, 10),
    capitalizacao_mercado DECIMAL(20, 10),
    data_criacao DATE,
    outras_informacoes TEXT
);

SELECT * FROM moedasdigitais.all_coin LIMIT 0, 50000


-- foi importado atraves do proprio programas sql, onde se clica com o botão direito em cima da tabela criada e seleciona Tabela da import, 
-- onde voce poder escolher entre criar automatico a tabela
-- usando as informaçoes do CVS escolhido 
