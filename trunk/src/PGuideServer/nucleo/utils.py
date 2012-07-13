# coding:utf-8

def toIntegerList(string):
    lista = []
    integer = ""
    for i in range(len(string)):
        if string[i] is not "[" and \
           string[i] is not "," and \
           string[i] is not "]":
            integer += string[i]
        else:
            if integer != "":
                lista.append(int(integer))
                integer = ""
    return lista