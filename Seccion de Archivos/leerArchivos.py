#!c:/Python/python.exe
# -*- coding: utf-8 -*-  

archivo = open('archivo1.txt','r')

#print(archivo.readlines())
#split separa cadenas de texto segun valor pasado

#for l in archivo.read().split('\n'):
   # print(l)

lista = archivo.read().split('\n')

for n in lista:
    
    print(n)