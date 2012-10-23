# -*- coding:utf-8 -*-
import operator

from PGuideServer.Recomendacao.utils import calcularDistancia, AvaliacaoItem, Localizacao,\
    AvaliacaoEstabelecimento, Valores
from PGuideServer.nucleo.models import Estabelecimento, ItemEstabelecimento

def avaliar(localizacao_usuario, estabelecimento_item_list, indice_preco, indice_reputacao, indice_proximidade, formas_de_pagamento):
    '''
        @author: alezy oliveira lima
    
        @param localizacao_usuario: localizacao.latitude e localizacao.longitude do usuário
        @type localizacao_usuario: Recomendacao.utils.Localizacao
    
        @param estabelecimento_item_list: lista de estabelecimentos que tem o item pretendido pelo usuário
        @type estabelecimento_item_list: list(ItemEstabelecimento)
        
        @param indice_preco: escala de indice_preco.minimo e indice_preco.maximo indicada pelo usuario
        @param indice_reputacao: escala de indice_reputacao.minimo e indice_reputacao.maximo indicada pelo usuario
        @param indice_proximidade: escala de indice_proximidade.minimo e indice_proximidade.maximo indicada pelo usuario
        @type indice_preco, indice_reputacao, indice_proximidade: Recomendacao.utils.Valores
        
        @param formas_de_pagamento: formas de pagamento indicadas pelo usuario
        @type formas_de_pagamento: list(int)
        
        @rtype: list(AvaliacaoItem)
    '''
    
    lista_estabelecimentos_avaliados = []
    for item_estabelecimento in estabelecimento_item_list:
        x = AvaliacaoItem()
        x.item = item_estabelecimento
        x.pontuacao = 0
        loc_est = Localizacao(item_estabelecimento.estabelecimento.latitude, item_estabelecimento.estabelecimento.longitude)
        
        x.pontuacao += calcularPontuacaoProximidade(indice_proximidade, localizacao_usuario, loc_est)
        x.pontuacao += calcularPontuacaoPreco(indice_preco, item_estabelecimento.preco)
        x.pontuacao += calcularPontuacaoReputacao(indice_reputacao, item_estabelecimento.estabelecimento.reputacao.media)
        # as formas de pagamento nao calculam pontuação, são critérios eliminatórios
        #print "\n\n" + x.item.estabelecimento.nome_curto + "\n" + u"preço: " + str(x.item.preco) + "\n" + str(x.pontuacao) + " pontos"
        lista_estabelecimentos_avaliados.append(x)
        
    # ordenando
    lista_estabelecimentos_avaliados.sort(key=operator.attrgetter('pontuacao'))
    lista_estabelecimentos_avaliados.reverse()
    
    # valores em referência ao percencual
    MAX = lista_estabelecimentos_avaliados[0].pontuacao
    for x in lista_estabelecimentos_avaliados:
        x.pontuacao = float("%.2f"%((100.0 * x.pontuacao) / MAX))
        
    return list(lista_estabelecimentos_avaliados)

    
