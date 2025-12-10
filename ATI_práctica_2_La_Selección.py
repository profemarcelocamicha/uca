
# Ctrol + K + C para cometarios temporales
# Ctrol + K + U para descomentar

# lineas=80




# print("1) Solicitar al operador dos números e indicar si son iguales o distintos.")
# print("-"*lineas)
# print("Ejercicio 1 - Opción números enteros")

# numero1 = int(input("Ingrese un número entero: "))
# numero2 = int(input("Ingrese otro número entero: "))
# if numero1 == numero2:
#     print("Los números son iguales")

# else:
#     print("Los números son distintos")
# # Verificamos que el número es de tipo entero, si no pongo int antes del input se toma como string
# print(type(numero1), type(numero2))



# print("-"*lineas)
# print("Ejercicio 1 - Opción números enteros o decimales")

# numero3 = float(input("Ingrese un número (puede tener decimales): "))
# numero4 = float(input("Ingrese otro número (puede tener decimales): "))
# if numero3 == numero4:
#     print("Los números son iguales")
# else:
#     print("Los números son distintos")
# # Verificamos que el número es de tipo float (decimal), si no pongo float antes del input se toma como string
# print(type(numero3), type(numero4))






# print("-"*lineas)
# print("2) Pedirle tres números al operador e indicar el número mayor")

# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))
# num3 = float(input("Ingrese el tercer número: "))

# if num1 >= num2 and num1 >= num3:
#     mayor = num1
# elif num2 >= num1 and num2 >= num3:
#     mayor = num2
# else:
#     mayor = num3
# print("El número mayor es:", mayor)







# # print("-"*lineas)
# print("3) Solicitar un número al operador e indicar si es positivo y par")
# numero = int(input("Ingrese un número: "))

# if numero > 0 and numero % 2 == 0: 
#     print("El número es positivo y par.")
# else:
#     print("El número NO es positivo y par.")









# print("-"*lineas)
# print("4) Solicitar un número por teclado y controlar que se encuentre comprendido entre los números 1 y 12. " \
# "Si así lo esta sacar un mensaje que indique que el valor es correcto. " \
# "En caso contrario indicar que es incorrecto")

# numero = int(input("Ingrese un número entre 1 y 12: "))

# if 1 <= numero <= 12:
#     print("El valor es correcto.")
# else:
#     print("El valor es incorrecto.")







# print("-"*lineas)
# print("5) Aceptando dos números por el teclado, indicar si uno de ellos es divisible por otro")

# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))

# if num1 == 0 or num2 == 0:
#     print("No se puede dividir por cero o es cero")
# elif num1 == num2:
#     print(f"{num1} y {num2} son mutuamente divisibles")
#     # print(num1,"y",num2,"son mutuamente divisibles")
# # El resto de dividir num1 por num2 es 0?    
# elif num1 % num2 == 0: 
#     print(f"{num1} es divisible por {num2}.")
# elif num2 % num1 == 0:
#     print(f"{num2} es divisible por {num1}.")
# else:
#     print("Ninguno de los dos números es divisible por el otro")






    
# print("-"*lineas)
# print("6) Escribir un algoritmo que divida dos números que se ingresan. " \
# "Contemplar la imposibilidad de dividir por cero, imprimiendo un mensaje si se detecta esa condición")

# dividendo = float(input("Ingrese el dividendo: "))
# divisor = float(input("Ingrese el divisor: "))

# if divisor == 0:
#     print("No se puede dividir por cero.")
# else:
#     resultado = dividendo / divisor
#     print("El resultado de la división es:", resultado)






# print("-"*lineas)
# print("7) Ingresar dos números e indicar con un " \
# "–1 si ambos son negativos, " \
# "1 si ambos son positivos, " \
# "0 en el caso en que uno sea negativo y el otro positivo")

# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))

# if num1 < 0 and num2 < 0:
#     print(-1)  # Ambos negativos
# elif num1 > 0 and num2 > 0:
#     print(1)   # Ambos positivos
# else:
#     print(0)   # Uno positivo y otro negativo (o alguno es cero)






# print("-"*lineas)
# print("8) Realizar un programa que pida al operador dos números e indique el signo del producto sin realizarlo "
# "(regla de los signos)") 

# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))

