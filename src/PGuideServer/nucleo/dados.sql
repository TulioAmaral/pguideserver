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
INSERT INTO nucleo_marca (id, nome) VALUES (3, "Nobre");
INSERT INTO nucleo_marca (id, nome) VALUES (4, "Bauducco");

INSERT INTO nucleo_item (id, nome, codigo, marca_id, categoria_id, tamanho, unidade_id) VALUES (1, "Mint Strips", "6928544904377", 1, 1, "16", 6);
INSERT INTO nucleo_item (id, nome, codigo, marca_id, categoria_id, tamanho, unidade_id) VALUES (2, "Pilhas AAA R03 1,5V Super", "7033080198", 2, 12, "4", 6);
INSERT INTO nucleo_item (id, nome, codigo, marca_id, categoria_id, tamanho, unidade_id) VALUES (3, "Álcool Etílico Hidratado", "7896547500102", 3, 25, "500", 8);
INSERT INTO nucleo_item (id, nome, codigo, marca_id, categoria_id, tamanho, unidade_id) VALUES (4, "Cookies Original", "7891962026756", 4, 1, "110", 0);
INSERT INTO nucleo_item (id, nome, codigo, marca_id, categoria_id, tamanho, unidade_id) VALUES (5, "Cookies Chocco", "7891962035505", 4, 1, "105", 0);

INSERT INTO nucleo_itemlista (id, item_id, user_id, quantidade, status) VALUES (1, 1, 2, 2, 1);

INSERT INTO nucleo_reputacao (id, quantidade_avaliacoes, media) VALUES (1, 2, 5.0);
INSERT INTO nucleo_reputacao (id, quantidade_avaliacoes, media) VALUES (2, 2, 3.4);
INSERT INTO nucleo_reputacao (id, quantidade_avaliacoes, media) VALUES (3, 2, 4.1);
INSERT INTO nucleo_reputacao (id, quantidade_avaliacoes, media) VALUES (4, 2, 4.6);
INSERT INTO nucleo_reputacao (id, quantidade_avaliacoes, media) VALUES (5, 2, 4.0);
INSERT INTO nucleo_reputacao (id, quantidade_avaliacoes, media) VALUES (6, 2, 3.5);

INSERT INTO nucleo_estabelecimento (id, nome_curto, nome_completo, endereco, bairro, cidade, estado, cnpj, formas_de_pagamento, reputacao_id, latitude, longitude) VALUES (1, "Ponto Frio", "NOVA PONTOCOM COMERCIO ELETRONICO", "Estrada do Ingai, 200", "Dos Altos", "Barueri", "SP", "09.358.108/0002-06", "[1]", 1, -23.498022, -46.967629);
INSERT INTO nucleo_estabelecimento (id, nome_curto, nome_completo, endereco, bairro, cidade, estado, cnpj, formas_de_pagamento, reputacao_id, latitude, longitude) VALUES (2, "Compra Fácil", "SOC COM IMP HERMES S/A", "Av. Brasil, 44228", "Campo Grande", "Rio de Janeiro", "RJ", "33.068.883/0002-01", "[1]", 2, -22.865687, -43.580608);
INSERT INTO nucleo_estabelecimento (id, nome_curto, nome_completo, endereco, bairro, cidade, estado, cnpj, formas_de_pagamento, reputacao_id, latitude, longitude) VALUES (3, "Americanas", "B2W COMPANHIA GLOBAL DO VAREJO", "Rod BR 101 Sul, km 29.6, 29600", "Pt dos Carvalho", "Cabo de Santo Agostinho", "PE", "00.776.574/0011-28", "[1]", 3, -8.282078, -35.057817);
INSERT INTO nucleo_estabelecimento (id, nome_curto, nome_completo, endereco, bairro, cidade, estado, cnpj, formas_de_pagamento, reputacao_id, latitude, longitude) VALUES (4, "Unicompra", "UNICOMPRA SUPERMERCADOS LTDA", "Avenida América, 2960", "Centro", "Palmeira dos Índios", "AL", "78.910.111/0001-28", "[1,2,3,5,8]", 4, -9.408234, -36.631316);
INSERT INTO nucleo_estabelecimento (id, nome_curto, nome_completo, endereco, bairro, cidade, estado, cnpj, formas_de_pagamento, reputacao_id, latitude, longitude) VALUES (5, "Todo Dia", "BOMPREÇO SUPERMERCADOS DO NORDESTE", "Rua São Braz, 51", "Centro", "Palmeira dos Índios", "AL", "00.776.574/0011-17", "[1,3,4,5,6,7,8]", 5, -9.409637, -36.630286);
INSERT INTO nucleo_estabelecimento (id, nome_curto, nome_completo, endereco, bairro, cidade, estado, cnpj, formas_de_pagamento, reputacao_id, latitude, longitude) VALUES (6, "Mercadinho Vieira", "JAMES VIEIRA ME", "Rua Tertuliano Canuto, 108", "São Francisco", "Palmeira dos Índios", "AL", "45.012.345/0001-10", "[1]", 6, -9.414612, -36.622402);

INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (1, 1, 1, 1, 2.50, 0, "2012-06-24 12:41:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (2, 2, 1, 1, 2.00, 0, "2012-06-24 12:42:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (3, 3, 1, 1, 3.00, 50, "2012-06-24 12:42:32");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (4, 1, 2, 1, 2.25, 15, "2012-06-24 12:46:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (5, 2, 2, 1, 2.10, 0, "2012-06-24 12:49:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (6, 4, 3, 1, 1.15, 0, "2012-06-24 12:49:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (7, 5, 3, 1, 1.32, 0, "2012-06-24 12:49:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (8, 6, 3, 1, 1.51, 10, "2012-06-24 12:49:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (9, 5, 4, 1, 2.49, 0, "2012-06-24 12:49:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (10, 6, 4, 1, 2.39, 0, "2012-06-24 12:49:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (11, 5, 5, 1, 2.20, 0, "2012-06-24 12:49:31");
INSERT INTO nucleo_itemestabelecimento (id, estabelecimento_id, item_id, disponibilidade, preco, desconto, data) VALUES (12, 6, 5, 1, 2.25, 5, "2012-06-24 12:49:31");