def avaliarMultiplosItens(localizacao_usuario, item_list, indice_preco, indice_reputacao, indice_proximidade, formas_de_pagamento):
    '''
        @author: alezy oliveira lima
    
        @param localizacao_usuario: localizacao.latitude e localizacao.longitude do usuário
        @type localizacao_usuario: Recomendacao.utils.Localizacao
    
        @param item_list: lista de itens (lista de compras) do usuário
        @type item_list: list(ItemLista)
        
        @param indice_preco: escala de indice_preco.minimo e indice_preco.maximo indicada pelo usuario
        @param indice_reputacao: escala de indice_reputacao.minimo e indice_reputacao.maximo indicada pelo usuario
        @param indice_proximidade: escala de indice_proximidade.minimo e indice_proximidade.maximo indicada pelo usuario
        @type indice_preco, indice_reputacao, indice_proximidade: Recomendacao.utils.Valores
        
        @param formas_de_pagamento: formas de pagamento indicadas pelo usuario
        @type formas_de_pagamento: list(int)
        
        @rtype: list(AvaliacaoEstabelecimento)
    '''

    #1 
    estabs_primeiro_item = ItemEstabelecimento.objects.filter(item = item_list[0].item)
    l_primeiro = []
    for estab in estabs_primeiro_item:
        l_primeiro.append(estab.estabelecimento)
    conj1 = set(l_primeiro) # conjunto de estabs que tem o primeiro item
    #2
    for item in item_list:
        if item is not item_list[0]:
            estabs_item_atual = ItemEstabelecimento.objects.filter(item = item) # lista de estabelecimentos que tem o item atual da iteração
            l_atual = []
            for estab in estabs_item_atual:
                l_atual.append(estab.estabelecimento)
            conjAtual = set(l_atual) # conjunto de estabs que tem o item atual
            conj1 = conj1.intersection(conjAtual) # conjunto de interseção
            
    #3 lista com os estabelecimentos que tem todos os itens
    estabs_final = list(conj1)
    estabs = []
    for estab in estabs_final:
        x = AvaliacaoEstabelecimento()
        x.estabelecimento = estab
        x.preco_total = x.pontuacao = 0
        estabs.append(x)
    
    #4 somatorio dos precos dos itens
    for estab in estabs:
        for item in item_list:
            item_estab = ItemEstabelecimento.objects.get(item=item.item, estabelecimento=estab.estabelecimento)
            estab.preco_total += float("%.2f" % (item_estab.preco * item.quantidade)) # * item_estab.desconto    # não estão sendo calculados os descontos
        
    # cálculo das pontuações
    estabs.sort(key=operator.attrgetter("preco_total"))
    indice_preco.minimo = estabs[0].preco_total
    indice_preco.maximo = estabs[len(estabs)-1].preco_total
    
    for estab in estabs:
        loc_est = Localizacao(estab.estabelecimento.latitude, estab.estabelecimento.longitude)
#        estab.pontuacao += float( "%.2f" % calcularPontuacaoPreco(indice_preco, estab.preco_total) )
#        estab.pontuacao += float( "%.2f" % calcularPontuacaoProximidade(indice_proximidade, localizacao_usuario, loc_est) )
        estab.pontuacao += float( "%.2f" % calcularPontuacaoReputacao(indice_reputacao, estab.estabelecimento.reputacao.media) )
    
    # ordenação e proporcionalização em percentual
    estabs.sort(key=operator.attrgetter("pontuacao"))
    estabs.reverse()
    MAX = estabs[0].pontuacao
    for x in estabs:
        x.pontuacao = float("%.2f"%((100.0 * x.pontuacao) / MAX))
    
    return estabs
    

def calcularPontuacaoProximidade(indice_proximidade, loc_usuario, loc_est):
    '''
        @param indice_proximidade: indice de proximidade (minimo e maximo) definido pelo usuario
        @param loc_usuario: localização atual do usuário (lat/long)
        @param loc_est: localização do estabelecimento (lat/long)
        @rtype: float
    '''
    try:
        distancia = calcularDistancia(loc_usuario, loc_est)
        pontuacao = ( 100.0 - ((distancia - indice_proximidade.diferenca()) * 100.0)/float(indice_proximidade.diferenca()) )
        return float( "%.2f" % (pontuacao * indice_proximidade.relevancia)/100.0 )
    except Exception, e:
        print "Recomendacao.views.calcularPontuacaoProximidade:", e
        return 0

    
def calcularPontuacaoPreco(indice_preco, preco):
    '''
        @param indice_preco: indice de preço (minimo e maximo) definido pelo usuario
        @param preco: preço do produto no estabelecimento
        @rtype: float
    '''
    try:
        pontuacao = ( 100 - ((preco - indice_preco.minimo) * 100)/float(indice_preco.diferenca()) )
    except Exception, e:
        print "Recomendacao.views.calcularPontuacaoPreco:", e    
    return float( "%.2f" % (pontuacao * indice_preco.relevancia)/100.0 )

    
def calcularPontuacaoReputacao(indice_reputacao, reputacao):
    '''
        @param indice_reputacao: indice da reputação (minimo e maximo) definido pelo usuario
        @param reputacao: reputação atual do estabelecimento
        @rtype: float
    '''
    try:
        pontuacao = ((reputacao - indice_reputacao.minimo) * 100)/float(indice_reputacao.diferenca())
    except Exception, e:
        print "Recomendacao.views.calcularPontuacaoReputacao:", e
    return float( "%.2f" % ((pontuacao * indice_reputacao.relevancia)/100.0) )
    
    
    
    