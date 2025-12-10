# Ejercicio 1

# Realizar un programa que cumpla con las siguientes especificaciones:

# *** Solicitar por separado, el ingreso por teclado de la siguiente información:
# calle, numero y ciudad
# El numero se debe ingresar como entero.
# *** Si en numero es cero, se debe informar el error y volver a solicitarlo.

# *** Generar un identificador con el formato:
# [calle]-[numero]-[ciudad]
# donde:
#     para la calle se debe guardar solo las primeras 4 posiciones.
#     para el numero se debe convertir a string y se debe asegurar que la cantidad de caracteres sea siempre 8, 
#     (si es menos se debe completar con ceros). 
#     para la ciudad no puede superar los 6 caracteres. 
#       Ejemplo:
#       Ingrese calle: Rivadavia    => Riva
#       Ingrese numero: 1545        => 15450000
#       Ingrese ciudad_ Castelar    => Castel
# *** Este identificar debe asignarse a una variable
# *** Mostrar el identificador generado en pantalla

# Solicitar la calle
calle = input("Ingrese la calle: ")

# Solicitar el número, validando que no sea cero
while True:
    try:
        numero = int(input("Ingrese el número (entero distinto de cero): "))
        if numero == 0:
            print("Error: el número no puede ser cero.")
        else:
            break
    except ValueError:
        print("Error: debe ingresar un número entero.")

# Solicitar la ciudad
ciudad = input("Ingrese la ciudad: ")

# Procesar cada parte para generar el identificador

# Tomar solo las primeras 4 letras de la calle
calle_corta = calle[:4]

# Convertir el número a string
numero_str = str(numero)

# Calcular cuántos ceros faltan
cantidad_ceros = 8 - len(numero_str)  #1986

# Agregar ceros manualmente al principio con iteración
ceros = ""

for i in range(cantidad_ceros):
    ceros = ceros + "0"
    print(i) 
print (ceros) #0000

numero_formateado = numero_str + ceros #00001986

# int 1+1=2
# str 1+1=11

# Tomar como máximo los primeros 6 caracteres de la ciudad
ciudad_corta = ciudad[:6]

# Generar el identificador
identificador = calle_corta + "-" + numero_formateado + "-" + ciudad_corta

# Mostrar el identificador
print("Identificador generado:", identificador)





"""
# Ejercicio 2
# Desarrolle un programa que calcule el ahorro anual según estas reglas:
# Solicitar:

# T=total de compras en el año: (decimales)
# E=Edad: (entero)
# Z=Zona:
# B=Banco:

# * Si E >= 65: se aplica un beneficio del 10%
# * Si Z es "Norte": No se aplica beneficio, si es de cualquier otra zona se aplica un 1%
# * Si B es "Santander": se aplica un beneficio del 2%
# * Si B es "Frances": se aplica un beneficio del 3%
# * Si B es "Nacion": se aplica un beneficio del 5% (con un tope de 100.000 pesos)

# Si el total ahorrado supera los 200.000 se le dará un beneficio fijo adicional de 50.000

# Se debera informar:
# Total de compras en el año: 
# Ahorro por edad:
# Ahorro por zona:
# Ahorro por banco:
# Bono adicional:
# Total de beneficios obtenidos:

# Solicitar datos al usuario
T = float(input("Ingrese el total de compras en el año: "))
E = int(input("Ingrese la edad: "))
Z = input("Ingrese la zona (Norte, Sur, Este, Oeste): ").strip().capitalize()
B = input("Ingrese el banco (Santander, Frances, Nacion, Otro): ").strip().capitalize()


# Inicializar ahorros
ahorro_edad = 0.0
ahorro_zona = 0.0
ahorro_banco = 0.0
bono_adicional = 0.0

# Calcular beneficio por edad
if E >= 65:
    ahorro_edad = T * 0.10

# Calcular beneficio por zona
if Z != "Norte":
    ahorro_zona = T * 0.01

# Calcular beneficio por banco
if B == "Santander":
    ahorro_banco = T * 0.02
elif B == "Frances":
    ahorro_banco = T * 0.03
elif B == "Nacion":
    ahorro_banco = min(T * 0.05, 100000)

# Calcular total de beneficios
total_ahorro = ahorro_edad + ahorro_zona + ahorro_banco

# Verificar si corresponde bono adicional
if total_ahorro > 200000:
    bono_adicional = 50000

total_beneficio = total_ahorro + bono_adicional

# Mostrar resultados
print("\n--- Detalle de beneficios ---")
print(f"Total de compras en el año: ${T:,.2f}")
print(f"Ahorro por edad: ${ahorro_edad:,.2f}")
print(f"Ahorro por zona: ${ahorro_zona:,.2f}")
print(f"Ahorro por banco: ${ahorro_banco:,.2f}")

if bono_adicional > 0:
    print("Bono adicional: $50,000.00")
else:
    print("No corresponde bono adicional.")

print(f"Total de beneficios obtenidos: ${total_beneficio:,.2f}")
"""







