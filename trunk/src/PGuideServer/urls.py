from django.conf.urls.defaults import patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^PGuideServer/', include('PGuideServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    #####  webservice urls ####
    (r'^login/', "PGuideServer.Webservice.views.login"),
    (r'^cadastrar_usuario/', "PGuideServer.Webservice.views.cadastrar_usuario"),
    (r'^cadastrar_preferencias/', "PGuideServer.Webservice.views.cadastrar_preferencias"),
    
    # single
    (r'^getProfile/', "PGuideServer.Webservice.views.getProfile"),
    (r'^getMarca/', "PGuideServer.Webservice.views.getMarca"),
    (r'^getItemID/', "PGuideServer.Webservice.views.getItemID"),
    (r'^getItem/', "PGuideServer.Webservice.views.getItem"),
    (r'^getEstabelecimento/', "PGuideServer.Webservice.views.getEstabelecimento"),
    (r'^getPreferencias/', "PGuideServer.Webservice.views.getPreferencias"),
    
    # set
    (r'^adicionarItemNaLista/', "PGuideServer.Webservice.views.adicionarItemNaLista"),
    
    # search
    (r'^pesquisar/', "PGuideServer.Webservice.views.pesquisar"),
    (r'^getListaDeCompras/', "PGuideServer.Webservice.views.getListaDeCompras"),
    (r'^buscarRecomendacaoProduto/', "PGuideServer.Webservice.views.buscarRecomendacaoProduto"),
    
    # all
    (r'^getUnidadesDeMedida/', "PGuideServer.Webservice.views.getUnidadesDeMedida"),
    (r'^getCategorias/', "PGuideServer.Webservice.views.getCategorias"),
    (r'^getFormasDePagamento/', "PGuideServer.Webservice.views.getFormasDePagamento"),

    # edit
    (r'^alterarStatusDoItemDaLista/', "PGuideServer.Webservice.views.alterarStatusDoItemDaLista"),
    
    # delete
    (r'^limparListaDeCompras/', "PGuideServer.Webservice.views.limparListaDeCompras"),
    (r'^removerItemDaLista/', "PGuideServer.Webservice.views.removerItemDaLista"),
)
