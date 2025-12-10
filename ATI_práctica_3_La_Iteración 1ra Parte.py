# import os
# os.system('cls')
# lineas=80


# 1) Realizar un programa que muestre la tabla del 2.
# print("1) Realizar un programa que muestre la tabla del 2.")
# print("-"*lineas)

# for i in range(1, 11):
#     resultado = 2 * i
#     print("2 *", i, "=", resultado)    
#     # print(f"2 x {i} = {resultado}") #También lo podrían escribir de esta manera
# print("fin")

    




# # 2) Realizar un programa que pida al operador un número entero y muestre la tabla de ese número.
# print("2) Realizar un programa que pida al operador un número entero y muestre la tabla de ese número.")
# print("-"*lineas)

# numero = int(input("Ingrese un número entero: "))
# # print(f"Tabla del {numero}:")
# print("Tabla del ", numero, ":")

# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} * {i} = {resultado}")
#     print(numero, " * ", i, " = ", resultado)    
     

    


    

# # 3) Sumar todos los números pares comprendidos entre 2 y 100.
# print("3) Sumar todos los números pares comprendidos entre 2 y 100.")
# print("-"*lineas)

# # Usando comparación por el resto
# suma = 0
# resultado = 0

# for numero in range(2, 101):  # Recorre del 2 al 100 inclusive
#     if numero % 2 == 0:  # Si el resto al dividir por 2 es 0, es par
#         # suma += numero
#         suma = suma + numero

# print("La suma de los números pares del 2 al 100 es:", suma, "\n")






# # # Ejemplo de for, usando parámetro de STEP.
# for numero in range(2, 101, 2):  # Va de 2 a 100, el tercer parámetro es el step, es decir, va de dos en dos (pares)
#     print(numero)
# # Usando parámetro del for
# suma = 0
# for numero in range(2, 101, 2):  # Va de 2 a 100, de dos en dos (pares)
#     # suma += numero
#     suma = suma + numero
# print("Usando parámetro del for")            
# print("La suma de los números pares del 2 al 100 es:", suma, "\n")





# # 4) Realizar un programa que sume los números impares menores a K. Solicitar el valor de K por el teclado.


# # Usando comparación por el resto
# K = int(input("Ingrese un número entero: "))

# suma = 0
# for numero in range(1, K):  # Recorre desde 1 hasta K-1
#     if numero % 2 != 0:     # Si el número es impar
#         # print(numero) Se puede descomentar esta linea para ver los números que se suman
#         #suma += numero
#         suma = suma + numero
# print(f"La suma de los números impares menores a {K} es: {suma}")
#print("La suma de los números impares menores a ", K, " es: ", suma)
      


# # Ejemplo de for, usando parámetro de STEP.
# suma = 0
# for numero in range(1, K, 2):  # Empieza en 1 y salta de 2 en 2 (solo impares)
#     # print(numero) Se puede descomentar esta linea para ver los números que se suman
#     # suma += numero
#     suma = suma + numero
# print(f"La suma de los números impares menores a {K} es: {suma}")






# # 5) Realizar un programa que sume los primeros números naturales siempre que la suma no supere un valor T. Solicitar T por teclado.

# # Ejemplo:
# # Si el usuario pone T = 10, se suman: 1 + 2 + 3 + 4 = 10
# # (No suma el 5 porque 10 + 5 = 15. Y 15 es mayor a 10)


# T = int(input("Ingrese el valor máximo permitido para la suma: "))
# suma = 0
# n = 1
# print("Números sumados:")
# while suma + n <= T:
#     print(n)
#     #suma += n    #Es lo mismo que escribir suma = suma + n
#     suma = suma + n
#     #n += 1       #Es lo mismo que escribir n = n + 1
#     n = n + 1
# print(f"La suma total sin superar {T} es: {suma}")





# # 6) Aceptar por teclado una serie de números naturales (como final de la serie se debe reconocer el número 0 el cual no se debe considerar) e informar cual de ellos es el mayor.
# print("6) Aceptar por teclado una serie de números naturales (como final de la serie se debe reconocer el número 0 el cual no se debe considerar) e informar cual de ellos es el mayor.")
# print("-"*lineas)

# numero_mayor = None

# while True:
#     numero = int(input("Ingrese un número natural (0 para finalizar): "))
#     if numero == 0:
#         break  # Finaliza la carga
#     if numero_mayor is None or numero > numero_mayor:
#         numero_mayor = numero

# if numero_mayor is None:
#     print("No se ingresaron números.")
# else:
#     print("El mayor número ingresado fue:", numero_mayor)



