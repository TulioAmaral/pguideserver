# -*- coding: utf-8 -*-
#from django.contrib.auth import authenticate
import simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User
from PGuideServer.nucleo.models import Usuario, Item, Marca, Categoria,\
    UnidadeDeMedida, ItemLista, ItemEstabelecimento, HistoricoConsultas,\
    Estabelecimento, PreferenciasDoUsuario, FormasDePagamento, Reputacao
from django.core import serializers
from PGuideServer.Recomendacao.utils import Localizacao, Valores
from PGuideServer.Recomendacao.views import avaliar, avaliarMultiplosItens,\
    recomendacaoProbabilistica

def getNomeItem(request):
    username = request.GET['username']
    id_ = request.GET['id']
    
    if Usuario.objects.get(username=username) is not None:
        item = ItemEstabelecimento.objects.get(id=id_)
        return HttpResponse(simplejson.dumps({"nome":item.item.nome}),
                            content_type = 'application/json; charset=utf8')
    

def buscarOfertas(request):
    username = request.GET['username']
    
    try:
        user = Usuario.objects.get(username=username)
    except:
        pass
    
    if user is not None:
        itens = recomendacaoProbabilistica(user, 5)
        lista = list()
        for item in itens:
            lista.append(ItemEstabelecimento.objects.get(id=item).id)
    
        return HttpResponse(simplejson.dumps({"lista":lista}), 
                            content_type = 'application/json; charset=utf8')
        

def avaliarEstabelecimento(request):
    username = request.GET['username']
    estabelecimento_id = request.GET['estabelecimento']
    avaliacao = request.GET['avaliacao']
    
    user = Usuario.objects.get(username=username)
    if user is not None:
        estabelecimento = Estabelecimento.objects.get(pk=estabelecimento_id)
        estabelecimento.reputacao.addVoto(avaliacao)
        estabelecimento.reputacao.save(force_update=True)
        return HttpResponse(simplejson.dumps({"ok":True}), content_type = 'application/json; charset=utf8')

def login(request):
    username = request.GET['username']
    password = request.GET['password']
    
    try:
        #user = authenticate(username = username, password = password)
        user = User.objects.get(username = username)
        if user.password != password:
            user = None
    except:
        user = None
        
    if user is not None:
        if user.is_active:
            return HttpResponse(
                simplejson.dumps({"login": True}), 
                content_type = 'application/json; charset=utf8'
            )
    return HttpResponse(
        simplejson.dumps({"login": False}), 
        content_type = 'application/json; charset=utf8'
    )
    
def cadastrar_usuario(request):
    nome = request.GET['nome']
    sobrenome = request.GET['sobrenome']
    cidade = request.GET['cidade']
    estado = request.GET['estado']
    email = request.GET['email']
    senha = request.GET['senha']
    
    dictionary = {"sucesso_cadastro": True}
    
    usuario = Usuario()
    usuario.username = email
    usuario.first_name = nome
    usuario.last_name = sobrenome
    usuario.email = email
    usuario.password = senha
    
    usuario.cidade = cidade
    usuario.estado = estado
    try:
        usuario.save()
    except Exception as error:
        dictionary["sucesso_cadastro"] =  False
        dictionary["erro"] = error
        print error
        
    return HttpResponse(
        simplejson.dumps(dictionary), 
        content_type = 'application/json; charset=utf8'
    )

def cadastrar_preferencias(request):
    username = request.GET['username']
    minPreco = request.GET['minPreco']
    maxPreco = request.GET['maxPreco']
    irPreco = request.GET['irPreco']
    minReputacao = request.GET['minReputacao']
    irReputacao = request.GET['irReputacao']
    minDistancia = request.GET['minDistancia']
    maxDistancia = request.GET['maxDistancia']
    irDistancia = request.GET['irDistancia']
    formasDePagamento = request.GET['formasDePagamento']
    
    pref = PreferenciasDoUsuario()
    pref.minPrecoItem = minPreco
    pref.maxPrecoItem = maxPreco
    pref.relevanciaPrecoItem = irPreco
    pref.minReputacaoItem = minReputacao
    pref.maxReputacaoItem = 5
    pref.relevanciaReputacaoItem = irReputacao
    pref.minDistanciaItem = minDistancia
    pref.maxDistanciaItem = maxDistancia
    pref.relevanciaDistanciaItem = irDistancia
    pref.formasPagamento = formasDePagamento
    
    try:
        user = Usuario.objects.get(username=username)
        if user.preferencias is not None:
            pref.id = user.preferencias
            pref.save(force_update=True)
        else:
            pref.save()
        user.preferencias = pref
        user.save(force_update=True)
    except Exception as error:
        print error
        
    return HttpResponse(
        simplejson.dumps({'sucesso_cadastro': True}), 
        content_type = 'application/json; charset=utf8'
    )
    
