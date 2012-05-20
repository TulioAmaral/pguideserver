from django.contrib import admin
from PGuideServer.nucleo.models import Categoria, Estabelecimento, \
                                       HistoricoConsultas, Item, ItemLista, Marca, \
                                       UnidadeDeMedida, Usuario

admin.site.register(Categoria)
admin.site.register(Estabelecimento)
admin.site.register(HistoricoConsultas)
admin.site.register(Item)
admin.site.register(ItemLista)
admin.site.register(Marca)
admin.site.register(UnidadeDeMedida)
admin.site.register(Usuario)