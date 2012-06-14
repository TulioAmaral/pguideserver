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
    
    # single
    (r'^getProfile/', "PGuideServer.Webservice.views.getProfile"),
    (r'^getMarca/', "PGuideServer.Webservice.views.getMarca"),
    
    # search
    (r'^pesquisar/', "PGuideServer.Webservice.views.pesquisar"),
    
    # all
    (r'^getUnidadesDeMedida/', "PGuideServer.Webservice.views.getUnidadesDeMedida"),
    (r'^getCategorias/', "PGuideServer.Webservice.views.getCategorias"),

)
