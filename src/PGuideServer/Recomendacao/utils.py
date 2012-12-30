# -*- coding:utf-8 -*-
from math import pi, sin, cos, sqrt, atan2
from django.db import models
from PGuideServer.nucleo.models import ItemEstabelecimento, Estabelecimento

class Valores:
    minimo = None
    maximo = None
    relevancia = None #  peso
    
    def __init__(self, minimo, maximo, relevancia):
        self.minimo = minimo
        self.maximo = maximo
        self.relevancia = relevancia
    
    def diferenca(self):
        return self.maximo - self.minimo

class IndicePreco(Valores):
    pass

class IndiceReputacao(Valores):
    pass

class IndiceProximidade(Valores):
    pass

class AvaliacaoItem(models.Model):
    item = models.ForeignKey(ItemEstabelecimento)
    pontuacao = models.FloatField()
    
class AvaliacaoEstabelecimento(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento)
    preco_total = models.FloatField()
    pontuacao = models.FloatField()
    
class Localizacao:
    latitude = None
    longitude = None
    
    def __init__(self, lat, long):
        self.latitude = lat
        self.longitude = long
        
    def __unicode__(self):
        return '[',self.latitude, ',', self.longitude,']'
    

# funcoes

def calcularDistancia(localizacao_usuario, localizacao_estabelecimento):
   
    ''' Haversine formula
        give coordinates as (lat_decimal,lon_decimal) tuples
    '''
    earthradius = 6371.0

    lat1 = localizacao_usuario.latitude
    lon1 = localizacao_usuario.longitude
    lat2 = localizacao_estabelecimento.latitude
    lon2 = localizacao_estabelecimento.longitude

    # convert to radians
    lon1 = lon1 * pi / 180.0
    lon2 = lon2 * pi / 180.0
    lat1 = lat1 * pi / 180.0
    lat2 = lat2 * pi / 180.0

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (
        (sin(dlat/2))**2 +
        cos(lat1) * cos(lat2) * (sin(dlon/2.0))**2
    )
    c = 2.0 * atan2(sqrt(a), sqrt(1.0-a))
    km = earthradius * c
    return float("%.2f"%(km))