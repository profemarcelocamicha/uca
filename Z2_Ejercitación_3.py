#  Solicitar por teclado y guardar en listas lo siguiente:
#    5 nombres,
#    5 frutas y
#    5 colores.
# recorrer la estructura de nombres e imprimir un mensaje con el siguiente formato de ejemplo:
# "Pedro suele comer durazno y su color favorito es celeste"
# (Utilizando la funcion random.choice() elegir la fruta y el color para cada nombre) 
# Informar el nombre o los nombres más largos

import random

nombres=[]
frutas=[]
colores=[]
nombres


for i in range (5):
    nombre=input("ingrese un nombre ")
    nombres.append(nombre)
for i in range (5):
    fruta=input("ingrese una fruta ")
    frutas.append(fruta)
for i in range (5):
    color=input("ingrese un color ")
    colores.append(color)

for i in range (5):
    print (nombres[i], " suele comer", random.choice(frutas), "y su color favorito es", random.choice(colores))






# Sin utilizar librerías externas escribir un programa que genere 20 valores para la siguiente función, 
# considerando que el primer valor de variable x debe ser -5, 
# y debe tener incremento de a 0.5.
# Mostrar en pantalla cada valor de x con su correspondiente valor de f(x) generado
# f(x)= x^2 + 1

lista_x = []
lista_y = []
x = float(-5)
y = float(0)

for i in range (20):
    y = x**2 + 1
    lista_x.append(x)
    lista_y.append(y)
    x = x + 0.5

for i in range (20):
    print(i+1, ") x =", lista_x[i], " ->  y =", lista_y[i])



