# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
import simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User
from PGuideServer.nucleo.models import Usuario, Item, Marca, Categoria,\
    UnidadeDeMedida, HistoricoConsultas, ItemLista
from django.core import serializers

def login(request):
    username = request.GET['username']
    password = request.GET['password']
    
    try:
        user = authenticate(username = username, password = password)
    except:
        pass
        
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
    
    user = User()
    user.username = email
    user.first_name = nome
    user.last_name = sobrenome
    user.email = email
    user.password = senha
    user.save()
    try:
        user = User.objects.get(username = email)
    except Exception as error:
        dictionary["sucesso_cadastro"] = False
        dictionary["erro"] = error
    
    usuario = Usuario()
    usuario.user = user
    usuario.cidade = cidade
    usuario.estado = estado
    try:
        usuario.save()
    except Exception as error:
        dictionary["sucesso_cadastro"] =  False
        dictionary["erro"] = error
        
    return HttpResponse(
        simplejson.dumps(dictionary), 
        content_type = 'application/json; charset=utf8'
    )

def getProfile(request):
    username = request.GET['username']
    
    try:
        user = User.objects.get(username = username)
        usuario = Usuario.objects.get(user = user)
    except:
        pass
        
    if user is not None:
        return HttpResponse(
            simplejson.dumps({"username": user.username,
                              "email": user.email,
                              "nome": user.first_name,
                              "sobrenome": user.last_name,
                              "cidade": usuario.cidade,
                              "estado": usuario.estado}), 
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