def limparListaDeCompras(request):
    username = request.GET['username']
    
    dictionary = {"sucesso_limpar_lista": True}
    
    try:
        user = Usuario.objects.get(username = username)
    except Exception as error:
        dictionary["sucesso_limpar_lista"] = False
        dictionary["erro"] = error
        
    try:
        itens = []
        itens.extend(ItemLista.objects.filter(user = user, status = 1))
        itens.extend(ItemLista.objects.filter(user = user, status = 2))
        for item in itens:
            item.status = 5
            item.save(force_update=True)
    except Exception as error:
        dictionary["sucesso_limpar_lista"] =  False
        dictionary["erro"] = error
        
    return HttpResponse(
        simplejson.dumps(dictionary), 
        content_type = 'application/json; charset=utf8'
    )

def getProfile(request):
    username = request.GET['username']
    
    try:
        usuario = Usuario.objects.get(username = username)
    except:
        pass
        
    if usuario is not None:
        return HttpResponse(
            simplejson.dumps({"username": usuario.username,
                              "email": usuario.email,
                              "nome": usuario.first_name,
                              "sobrenome": usuario.last_name,
                              "cidade": usuario.cidade,
                              "estado": usuario.estado}), 
            content_type = 'application/json; charset=utf8'
        )
    return HttpResponse(
        simplejson.dumps({"username": "-1"}), 
        content_type = 'application/json; charset=utf8'
    )
    
def getReputacao(request):
    rep_id = request.GET['id']

    reputacao = Reputacao.objects.get(pk = rep_id)
    return HttpResponse(
        simplejson.dumps({"avaliacoes":reputacao.quantidade_avaliacoes,"media":reputacao.media}), 
        content_type = 'application/json; charset=utf8')
        

def getPreferencias(request):
    username = request.GET['username']
    
    try:
        usuario = Usuario.objects.get(username = username)
    except:
        pass
        
    if usuario is not None:
        preferencias = PreferenciasDoUsuario.objects.get(id=usuario.preferencias)
        return HttpResponse(
            simplejson.dumps({
                              "minPrecoItem": preferencias.minPrecoItem,
                              "maxPrecoItem": preferencias.maxPrecoItem, # 1 mi
                              "relevanciaPrecoItem": preferencias.relevanciaPrecoItem, # 100%
                            
                              "minDistanciaItem": preferencias.minDistanciaItem,
                              "maxDistanciaItem": preferencias.maxDistanciaItem, # 20.000 km
                              "relevanciaDistanciaItem": preferencias.relevanciaDistanciaItem,
                            
                              "minReputacaoItem": preferencias.minReputacaoItem,
                              "maxReputacaoItem": preferencias.maxReputacaoItem, # 5 estrelas
                              "relevanciaReputacaoItem": preferencias.relevanciaReputacaoItem,
                            
                              "formasPagamento": preferencias.formasPagamento
                              }, indent=2), 
            content_type = 'application/json; charset=utf8'
        )
    return HttpResponse(
        simplejson.dumps({"username": "-1"}), 
        content_type = 'application/json; charset=utf8'
    )

def getMarca(request):
    marca_id = request.GET['marca_id']
    
    marca = Marca.objects.get(id = marca_id)
    
    return HttpResponse(
        simplejson.dumps({"marca": marca.nome}), 
        content_type = 'application/json; charset=utf8'
    )


def getUnidadesDeMedida(request):
    unidades = UnidadeDeMedida.objects.all()
    l = []
    for unidade in unidades:
        l.append(unidade.unidade)
    
    return HttpResponse(
        simplejson.dumps({"unidades": l}), 
        content_type = 'application/json; charset=utf8'
    )


def getCategorias(request):
    categorias = Categoria.objects.all()
    l = []
    for categoria in categorias:
        l.append(categoria.categoria)
    
    return HttpResponse(
        simplejson.dumps({"categorias": l}), 
        content_type = 'application/json; charset=utf8'
    )
    

