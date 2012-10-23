INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (0, "grama(s)", "g");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (1, "quilo(s)", "kg");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (2, "tonelada(s)", "t");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (3, "milímetro(s)", "mm");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (4, "centímetro(s)", "cm");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (5, "metro(s)", "m");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (6, "unidade(s)", "");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (7, "caixa(s)", "cx");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (8, "mililitro(s)", "ml");
INSERT INTO nucleo_unidadedemedida (id, unidade, sigla) VALUES (9, "litro(s)", "L");

INSERT INTO nucleo_categoria (id, categoria) VALUES (0, "Alimentos e bebidas");
INSERT INTO nucleo_categoria (id, categoria) VALUES (1, "Automotivo");
INSERT INTO nucleo_categoria (id, categoria) VALUES (2, "Automóveis e motocicletas");
INSERT INTO nucleo_categoria (id, categoria) VALUES (3, "Bebês");
INSERT INTO nucleo_categoria (id, categoria) VALUES (4, "Beleza e saúde");
INSERT INTO nucleo_categoria (id, categoria) VALUES (5, "Brinquedos");
INSERT INTO nucleo_categoria (id, categoria) VALUES (6, "Calçados");
INSERT INTO nucleo_categoria (id, categoria) VALUES (7, "Cama, mesa e banho");
INSERT INTO nucleo_categoria (id, categoria) VALUES (8, "Celulares, smartphones e tablets");
INSERT INTO nucleo_categoria (id, categoria) VALUES (9, "Câmeras e filmadoras");
INSERT INTO nucleo_categoria (id, categoria) VALUES (10, "Eletrodomésticos");
INSERT INTO nucleo_categoria (id, categoria) VALUES (11, "Eletrônicos");
INSERT INTO nucleo_categoria (id, categoria) VALUES (12, "Esporte e lazer");
INSERT INTO nucleo_categoria (id, categoria) VALUES (13, "Ferramentas");
INSERT INTO nucleo_categoria (id, categoria) VALUES (14, "Filmes");
INSERT INTO nucleo_categoria (id, categoria) VALUES (15, "Games");
INSERT INTO nucleo_categoria (id, categoria) VALUES (16, "Industriais");
INSERT INTO nucleo_categoria (id, categoria) VALUES (17, "Informática");
INSERT INTO nucleo_categoria (id, categoria) VALUES (18, "Instrumentos musicais");
INSERT INTO nucleo_categoria (id, categoria) VALUES (19, "Jogos");
INSERT INTO nucleo_categoria (id, categoria) VALUES (20, "Livros");
INSERT INTO nucleo_categoria (id, categoria) VALUES (21, "Movelaria");
INSERT INTO nucleo_categoria (id, categoria) VALUES (22, "Papelaria");
INSERT INTO nucleo_categoria (id, categoria) VALUES (23, "Perfumaria");
INSERT INTO nucleo_categoria (id, categoria) VALUES (24, "Produtos de limpeza");
INSERT INTO nucleo_categoria (id, categoria) VALUES (25, "Roupas");
INSERT INTO nucleo_categoria (id, categoria) VALUES (26, "Serviços");
INSERT INTO nucleo_categoria (id, categoria) VALUES (27, "Software");
INSERT INTO nucleo_categoria (id, categoria) VALUES (28, "Viagens");

INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (0, "À vista");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (1, "Boleto");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (2, "Cartão - débito à vista");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (3, "Cartão - crédito à vista");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (4, "Cartão - crédito parcelado");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (5, "Prazo - Carnê");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (6, "Prazo - Cheque");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (7, "Depósito ou transferência");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (8, "Paypal");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (9, "Mercado Pago");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (10, "Pagamento digital");
INSERT INTO nucleo_formasdepagamento (id, forma_de_pagamento) VALUES (11, "Pag Seguro");

INSERT INTO nucleo_preferenciasdousuario (id, minPrecoItem, maxPrecoItem, relevanciaPrecoItem, minDistanciaItem, maxDistanciaItem, relevanciaDistanciaItem, minReputacaoItem, maxReputacaoItem, relevanciaReputacaoItem, formasPagamento) VALUES (1, 0, 1000000, 100, 0, 20000000, 100, 0, 5, 100, "[1]");

INSERT INTO auth_user (id, first_name, last_name, username, email, password, is_staff, is_active, is_superuser, last_login, date_joined) VALUES (2, "Alezy", "Oliveira", "alezyoliveira@msn.com", "alezyoliveira@msn.com", "1", 1, 1, 0, "2012-05-28 12:00:54", "2012-05-28 12:00:42");

INSERT INTO nucleo_usuario (user_ptr_id, cidade, estado, preferencias) VALUES (2, "Palmeira dos Índios", "Alagoas", 1);

INSERT INTO nucleo_marca (id, nome) VALUES (1, "All alimentos");
INSERT INTO nucleo_marca (id, nome) VALUES (2, "Bic");

INSERT INTO nucleo_item (id, nome, codigo, marca_id, categoria_id, tamanho, unidade_id) VALUES (1, "Mint Strips", "6928544904377", 1, 1, "16", 7);
INSERT INTO nucleo_item (id, nome, codigo, marca_id, categoria_id, tamanho, unidade_id) VALUES (2, "Pilhas AAA R03 1,5V Super", "7033080198", 2, 12, "4", 7);

INSERT INTO nucleo_itemlista (id, item_id, user_id, quantidade, status) VALUES (1, 1, 2, 2, 1);

INSERT INTO nucleo_reputacao (id, quantidade_avaliacoes, media) VALUES (1, 2, 5.0);
INSERT INTO nucleo_reputacao (id, quantidade_avaliacoes, media) VALUES (2, 2, 3.4);
INSERT INTO nucleo_reputacao (id, quantidade_avaliacoes, media) VALUES (3, 2, 4.1);

INSERT INTO nucleo_estabelecimento (id, nome_curto, nome_completo, endereco, bairro, cidade, estado, cnpj, formas_de_pagamento, reputacao_id, latitude, longitude) VALUES (1, "Ponto Frio", "NOVA PONTOCOM COMERCIO ELETRONICO", "Estrada do Ingai, 200", "Dos Altos", "Barueri", "SP", "09.358.108/0002-06", "[1]", 1, -23.498022, -46.967629);
INSERT INTO nucleo_estabelecimento (id, nome_curto, nome_completo, endereco, bairro, cidade, estado, cnpj, formas_de_pagamento, reputacao_id, latitude, longitude) VALUES (2, "Compra Fácil", "SOC COM IMP HERMES S/A", "Av. Brasil, 44228", "Campo Grande", "Rio de Janeiro", "RJ", "33.068.883/0002-01", "[1]", 2, -22.865687, -43.580608);
INSERT INTO nucleo_estabelecimento (id, nome_curto, nome_completo, endereco, bairro, cidade, estado, cnpj, formas_de_pagamento, reputacao_id, latitude, longitude) VALUES (3, "Americanas", "B2W COMPANHIA GLOBAL DO VAREJO", "Rod BR 101 Sul, km 29.6, 29600", "Pt dos Carvalho", "Cabo de Santo Agostinho", "PE", "00.776.574/0011-28", "[1]", 3, -8.282078, -35.057817);

INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (1, 1, 1, 1, 2.50, 0, "2012-06-24 12:41:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (2, 2, 1, 1, 2.00, 0, "2012-06-24 12:42:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (3, 3, 1, 1, 3.00, 50, "2012-06-24 12:42:32");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (4, 1, 2, 1, 2.25, 15, "2012-06-24 12:46:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (5, 2, 2, 1, 2.10, 5, "2012-06-24 12:49:31");

