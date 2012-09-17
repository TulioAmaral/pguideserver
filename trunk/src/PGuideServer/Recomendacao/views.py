# -*- coding:utf-8 -*-
import operator

from PGuideServer.Recomendacao.utils import calcularDistancia, AvaliacaoItem, Localizacao

def avaliar(localizacao_usuario, estabelecimento_item_list, indice_preco, indice_reputacao, indice_proximidade, formas_de_pagamento):
    '''
        @author: alezy oliveira lima
    
        @param localizacao_usuario: localizacao.latitude e localizacao.longitude do usuário
        @type localizacao_usuario: Recomendacao.utils.Localizacao
    
        @param item_id: lista de estabelecimentos que tem o item pretendido pelo usuário
        @type item_id: list(ItemEstabelecimento)
        
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
        
    lista_estabelecimentos_avaliados.sort(key=operator.attrgetter('pontuacao'))
    lista_estabelecimentos_avaliados.reverse()
    return list(lista_estabelecimentos_avaliados)

    
def calcularPontuacaoProximidade(indice_proximidade, loc_usuario, loc_est):
    '''
        @param indice_proximidade: indice de proximidade (minimo e maximo) definido pelo usuario
        @param loc_usuario: localização atual do usuário (lat/long)
        @param loc_est: localização do estabelecimento (lat/long)
        @rtype: float
    '''
    try:
        distancia = calcularDistancia(loc_usuario, loc_est)
        pontuacao = ( 100.0 - ((distancia - indice_proximidade.diferenca()) * 100.0)/(indice_proximidade.diferenca()*1.0) )
        return (pontuacao * indice_proximidade.relevancia)/100.0
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
        pontuacao = ( 100.0 - ((preco - indice_preco.diferenca()) * 100)/(indice_preco.diferenca()*1.0) )
    except Exception, e:
        print "Recomendacao.views.calcularPontuacaoPreco:", e
    return (pontuacao * indice_preco.relevancia)/100.0

    
def calcularPontuacaoReputacao(indice_reputacao, reputacao):
    '''
        @param indice_reputacao: indice da reputação (minimo e maximo) definido pelo usuario
        @param reputacao: reputação atual do estabelecimento
        @rtype: float
    '''
    try:
        pontuacao = ((reputacao - indice_reputacao.diferenca()) * 100)/(indice_reputacao.diferenca()*1.0)
    except Exception, e:
        print "Recomendacao.views.calcularPontuacaoReputacao:", e
    return (pontuacao * indice_reputacao.relevancia)/100.0
    
    
    
    