# # Regla de los signos sin realizar el producto
# if num1 == 0 or num2 == 0:
#     print("El producto es cero")
# elif (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
#     print("El signo del producto es positivo")
# else:
#     print("El signo del producto es negativo")




   


# # .
# print("-"*lineas)
# print("9) Escribir un programa que acepte tres valores que representan las longitudes de los lados de un triangulo " \
# "y determine que tipo de triángulo es") 

# lado1 = float(input("Ingrese la longitud del primer lado: "))
# lado2 = float(input("Ingrese la longitud del segundo lado: "))
# lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Verificar si los lados pueden formar un triángulo (la suma de dos lados debe ser mayor que el tercero)
# if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
#     # Determinar el tipo de triángulo
#     if lado1 == lado2 == lado3:
#         print("Es un triángulo equilátero.")
#     elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#         print("Es un triángulo isósceles.")
#     else:
#         print("Es un triángulo escaleno.")
# else:
#     print("Los valores ingresados no pueden formar un triángulo.")







# print("-"*lineas)
# print("10) Escribir un algoritmo que realice el proceso de una calculadora, es decir:" \
# " solicite dos números y una variable de caracteres que puede ser “+”, “-“, “*”, o “/” e " \
# "imprima el resultado de las operaciones suma, resta, multiplicación y " \
# "división según corresponda en función del valor de la variable de caracteres") 

# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))

# # Solicitar la operación
# operacion = input("Ingrese la operación (+, -, *, /): ")

# if operacion == "+":
#     resultado = num1 + num2
#     print("Resultado de la suma:", resultado)
# elif operacion == "-":
#     resultado = num1 - num2
#     print("Resultado de la resta:", resultado)
# elif operacion == "*":
#     resultado = num1 * num2
#     print("Resultado de la multiplicación:", resultado)
# elif operacion == "/":
#     if num2 != 0:
#         resultado = num1 / num2
#         print("Resultado de la división:", resultado)
#     else:
#         print("No se puede dividir por cero")
# else:
#     print("Operación inválida. Solo se permiten: +, -, *, /.")







# print("-"*lineas)
# print("11) Realizar un programa que pida tres números en variables llamadas X1, X2, y X3, " \
# "y realice los reemplazos correspondientes de tal forma que " \
# "en X1 quede el mayor, en X3 el menor, y en X2 el restante (intermedio). " \
# "Mostrarlos de menor a mayor") 

# X1 = float(input("Ingrese el primer número (X1): "))
# X2 = float(input("Ingrese el segundo número (X2): "))
# X3 = float(input("Ingrese el tercer número (X3): "))

# # Variables auxiliares
# mayor = 0
# medio = 0
# menor = 0

# # Comparaciones para ordenar sin listas
# if X1 >= X2 and X1 >= X3:
#     mayor = X1
#     if X2 >= X3:
#         medio = X2
#         menor = X3
#     else:
#         medio = X3
#         menor = X2
# elif X2 >= X1 and X2 >= X3:
#     mayor = X2
#     if X1 >= X3:
#         medio = X1
#         menor = X3
#     else:
#         medio = X3
#         menor = X1
# else:
#     mayor = X3
#     if X1 >= X2:
#         medio = X1
#         menor = X2
#     else:
#         medio = X2
#         menor = X1

# # Reasignar las variables X1, X2, X3
# X1 = mayor
# X2 = medio
# X3 = menor

# # Mostrar de menor a mayor
# print("Los valores ordenados de menor a mayor son:")
# print("X3 (menor):", X3)
# print("X2 (intermedio):", X2)
# print("X1 (mayor):", X1)






# print("-"*lineas)
# print("12) Dado un mes y un año, indicar la cantidad de días que tienen. " \
# "Contemplar los años bisiestos. " \
# "Un año es bisiesto si es divisible por cuatro con excepción de los fines de siglos que no sean divisibles por 400")

# # # Un año es bisiesto si es divisible por 4.
# # # Si el año es divisible por 100, entonces no es bisiesto, 
# #     # excepto que además sea divisible por 400, entonces sí es bisiesto.

# # # Año | % 4 == 0  | % 100 != 0  | % 400 == 0  | Es bisiesto?
# # # 2020| SI        | SI          | NO          | SI
# # # 1900| SI        | NO          | NO          | NO
# # # 2000| SI        | NO          | SI          | SI
# # # 2023| NO        |             | NO          | NO