def pesquisar(request):
    palavra_chave = request.GET['palavra_chave']
    username = request.GET['username']
    
    try:
        user = User.objects.get(username = username)
    except:
        pass
    
    query = Item.objects.filter(nome__contains = palavra_chave)
    data = serializers.serialize("json", query, indent=2)
    
    if user is not None:
        return HttpResponse(data, content_type = "application/json; charset=utf8")
    
def getEstabelecimentos(request):
    palavra_chave = request.GET['palavra_chave']
    username = request.GET['username']
    
    try:
        user = User.objects.get(username=username)
    except:
        pass
    query = []
    query.extend(Estabelecimento.objects.filter(nome_curto__contains=palavra_chave))
    query = list(set(query).union(Estabelecimento.objects.filter(nome_completo__contains=palavra_chave)))
    data = serializers.serialize("json", query, indent=2)
    if user is not None:
        return HttpResponse(data, content_type = "application/json; charset=utf8")
    
def getFormasDePagamento(request):
    username = request.GET['username']
    
    try:
        user = User.objects.get(username = username)
    except:
        pass
    
    query = FormasDePagamento.objects.all()
    data = serializers.serialize("json", query, indent=2)
    
    if user is not None:
        return HttpResponse(data, content_type = "application/json; charset=utf8")
    

def getItemID(request):
    codigo = request.GET['codigo']
    username = request.GET['username']
    
    try:
        user = User.objects.get(username = username)
    except:
        pass
    
    try:
        item = Item.objects.get(codigo = codigo)
    except:
        item = Item()
        item.id = -1
    
    if user is not None:
        return HttpResponse(
            simplejson.dumps({"item_id": item.id}), 
            content_type = 'application/json; charset=utf8'
        )

def getEstabelecimento(request):
    id = request.GET["id"]

    estabelecimento = Estabelecimento.objects.filter(pk=id)
    
    data = serializers.serialize("json", estabelecimento, indent=2)
    return HttpResponse(data, content_type = 'application/json; charset=utf8')
    
def getItemEstabelecimento(request):
    id = request.GET["id"]

    itemEstabelecimento = ItemEstabelecimento.objects.filter(pk=id)
    
    data = serializers.serialize("json", itemEstabelecimento, indent=2)
    return HttpResponse(data, content_type = 'application/json; charset=utf8')
    

def getItem(request):
    n_id = int(request.GET['id'])
    username = request.GET['username']
    
    try:
        user = User.objects.get(username = username)
    except:
        pass
    
    try:
        item = Item.objects.filter(id = n_id)
    except:
        pass
    
    data = serializers.serialize("json", item, indent=2)
    
    if user is not None:
        return HttpResponse(data, 
            content_type = 'application/json; charset=utf8'
        )


def getListaDeCompras(request):
    username = request.GET['username']
    
    try:
        user = User.objects.get(username = username)
    except:
        pass
    
    lista = []
    try:
        lista.extend(ItemLista.objects.filter(user = user, status = 1)) # ativos não comprados
        lista.extend(ItemLista.objects.filter(user = user, status = 2)) # ativos comprados
    except:
        pass
    
    data = serializers.serialize("json", lista, indent=2)
    
    if user is not None:
        return HttpResponse(data, 
            content_type = 'application/json; charset=utf8'
        )
    

def adicionarItemNaLista(request):
    username = request.GET['username']
    item = Item.objects.get(id = request.GET['item'])
    status = request.GET['status']
    quantidade = request.GET['quantidade']
    
    try:
        user = Usuario.objects.get(username = username)
        novo_item_da_lista = ItemLista()
        novo_item_da_lista.user = user
        novo_item_da_lista.status = status
        novo_item_da_lista.quantidade = quantidade
        novo_item_da_lista.item = item
        novo_item_da_lista.save()
        results = {"sucesso_add_item": True}
    except Exception, e:
        results = {"sucesso_add_item": False}
        results["erro"] = e
    
    return HttpResponse(
        simplejson.dumps(results), 
        content_type = 'application/json; charset=utf8'
    )


