# VISUAL STUDIO CODE
# https://code.visualstudio.com/


# 1) Describa los resultados que obtienen los siguientes algoritmos:


# i.
#        X ← 14
#        Y ← 12
#        Z ← X + Y
#        Imprimir X, Y
#        Imprimir Z

x=14
y=12
z=x+y

print("Ejercicio 1.i")
print (x,y)
print (z)



# ii.
#        P ← 8
#        Y ← P * 2
#        Imprimir P
#        Imprimir Y

p=8
y=p*2
print("Ejercicio 1.ii")
print (p)
print (y)



# 2) ¿ Cuáles serían las instrucciones para calcular las siguientes expresiones matemáticas? 
# (en dos versiones, la primera realizando una operación elemental por instrucción,
#  y otra, realizando todas las operaciones en una misma instrucción)



# i.            x
#          z=  -----
#               y + w 

x=10
y=2
w=3

# Una operación elemental por instrucción

oper1 = y + w       # Paso 1: sumar y + w
z =  x // oper1     # Paso 2: división entera de x entre el resultado anterior
print("Ejercicio 2.i")
print(z)

# Todas las operaciones en una sola instrucción
z = x // (y + w)
print(z)



# ii.       
#                y + w
#          z= k -----
#                x

y=20.5
w=10
x=5
k=2

# Una operación elemental por instrucción
oper1 = y + w
oper2 = oper1 // x
z= k*oper2
print("Ejercicio 2.ii")
print(z)
# Todas las operaciones en una sola instrucción
z = k*((y+w) // x)
print(z)



# iii.        
#                b
#          z= a -----
#                c

a=100
b=12
c=6

# Una operación elemental por instrucción
oper1 = b // c
z= a*oper1
print("Ejercicio 2.iii")
print(z)
# Todas las operaciones en una sola instrucción
z = a * b // c
print(z)



# iv.
#                a
#          z=  ----
#                bc

a=100
b=5
c=2

# Una operación elemental por instrucción
oper1 = b * c
z= a // oper1
print("Ejercicio 2.iv")
print(z)
# Todas las operaciones en una sola instrucción
z = a // (b * c)
print(z)



# v.
#                a
#          z=  ---- c
#                b

a=100
b=5
c=2

# Una operación elemental por instrucción
oper1 = a // b
z= oper1 * c
print("Ejercicio 2.v")
print(z)
# Todas las operaciones en una sola instrucción
z = (a // b) * c
print(z)



# 3) Escribir un programa que calcule el cuadrado de 144
numero = 144
cuadrado = numero ** 2
print("Ejercicio 3.i")
print("El cuadrado de", numero, "es", cuadrado)



# 4) Escribir un programa que calcule el cuadrado de un número que se ingresa.
# Solicita un número al usuario
print("Ejercicio 4")
numDecimal = float(input("Ingresá un número: "))
# Calcula el cuadrado del número
cuadrado2 = numDecimal ** 2
# Muestra el resultado
print("El cuadrado de", numDecimal, "es", cuadrado2)


# 5) Calcular el perímetro y la superficie de un cuadrado cuyo lado se ingresa.
# Solicita al usuario el valor del lado
print("Ejercicio 5")
lado = float(input("Ingresá el valor del lado del cuadrado: "))

# Calcula el perímetro y la superficie
perimetro = 4 * lado
superficie = lado ** 2
# Muestra los resultados
print("Perímetro del cuadrado:", perimetro)
print("Superficie del cuadrado:", superficie)


# 6) Realizar un programa que pida tres números y calcule su promedio.
# Solicita tres números al usuario
print("Ejercicio 6")
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))
num3 = float(input("Ingresá el tercer número: "))

# Calcula el promedio
promedio = (num1 + num2 + num3) / 3
# Muestra el resultado
print("El promedio es:", promedio)



# 7) Calcular el perímetro y la superficie de un círculo a partir del radio que se le solicita al operador.
print("Ejercicio 7")
import math  # Importamos la biblioteca math para usar pi

print(math.pi)

print(round(math.pi, 3))

# Solicita el radio al usuario
radio = float(input("Ingresá el radio del círculo: "))
# Calcula perímetro y superficie
# perimetro = 2 * math.pi * radio
perimetro = 2 * 3.1416 * radio
# superficie = math.pi * radio ** 2
superficie = 3.1416 * radio ** 2
# Muestra los resultados
print("Perímetro del círculo:", perimetro)
print("Superficie del círculo:", superficie)


# 8) Diseñar un algoritmo que transforme una temperatura en grados Celsius a grados Fahrenheit.
# F=(9/5)C+32
print("Ejercicio 8")
# Inicio
#     Leer temperatura en grados Celsius (C)
#     Calcular F = (9 / 5) * C + 32
#     Mostrar el resultado en grados Fahrenheit (F)
# Fin

# Solicita al usuario la temperatura en grados Celsius
celsius = float(input("Ingresá la temperatura en grados Celsius: "))
# Aplica la fórmula para convertir a Fahrenheit
fahrenheit = (9 / 5) * celsius + 32
# Muestra el resultado
print("La temperatura en grados Fahrenheit es:", fahrenheit)