"""
# Ejercicio 3
# Escribir un programa que realice las siguientes tareas:
# * Solicitar al usuario el ingreso de números hasta que el número ingresado sea cero
# * Se deberán ir sumando en variables independientes, los siguientes numeros:
#     1, #unos
#     menores que -6, #men6
#     mayores que 6 #may6
# * para los numeros que cumplen las condiciones se deben usar variables como contadores
# * para los numeros que no se informan se deben guardar en una lista

# Informar:
# Cantidad de numeros 1:
# Cantidad de numeros < -6:
# Cantidad de numeros > 6:
# Para los numeros que no cumplen con las condiciones anteriores:
#   Cantidad de numeros
#   Suma 
#   Promedio
#   Maximo
#   Minimo    

# Inicialización de contadores y lista
unos = 0
men6 = 0
may6 = 0
otros = []

while True:
    try:
        numero = int(input("Ingrese un número (0 para finalizar): "))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        continue

    if numero == 0:
        break  # Finaliza el ingreso
    elif numero == 1:
        unos += 1
    elif numero < -6:
        men6 += 1
    elif numero > 6:
        may6 += 1
    else:
        otros.append(numero)

# Mostrar resultados
print("\nResultados:")
print("Cantidad de números 1:", unos)
print("Cantidad de números < -6:", men6)
print("Cantidad de números > 6:", may6)
print("Cantidad de números que no cumplen con las condiciones anteriores:", len(otros))
print("Suma de los números que no cumplen con las condiciones anteriores:", sum(otros))
"""
    


# Ejercicio 4
# Crear una función que reciba un número por parámetro y determine si el mismo es múltiplo de 3 y mayor a 10.
# La función debe devolver verdadero si el número recibido es múltiplo de 3 y mayor a 10, o falso en caso contrario.
# Escribir un programa que solicite el ingreso de números positivos hasta recibir un cero.
# Si el numero ingresado es distinto de cero, informarlo y solicitarlo nuevamente.
# Utilizando la función creada, evaluar si el número ingresado es múltiplo de 3 y mayor a 10.
# Si lo es, guardar el número en una lista, si no lo es guardar el número en otra lista.
# Luego de finalizar la carga de números mostrar:
#     todos los números múltiplos de 3 y mayores a 10 guardados en la lista
#     y la cantidad  
#     todos los números restantes guardados en la otra lista
#     y la cantidad

# Función que verifica si un número es múltiplo de 3 y mayor a 10
def es_multiplo_de_3_y_mayor_10(numero):
    if numero % 3 == 0 and numero > 10:
        return True
    else:
        return False
#   return numero % 3 == 0 and numero > 10

# Listas para guardar los números según la condición
lista_multiplos = []
lista_otros = []

# Solicita números hasta que se ingrese un 0
while True:
    numero = int(input("Ingrese un número positivo (0 para terminar): "))
    
    if numero == 0:
        break

    if numero < 0:
        print("El número debe ser positivo. Intente nuevamente.")
        continue

    # Evaluamos el número con la función y lo guardamos en la lista correspondiente
    if es_multiplo_de_3_y_mayor_10(numero):
        lista_multiplos.append(numero)
    else:
        lista_otros.append(numero)

# Mostrar resultados
print("\nNúmeros múltiplos de 3 y mayores a 10:")
print(lista_multiplos)
print("Cantidad:", len(lista_multiplos))

print("\nOtros números:")
print(lista_otros)
print("Cantidad:", len(lista_otros))



"""
# Ejercicio 5
# Sin utilizar librerías externas escribir un programa que genere 10 valores para la siguiente función, 
# considerando que el primer valor de variable x debe ser -5, y debe tener incremento de a 1.
# Mostrar en pantalla cada valor de x con su correspondiente valor de f(x) generado
# $f(x)= x**3 + 1

# Generar 10 valores de x comenzando desde -5
x = -5
contador = 0

while contador < 10:
    fx = x**3 + 1
    print(f"x = {x}, f(x) = {fx}")
    x += 1
    contador += 1
"""


"""

# Ejercicio 6
# Repetir el punto anterior utilizando Numpy
import numpy as np

# Generar los valores de x con numpy
muestras = 10
desde = -5
incremento = 1

hasta = desde + (muestras - 1) * incremento
#hasta = -5   +  ( 10     -1) * 1
#hasta = -5   +  ( 9 )
#hasta =  4

x_np = np.linspace(desde, hasta,  muestras) 
print(x_np)

# Calcular f(x) con numpy
y_np = x_np**3 + 1

# Mostrar los resultados
for a in range(muestras):
    print("x =", x_np[a], "→ f(x) =", y_np[a])

    

# Ejercicio 7
# Graficar la funcion usando los datos del ejercicio anterior

import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plt.plot(x_np, y_np, color='blue', label='f(x)')
plt.title("Gráfico de f(x) = x^3 + 1")
plt.xlabel("x")
plt.ylabel("f(x)")
#plt.grid(True)
plt.legend()
plt.show()
"""