def alterarStatusDoItemDaLista(request):
    username = request.GET['username']
    _id = request.GET['id']
    status = request.GET['status']
    
    try:
        user = Usuario.objects.get(username = username)
        if user is not None:
            item_lista = ItemLista.objects.get(id = _id)
            item_lista.status = status
            item_lista.save(force_update = True)
            results = {"sucesso_alterar_status_item": "ok"}
    except Exception as error:
        results = {"sucesso_alterar_status_item": error}
    
    return HttpResponse(
        simplejson.dumps(results), 
        content_type = 'application/json; charset=utf8'
    )


def removerItemDaLista(request):
    username = request.GET['username']
    _id = request.GET['id']
    
    try:
        user = Usuario.objects.get(username = username)
        if user is not None:
            item_lista = ItemLista.objects.get(id = _id)
            item_lista.status = 5
            item_lista.save(force_update = False)
            results = {"sucesso_remover_item_da_lista": "ok"}
    except Exception as error:
        results = {"sucesso_remover_item_da_lista": error}
    
    return HttpResponse(
        simplejson.dumps(results), 
        content_type = 'application/json; charset=utf8'
    )


def buscarRecomendacaoProduto(request):
    '''
        /buscarRecomendacaoProduto? username=XXX & ID=XXX & 
                                    latitude=XXX & longitude=XXX
                                    
    '''
    
    username = request.GET['username']
    id_item = request.GET['ID']
    latitude = float(request.GET['latitude'])
    longitude = float(request.GET['longitude'])
    userLocation = Localizacao(latitude, longitude)
    try:
        user = Usuario.objects.get(username=username)
    except Exception, e:
        print e
        return None
    #criterios = request.GET['criterios'] # vem no formato de cadeia de caracteres binários: 0110
    
    busca = res_busca = []
    
    try:
        busca.extend(ItemEstabelecimento.objects.filter(item = id_item, disponibilidade = 1))
        busca.extend(ItemEstabelecimento.objects.filter(item = id_item, disponibilidade = 2))
    except:
        busca = []
    
    try:
        preferencias = PreferenciasDoUsuario.objects.get(pk=user.preferencias)
        ind_preco = Valores(preferencias.minPrecoItem, preferencias.maxPrecoItem, preferencias.relevanciaPrecoItem)
        ind_rep = Valores(preferencias.minReputacaoItem, preferencias.maxReputacaoItem, preferencias.relevanciaReputacaoItem)
        ind_dist = Valores(preferencias.minDistanciaItem, preferencias.maxDistanciaItem, preferencias.relevanciaDistanciaItem)
        res_busca = avaliar(userLocation, busca, ind_preco, ind_rep, ind_dist, None)
    except Exception, e:
        print e
    
    try:
        historico = HistoricoConsultas()
        historico.user = user
        historico.item = Item.objects.get(pk=id_item)
        historico.save()
    except:
        pass
    
    data = serializers.serialize("json", res_busca, indent=2)
    
    if user is not None:
        return HttpResponse(data, 
            content_type = 'application/json; charset=utf8'
        )


def buscarRecomendacaoLista(request):
    '''
        /buscarRecomendacaoLista? username=XXX & 
                                    latitude=XXX & longitude=XXX
                                    
    '''
    username = request.GET['username']
    latitude = float(request.GET['latitude'])
    longitude = float(request.GET['longitude'])
    
    userLocation = Localizacao(latitude, longitude)
    try:
        user = Usuario.objects.get(username=username)
    except Exception, e:
        print e
        return None
    
    estabs = []
    try:
        preferencias = PreferenciasDoUsuario.objects.get(pk=user.preferencias)
        ind_preco = Valores(preferencias.minPrecoItem, preferencias.maxPrecoItem, preferencias.relevanciaPrecoItem)
        ind_rep = Valores(preferencias.minReputacaoItem, preferencias.maxReputacaoItem, preferencias.relevanciaReputacaoItem)
        ind_dist = Valores(preferencias.minDistanciaItem, preferencias.maxDistanciaItem, preferencias.relevanciaDistanciaItem)
        item_list = ItemLista.objects.filter(user=user.user_ptr_id, status=1)
        estabs = avaliarMultiplosItens(userLocation, item_list, ind_preco, ind_rep, ind_dist, None)
    except Exception, e:
        print "erro",e
    
    data = serializers.serialize("json", estabs, indent=2)
    
    if user is not None:
        return HttpResponse(data, 
            content_type = 'application/json; charset=utf8'
        )