# 9) Diseñar un algoritmo que transforme una temperatura en grados Fahrenheit a grados Celsius.
print("Ejercicio 9")
# Inicio
#     Leer temperatura en grados Fahrenheit (F)
#     Calcular C = (5 / 9) * (F - 32)
#     Mostrar el resultado en grados Celsius (C)
# Fin

# Solicita al usuario la temperatura en grados Fahrenheit
fahrenheit = float(input("Ingresá la temperatura en grados Fahrenheit: "))
# Aplica la fórmula para convertir a Celsius
celsius = (5 / 9) * (fahrenheit - 32)
# Muestra el resultado
print("La temperatura en grados Celsius es:", celsius)



# 10) Se desea un algoritmo que convierta una medida en metros a pies y pulgadas.
# (1 metro = 39,97 pulgadas, 1 pie = 12 pulgadas)
print("Ejercicio 10")

# Inicio
#     Leer una medida en metros (m)
#     Calcular pulgadas = m * 39.97
#     Calcular pie = 39.97/12
#     Calcular pies = m * 3.33
#     Mostrar pies y pulgadas
# Fin

# Solicita al usuario la medida en metros
metros = float(input("Ingresá una medida en metros: "))
# Conversión
pies = metros * 3.33
pulgadas = metros * 39.97
# Muestra los resultados
print("Equivale a:", round(pies, 2), "pies")
print("Equivale a:", round(pulgadas, 2), "pulgadas")

# print("Equivale a:", pies, "pies")
# print("Equivale a:", pulgadas, "pulgadas")



# 11) Solicitar un numero en segundos, e indicar cuantas horas, minutos, y segundos representa.

print("Ejercicio 11")
# Solicita al usuario una cantidad de segundos
total_segundos = int(input("Ingresá una cantidad de segundos: "))
# Cálculo de horas, minutos y segundos
horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60
# Muestra el resultado
print("Equivale a:")
print(horas, "horas")
print(minutos, "minutos")
print(segundos, "segundos")



# 12) Una persona esta planeando realizar un viaje desde Buenos Aires hasta Ushuaia y desea saber 
# la cantidad de veces que tendrá que llenar el tanque. 
# Suponiendo que se conoce la distancia, el consumo del auto, y la capacidad del tanque, 
# se desea saber la cantidad de veces que deberá llenar el tanque.

# Ejemplo 
# Distancia = 1000 km
# Consumo = 10 km/litro
# Capacidad del tanque = 50 litros
# 1000 / (10 * 50) = 2 cargas


print("Ejercicio 12")
import math
# Solicita los datos al usuario
distancia = float(input("Ingresá la distancia total en km: "))
consumo = float(input("Ingresá el consumo del auto (km por litro): "))
capacidad = float(input("Ingresá la capacidad del tanque en litros: "))
# Calcula la autonomía del vehículo
autonomia = consumo * capacidad
# Calcula la cantidad de recargas necesarias (redondeando hacia arriba)
# recargas_redondeado = math.ceil(distancia / autonomia)
recargas_decimales = (distancia / autonomia)
# recargas_parte_entera = (distancia // autonomia)
# Muestra el resultado
print("(Calculo redondeado) - Deberá llenar el tanque", recargas_redondeado, "veces durante el viaje.")
print("(Calculo división con decimales) - Deberá llenar el tanque", recargas_decimales, "veces durante el viaje.")
print("(Calculo división con solo la parte entera) - Deberá llenar el tanque", recargas_parte_entera, "veces durante el viaje.")



# 13) Escriba un programa que solicita un número, un divisor del número y devuelva el cociente entero y su resto. El resto se obtiene con el operador módulo “%”, es decir que 5 % 2 da como resultado 1.
print("Ejercicio 13")
# Solicita al usuario el número y su divisor
numero = int(input("Ingresá un número: "))
divisor = int(input("Ingresá un divisor: "))
# Calcula el cociente entero y el resto
cociente = numero // divisor
resto = numero % divisor
# Muestra los resultados
print("Cociente entero:", cociente)
print("Resto:", resto)



# 14) Solicitar por teclado el valor de la variable x1, a continuación solicitar el valor de la variable x2. Luego intercambiarlos, es decir colocar el valor de X2 en X1 e viceversa. Finalmente mostrar los valores de x1 y x2.
print("Ejercicio 14")
# Solicita los valores
x1 = input("Ingresá el valor de x1: ")
x2 = input("Ingresá el valor de x2: ")
# Intercambia los valores usando una variable auxiliar
aux = x1
x1 = x2
x2 = aux
# Muestra el resultado
print("Después del intercambio:")
print("x1 =", x1)
print("x2 =", x2)



# 15) Describa un algoritmo que permita preparar un Sándwich.
# Inicio
#     1. Ir a la cocina
#     2. Tomar dos rebanadas de pan
#     3. Colocar una rebanada de pan sobre un plato
#     4. Untar mayonesa sobre esa rebanada
#     5. Colocar una feta de jamón
#     6. Colocar una feta de queso
#     7. Tapar con la segunda rebanada de pan
#     8. Servir el sándwich
# Fin
