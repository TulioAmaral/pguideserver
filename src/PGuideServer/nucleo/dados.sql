INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (1, "grama", "g");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (2, "quilo", "kg");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (3, "tonelada", "t");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (4, "milímetro", "mm");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (5, "centímetro", "cm");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (6, "metro", "m");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (7, "unidade", "");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (8, "caixa", "cx");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (9, "mililitro", "ml");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (10, "litro", "L");

INSERT INTO nucleo_categoria (id, categoria) VALUES (1, "Alimentos e bebidas");
INSERT INTO nucleo_categoria (id, categoria) VALUES (2, "Automotivo");
INSERT INTO nucleo_categoria (id, categoria) VALUES (3, "Automóveis e motocicletas");
INSERT INTO nucleo_categoria (id, categoria) VALUES (4, "Bebês");
INSERT INTO nucleo_categoria (id, categoria) VALUES (5, "Beleza e saúde");
INSERT INTO nucleo_categoria (id, categoria) VALUES (6, "Brinquedos");
INSERT INTO nucleo_categoria (id, categoria) VALUES (7, "Calçados");
INSERT INTO nucleo_categoria (id, categoria) VALUES (8, "Cama, mesa e banho");
INSERT INTO nucleo_categoria (id, categoria) VALUES (9, "Celulares, smartphones e tablets");
INSERT INTO nucleo_categoria (id, categoria) VALUES (10, "Câmeras e filmadoras");
INSERT INTO nucleo_categoria (id, categoria) VALUES (11, "Eletrodomésticos");
INSERT INTO nucleo_categoria (id, categoria) VALUES (12, "Eletrônicos");
INSERT INTO nucleo_categoria (id, categoria) VALUES (13, "Esporte e lazer");
INSERT INTO nucleo_categoria (id, categoria) VALUES (14, "Ferramentas");
INSERT INTO nucleo_categoria (id, categoria) VALUES (15, "Filmes");
INSERT INTO nucleo_categoria (id, categoria) VALUES (16, "Games");
INSERT INTO nucleo_categoria (id, categoria) VALUES (17, "Industriais");
INSERT INTO nucleo_categoria (id, categoria) VALUES (18, "Informática");
INSERT INTO nucleo_categoria (id, categoria) VALUES (19, "Instrumentos musicais");
INSERT INTO nucleo_categoria (id, categoria) VALUES (20, "Jogos");
INSERT INTO nucleo_categoria (id, categoria) VALUES (21, "Livros");
INSERT INTO nucleo_categoria (id, categoria) VALUES (22, "Movelaria");
INSERT INTO nucleo_categoria (id, categoria) VALUES (23, "Papelaria");
INSERT INTO nucleo_categoria (id, categoria) VALUES (24, "Perfumaria");
INSERT INTO nucleo_categoria (id, categoria) VALUES (25, "Produtos de limpeza");
INSERT INTO nucleo_categoria (id, categoria) VALUES (26, "Roupas");
INSERT INTO nucleo_categoria (id, categoria) VALUES (27, "Serviços");
INSERT INTO nucleo_categoria (id, categoria) VALUES (28, "Software");
INSERT INTO nucleo_categoria (id, categoria) VALUES (29, "Viagens");



INSERT INTO auth_user (id, first_name, last_name, username, email, password, is_staff, is_active, is_superuser, last_login, date_joined) VALUES (2, "Alezy", "Oliveira", "alezyoliveira@msn.com", "alezyoliveira@msn.com", "1", 1, 1, 0, "2012-05-28 12:00:54", "2012-05-28 12:00:42");

INSERT INTO nucleo_usuario (id, user_id, cidade, estado) VALUES (1, 2, "Palmeira dos Índios", "Alagoas");



INSERT INTO nucleo_marca (id, nome) VALUES (1, "All alimentos");
INSERT INTO nucleo_marca (id, nome) VALUES (2, "Bic");

INSERT INTO nucleo_item (id, nome, codigo, marca_id, categoria_id, tamanho, unidade_id) VALUES (1, "Mint Strips", "6928544904377", 1, 1, "16", 7);
INSERT INTO nucleo_item (id, nome, codigo, marca_id, categoria_id, tamanho, unidade_id) VALUES (2, "Pilhas AAA R03 1,5V Super", "7033080198", 2, 12, "4", 7);