# # 7) Ídem anterior pero indicando el menor.
# print("Ídem anterior pero indicando el menor.")
# print("-"*lineas)

# menor = None  # Inicialmente no hay ningún número cargado
# while True:
#     numero = int(input("Ingrese un número natural (0 para finalizar): "))
#     if numero == 0:
#         break  # Finaliza la carga
#     if menor is None or numero < menor:
#         menor = numero
#     # Si todavía no hay ningún número cargado (menor is None), asignamos el primer número ingresado como el menor.
#     # O si el número actual es más chico que el menor actual lo actualizamos.
# if menor is None:
#     print("No se ingresaron números.")
# else:
#     print("El menor número ingresado fue:", menor)







# # 8) Calcular el promedio aritmético de un conjunto de números informados por el teclado (0 indica el final).
# print("Calcular el promedio aritmético de un conjunto de números informados por el teclado (0 indica el final).")
# print("-"*lineas)

# suma = float(0)
# contador = 0

# while True:
#     num = float(input("Ingrese un número (0 para finalizar): "))
#     if num == 0:
#         break
#     suma += num
#     contador += 1
# if contador == 0:
#     print("No se ingresaron números.")
# else:
#     promedio = suma / contador
# #   print(f"El promedio de los {contador} números ingresados es: {promedio:.2f}")
#     print(f"El promedio de los {contador} números ingresados es: {promedio:}") 






# # 9) Aceptar por teclado 10 números enteros, indicar cuantos de ellos son pares y cuantos impares.
# print("9) Aceptar por teclado 10 números enteros, indicar cuantos de ellos son pares y cuantos impares.")
# print("-"*lineas)

# pares = 0
# impares = 0

# for i in range(1, 11):
#     numero = int(input(f"Ingrese el número {i}: "))
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

# print(f"Cantidad de números pares: {pares}")
# print(f"Cantidad de números impares: {impares}")





# # 10) Sumar una serie de valores que se informan por el teclado, controlando que su ingreso sea realizado en forma 
# # ascendente. Si el número indicado no cumple con esa condición se debe informar la situación y 
# # requerir nuevamente el valor. Se reconoce el final de la serie cuando se informa el valor cero.
# print("10) Sumar una serie de valores que se informan por el teclado, controlando que suingreso sea realizado en forma ascendente. Si el número indicado no cumple con esa condición se debe informar la situación y requerir nuevamente el valor. Se reconoce el final de la serie cuando se informa el valor cero.")
# print("-"*lineas)

# suma = 0
# anterior = None  # Aún no se ingresó ningún número

# while True:
#     numero = int(input("Ingrese un número (0 para salir): "))
#     if numero == 0:
#         break
#     if anterior is None or numero > anterior:
#         suma += numero
#         anterior = numero
#     else:
#         print(f"El número ingresado {numero} no es mayor que el anterior {anterior}. Intente nuevamente.")

# print("La suma de los números ingresados en forma ascendente es:", suma)







# # 11) Imprimir todos los números primos entre 1 y 100.
# print("11) Imprimir todos los números primos entre 1 y 100.")
# print("-"*lineas)
# # Un número primo es un número mayor que 1 que solo tiene dos divisores: el 1 y él mismo.
# # El 2 es el único número primo par. Todos los demás primos son impares.
# # Por ejemplo:
# # 2: sus únicos divisores son 1 y 2    entonces es primo
# # 3: divisores: 1, 3                   entonces es primo
# # 4: divisores: 1, 2, 4                entonces no es primo
# # 5: divisores: 1, 5                   entonces es primo
# # 6: divisores: 1, 2, 3, 6             entonces no es primo
# # Una buena práctica es verificar divisores hasta la raíz cuadrada

# for numero in range(2, 101):  # Empezamos en 2, porque 1 no es primo
#     es_primo = True
#     print(f"---------------- {numero} -------------------")    
#     print("int(numero ** 0.5) = ", int(numero ** 0.5), "\n"
#           "int(numero ** 0.5) + 1 = ", int(numero ** 0.5) + 1)    

#     for i in range(2, int(numero ** 0.5) + 1):  # Verifica divisores hasta la raíz cuadrada
#         if numero % i == 0:
#             print(f"{numero} / {i} tiene resto == 0")            
#             es_primo = False
#             print(numero, " No es número primo")
#             break
#         else:
#             print(f"{numero} / {i} tiene resto =! 0")                        
#     if es_primo:
#         print(numero, "----------------------------Es número primo")

