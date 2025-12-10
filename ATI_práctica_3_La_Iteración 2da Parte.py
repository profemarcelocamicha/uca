# import os
# os.system('cls')
# lineas=80


# # 12) Solicitar las notas del parcial de computación I e indicar cuantos tienen la posibilidad de promocionan la materia.
# print("12) Solicitar las notas del parcial de computación I e indicar cuantos tienen la posibilidad de promocionan la materia.")
# print("-"*lineas)

# total_alumnos = 0
# promocionan = 0
# print("Ingrese las notas de los alumnos (0 para finalizar):")
# while True:
#     nota = int(input("Nota: "))
#     if nota == 0:
#         break
#     if nota < 1 or nota > 10:
#         print("Nota inválida. Ingrese un valor entre 1 y 10.")
#         continue
#     # total_alumnos += 1
#     total_alumnos = total_alumnos + 1

#     if nota >= 7:
#         # promocionan += 1
#         promocionan = promocionan + 1

# print(f"\nTotal de alumnos: {total_alumnos}")
# print(f"Cantidad que pueden promocionar: {promocionan}")





# # 13) Calcular el valor de la serie 1 + x + x 2 / 2! + ...+ x n / n!. Para una cantidad predeterminada de términos que se solicitan por teclado.
# print("13) Calcular el valor de la serie 1 + x + x 2 / 2! + ...+ x n / n!. Para una cantidad predeterminada de términos que se solicitan por teclado.")
# print("-"*lineas)

# # 0!=1 (por definición)
# # 1!=1
# # 2!=2×1=2
# # 3!=3×2×1=6
# # 4!=4×3×2×1=24
# # 5!=5×4×3×2×1=120

# # Usando la librería math

# import math
# x = float(input("Ingrese el valor de x: "))
# n = int(input("Ingrese la cantidad de términos (n): "))
# suma = float(0)
# for i in range(n + 1):
#     termino = (x ** i) / math.factorial(i)
#     suma += termino
# print(f"El valor de la serie usando la librería match para calcular el factorial es: {suma}")

# Usando una iteración for

# def factorial(n):
#     resultado = 1
#     for i in range(1, n + 1):
#         resultado *= i
#     return resultado

# suma = 0
# for i in range(n + 1):
#     termino = (x ** i) / factorial(i)
#     suma += termino
# print(f"El valor de la serie usando la iteración para calcular el factorial es: {suma}")









# # 14) Ídem anterior, pero hasta que valor absoluto del último término calculado sea inferior a un valor que se solicita por teclado.
# print("14) Ídem anterior, pero hasta que valor absoluto del último término calculado sea inferior a un valor que se solicita por teclado.")
# print("-"*lineas)

# import math
# x = int(input("Ingrese el valor de x: "))
# valor = float(input("Ingrese el valor mínimo: "))

# suma = 0
# i = 0
# t1 = 1  # empezamos con el primer término (t1) (x^0 / 0! = 1)

# while abs(t1) >= valor:
#     t1 = (x ** i) / math.factorial(i)
#     suma += t1
#     i += 1

# print(f"El valor de la serie es: {suma}")
# print(f"Se calcularon {i} términos.")







# # 15) Calcular el enésimo término de la serie de Fibonacci definida por: A1 = 1; A2 = 2; A3 = A1 + A2; A n = A n-1 + A n-2
# # Ejemplo para el numero 5
# # 2 3 (3)
# # 3 5 (4)
# # 5 8 (5)

# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2

#     a1, a2 = 1, 2
#     for _ in range(3, n + 1):
#         print(n, a1, a2)
#         a1, a2 = a2, a1 + a2
#         print(n, a1, a2)        
#     return a2

# n = int(input("Ingresá el valor de n: "))
# print(f"El término número {n} de la serie es: {fibonacci(n)}")







# # 16) Escribir un programa que solicite al operador un número entero e indique la cantidad de cifras que tiene.


# numero = int(input("Ingrese un número entero: "))
# # Por las dudas le sacamos el signo, por si es negativo
# numero_absoluto = abs(numero)
# # Lo pasamos de int a String
# numero_string = str(numero_absoluto)
# # Calculamos la cantidad de cifras con la funcion len()
# cantidad_cifras = len(numero_string)
# # Todo lo anterior se puede escribir en una sola linea:
# # cantidad_cifras = len(str(abs(numero)))
# print(f"El número tiene {cantidad_cifras} cifra(s).")






