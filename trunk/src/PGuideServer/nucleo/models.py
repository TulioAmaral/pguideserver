# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from PGuideServer.nucleo.combo_fields import COMBO_ESTADOS, CATEGORIAS_ITENS
import datetime

class Marca(models.Model):
    nome = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.nome
    
    def field_list(self):
        return [(u'nome', self.nome)]


class Categoria(models.Model):
    categoria = models.CharField(max_length = 100, choices = CATEGORIAS_ITENS)
    
    def __unicode__(self):
        return self.categoria
    
    def field_list(self):
        return [(u'categoria', self.categoria)]


class UnidadeDeMedida(models.Model):
    #simbolo = models.CharField(max_length = 10)
    unidade = models.CharField(max_length = 20)
    sigla = models.CharField(max_length = 10)
    
    def __unicode__(self):
        return self.unidade
    
    def field_list(self):
        return [(u'unidade', self.unidade),
                (u'sigla', self.sigla)]
    

class Item(models.Model):
    codigo = models.CharField(max_length = 100, unique = True)
    nome = models.CharField(max_length = 100)
    marca = models.ForeignKey(Marca)
    categoria = models.ForeignKey(Categoria)
    tamanho = models.CharField(max_length = 20)
    unidade = models.ForeignKey(UnidadeDeMedida)
    
    def __unicode__(self):
        return "%s %s%s - %s" % self.nome, self.tamanho, self.unidade, self.marca
    
    def field_list(self):
        return [(u'codigo', self.codigo),
                (u'nome', self.nome),
                (u'marca', self.marca),
                (u'categoria', self.categoria),
                (u'tamanho', self.tamanho),
                (u'unidade', self.unidade)]
    

class ItemLista(models.Model):
    '''
    Relaciona os itens que usuários possuem em sua lista de compras
    
        # status:
        #    1 = ativo (para comprar)
        #    2 = ativo (já comprado)
        #    3 = arquivado (comprado)
        #    4 = arquivado (cancelado)
        #    4 = excluído (invisível para o usuário, mas útil para a recomendação)
    '''
    item = models.ForeignKey(Item)
    user = models.ForeignKey("Usuario")
    quantidade = models.FloatField()
    status = models.IntegerField()

    
    def field_list(self):
        return [(u'item', self.item),
                (u'user', self.user),
                (u'quantidade', self.quantidade),
                (u'status', self.status)]


#class Usuario(models.Model):
class Usuario(User):
    # more info: https://docs.djangoproject.com/en/dev/topics/auth/
    #user = models.OneToOneField(User)
    # username
    # first_name
    # last_name
    # email
    # password
    # date_joined
    cidade = models.CharField(max_length = 100)
    estado = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.user.username
    
    def field_list(self):
        return [(u'user', self.user)]


class HistoricoConsultas(models.Model):
    user = models.ForeignKey(Usuario)
    item = models.ForeignKey(Item)


class Estabelecimento(models.Model):
    nome_curto = models.CharField(max_length = 50)
    nome_completo = models.CharField(max_length = 100)
    endereco = models.TextField(max_length = 1000)
    bairro = models.CharField(max_length = 200)
    cidade = models.CharField(max_length = 100)
    estado = models.CharField(max_length = 100, choices = COMBO_ESTADOS)
    cnpj = models.CharField(max_length = 40)
    formas_de_pagamento = models.CharField(max_length = 100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __unicode__(self):
        return self.nome_curto
    
    def field_list(self):
        return [(u'nome_curto', self.nome_curto),
                (u'nome_completo', self.nome_completo),
                (u'endereco', self.endereco),
                (u'bairro', self.bairro),
                (u'cidade', self.cidade),
                (u'estado', self.estado),
                (u'cnpj', self.cnpj),
                (u'formas_de_pagamento', self.formas_de_pagamento),
                (u'latitude', self.latitude),
                (u'longitude', self.longitude)]


class ItemEstabelecimento(models.Model):
    # disponibilidade:
    #    1: disponível em estoque
    #    2: disponível para pré-venda
    #    3: indisponível
    estabelecimento = models.ForeignKey(Estabelecimento)
    item = models.ForeignKey(Item)
    disponibilidade = models.IntegerField()
    preco = models.FloatField()
    desconto = models.FloatField()
    data = models.DateTimeField(default = datetime.datetime.now())
    
    def __unicode__(self):
        return str(self.estabelecimento.nome_curto) + " - " + str(self.item.nome)
    
    def field_list(self):
        return [(u'estabelecimento', self.estabelecimento),
                (u'item', self.item),
                (u'disponibilidade', self.disponibilidade),
                (u'preco', self.preco),
                (u'desconto', self.desconto)]

class FormasDePagamento(models.Model):
    forma_de_pagamento = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.forma_de_pagamento
    
    def field_list(self):
        return [(u"forma_de_pagamento"), self.forma_de_pagamento]        