# # Solicitar mes y año al usuario
# mes = int(input("Ingrese el número del mes (1 a 12): "))
# anio = int(input("Ingrese el año: "))

# # Verificar si el año es bisiesto
# if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
#     bisiesto = True
# else:
#     bisiesto = False

# # Determinar la cantidad de días según el mes
# if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
#     dias = 31
# elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
#     dias = 30
# elif mes == 2:
#     if bisiesto:
#         dias = 29
#     else:
#         dias = 28
# else:
#     dias = None  # Mes inválido

# # Mostrar el resultado
# if dias is not None:
#     print(f"El mes {mes} del año {anio} tiene {dias} días.")
# else:
#     print("Mes inválido. Por favor ingrese un número entre 1 y 12.")






# print("-"*lineas)
# print("13) Escribir un programa que indique la hora correspondiente al minuto siguiente. " \
# "Es decir, debe solicitar por el teclado dos variables; " \
# "la primera de ellas corresponde a una hora, " \
# "en cambio la segunda a los minutos dentro de la hora. " \
# "Identifique Entrada, Proceso, y salida. " \
# "Realice el programa utilizando lenguaje C") 

# # Para tener en cuenta:
# # 60 seg -> 1 min
# # 60 min -> 1 h
# # 3600 seg -> 1 h
# # 3600 x 24 = 86400 seg
# # 24 h -> 1 dia


# # ----- ENTRADA -----
# hora = int(input("Ingrese la hora (0 a 23): "))
# minuto = int(input("Ingrese los minutos (0 a 59): "))

# # ----- PROCESO -----
# # Aumentar un minuto
# # minuto += 1
# minuto = minuto + 1

# # Verificar si hay cambio de hora
# if minuto == 60:
#     minuto = 0
#     hora = hora + 1
#     # Verificar si hay cambio de día
#     if hora == 24:
#         hora = 0

# # ----- SALIDA -----
# print("La hora un minuto después es:", hora, minuto)
# # print("La hora un minuto después es:", f"{hora:02d}:{minuto:02d}") # esta es otre forma de mostrar con dos digitos la linea de arriba







# print("-"*lineas)
# print("Requerir al operador el ingreso de dos valores, " \
# "la distancia recorrida en un auto, " \
# "y el consumo de combustible. " \
# "Indicar con la leyenda “consumo excesivo” si fue el rendimiento del combustible es inferior a 12 Km/l")

# distancia = float(input("Ingrese la distancia recorrida (en km): "))
# combustible = float(input("Ingrese el consumo de combustible (en litros): "))

# if combustible > 0:
#     rendimiento = distancia / combustible
#     print(f"El rendimiento fue de {rendimiento:.2f} km/l")
#     if rendimiento < 12:
#         print("Consumo excesivo")
# else:
#     print("Error: el consumo de combustible debe ser mayor que cero")






# print("-"*lineas)
# print("15) Calcular el salario neto a pagar por día, " \
# "a partir de la cantidad de horas trabajadas " \
# "y un determinado valor horario. " \
# "Tener en cuenta que para toda hora trabajada luego de la 8ª se abona un adicional del 50 % del valor horario; " \
# "y que a todo trabajador se le descuenta un 12% por jubilación y un 3% para la obra social") 

# horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
# valor_hora = float(input("Ingrese el valor por hora: "))

# # Calcular salario bruto
# if horas_trabajadas <= 8:
#     salario_bruto = horas_trabajadas * valor_hora
# else:
#     horas_normales = 8
#     horas_extra = horas_trabajadas - horas_normales
#     salario_bruto = (horas_normales * valor_hora) + (horas_extra * valor_hora * 1.5)

# # Descuentos
# descuento_jubilacion = salario_bruto * 0.12
# descuento_obra_social = salario_bruto * 0.03
# salario_neto = salario_bruto - descuento_jubilacion - descuento_obra_social

# print(f"Salario bruto: ${salario_bruto:.2f}")
# print(f"Descuento jubilación (12%): ${descuento_jubilacion:.2f}")
# print(f"Descuento obra social (3%): ${descuento_obra_social:.2f}")
# print(f"Salario neto a pagar: ${salario_neto:.2f}")