# # 17) Un monto (M) se coloca en una entidad bancaria a plazo fijo por un período de 90 días 
# # a una tasa de interés anual (T), renovándose al vencimiento por otro período igual en similares condiciones. 
# # ¿Al cabo de cuantos períodos se duplicará el monto original (M)?

# m = float(input("ingrese un monto:"))
# d = int(input("ingrese los dias a PF:")) # Podría poner 90 días directamente, sin preguntarlo
# t = float(input("ingrese la tasa anual:"))

# m_inicial=m
# m_dup= m*2
# contador=0

# while m_dup > m:
#     interes= (m*t*d)/(365*100)
#     m = m + interes
#     # print(m)
#     contador+= 1   
#     print(contador) 
#     print(f"monto inicial: {m_inicial}, monto acumulado en período {contador}: {m} interes sobre monto acumulado {interes}")
#     # print("monto inicial:", m_inicial, "monto acumulado en período", contador, ":", m,  "interes sobre monto acumulado", interes)    

# print(f"Cada {contador} periodos se duplicará el monto")






# Ejercicio 17 usando una función para calcular el interés
# m = float(input("ingrese un monto:"))
# d = int(input("ingrese los dias a PF:"))
# t = float(input("ingrese la tasa anual:"))
# m_inicial=m
# m_dup= m*2
# contador=0
# def calcular_interes(m, t, d):
#     return (m*t*d)/(365*100)
# while m_dup > m:
#     interes= calcular_interes(m,d,t)
#     m = m + interes
#     contador+= 1    
#     print(f"monto inicial: {m_inicial}, monto acumulado en período {contador}: {m} interes sobre monto acumulado {interes}")
# print(f"Cada {contador} periodos se duplicará el monto")





# # 18) En una carrera de natación en la que han participado 6 nadadores, 
# # se ha identificado cada uno de ellos por el número de la calle en la cual han largado (1 a 6). 
# # Solicitar para cada uno los tiempos medidos en cantidad de segundos, e indicar el número del ganador.

# mejor_tiempo = None
# ganador = None

# for calle in range(1, 7):   # calles 1 a 6
#     tiempo = float(input(f"Ingrese el tiempo del nadador en la calle {calle}: "))

#     if mejor_tiempo is None or tiempo < mejor_tiempo:
#         mejor_tiempo = tiempo
#         ganador = calle

# print(f"El ganador es el nadador de la calle {ganador} con un tiempo de {mejor_tiempo} segundos.")






# Ejercicio 18 con manejo de empates y sin usar listas

# mejor_tiempo = None
# ganadores = ""          # acá guardaremos las calles empatadas como texto
# cantidad_ganadores = 0

# for calle in range(1, 7):
#     tiempo = float(input("Ingrese el tiempo del nadador en la calle " + str(calle) + ": "))

#     if mejor_tiempo is None or tiempo < mejor_tiempo:
#         mejor_tiempo = tiempo
#         ganadores = str(calle)     # reemplazo: este es el nuevo único ganador
#         cantidad_ganadores = 1

#     elif tiempo == mejor_tiempo:
#         ganadores = ganadores + ", " + str(calle)
#         cantidad_ganadores += 1

# # Mostrar resultado
# if cantidad_ganadores == 1:
#     print("El ganador es el nadador de la calle " + ganadores +
#           " con " + str(mejor_tiempo) + " segundos.")
# else:
#     print("Hay un empate entre las calles: " + ganadores +
#           " con " + str(mejor_tiempo) + " segundos.")






# Ejercicio 18 usando listas 

# tiempos = []
# ganadores = []

# for calle in range(1, 7):
#     tiempo = float(input(f"Ingrese el tiempo (en segundos) del nadador de la calle {calle}: "))
#     tiempos.append(tiempo)
# mejor_tiempo = min(tiempos)
# for i in range(len(tiempos)):
#     if tiempos[i] == mejor_tiempo:
#         ganadores.append(i + 1)  
# if len(ganadores) == 1:
#     print(f"\nGanó el nadador de la calle {ganadores[0]}, con un tiempo de {mejor_tiempo:.2f} seg")
# else:
#     print(f"\nGanaron los nadadores de las calles {ganadores}")
#     print(f"Con un tiempo de {mejor_tiempo:.2f} seg")

