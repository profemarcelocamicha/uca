# Desarrolle un programa que calcule la bonificación anual para empleados según estas reglas:
# Solicitar:
# Antiguedad: años completos
# Evaluación de desempeño: 1-5 donde 5 es excelente
# Salario mensual actual
# Validaciones:
# * Si antiguedad < 1 año: No aplica bono ("Requisito mínimo no cumplido")
# * Si evaluación es 1 o 2: No aplica bono ("Desempeño insuficiente")
# * Solo si pasa ambas validaciones anteriores, calcular bono con estas reglas:
# Si antiguedad es mayo a 10 años y evaluacion igual a 4 o 5:
#    bono = evaluación dividido 5 por diez
# Sino:
#   bono = desempeño dividido 5
# Mostrar en pantalla los mensajes correspondientes en caso de no corresponder bono, y en caso de corresponder bono calcular el nuevo salario



# mensaje_antiguedad= "ingrese su antiguedad en años completados:" #asigno la variable del mensaje para pedir la antiguedad
# antiguedad= int(input(mensaje_antiguedad)) #a la variable antiguedad, le asigno pedir al usuario un mensaje en número, por lo cual le asigno int al input que es una variable de typo str
# mensaje_evaluación= "ingrese su evaluación de desempeño:" #asigno la variable del mensaje para pedir la evaluación
# evaluación= int(input(mensaje_evaluación)) #a la variable antiguedad, le asigno pedir al usuario un mensaje en número, por lo cual le asigno int al input que es una variable de typo str
# mensaje_salario= "ingrese su salario mensual actual:" #asigno la variable del mensaje para pedir el salario
# salario= float(input(mensaje_salario)) #a la variable salario, le asigno pedir al usuario un mensaje en número, por lo cual le asigno float (ya que el salario puede tener comas) al input que es una variable de typo st
# bono=float(0)
# if antiguedad<1: 
#     print("requisito mínimo no cumplido")
# elif evaluación==1 or evaluación==2:
#     print("desempeño insuficiente")
# elif antiguedad>=10 and (evaluación==4 or evaluación==5):
#     bono= evaluación/5*10
# else:
#     bono= evaluación/5
# total = salario + bono
# print(f"salario: {salario} bono: {bono} total a cobrar: {total}")


# Ejercicio 3

# Escribir un programa que realice las siguientes tareas:
# * Solicitar al usuario el ingreso de números hasta que el número ingresado sea cero
# * Guardar los números ingresados en una lista
# * Informar cuántos números ingresados son mayores a 1, y cuántos son menores a 1.

# lista=[]
# numMay1 = 0
# numMen1 = 0
# while True:
#     numero=float(input("ingrese numero: "))
#     if numero == 0:
#         break
#     else:
#         lista.append(numero)

# for num in lista:
#     if num > 1:
#         numMay1+= 1
#     elif num < 1:
#         numMen1+=1
# print(f"Números mayores a 1: {numMay1}")
# print(f"Números menorea a 1: {numMen1}")
# print(f"Números: {lista}")
            
#Ejercicio con errores
# numeros = [] #creo la lista numeros
# num=int(input("Ingrese un número")) #le pido al usuario que ingrese un mensaje y lo transformo a un número
# while num!=0: #mientras que el numero sea diferente a 0
#     num=int(input("Ingrese un número")) #va a volver a pedir que ingrese un numero
#     numeros.append(num) #y va a agregar el numero ya ingresado a la lista
# mayores_a_uno=[] #creo la lista de numeros mayores a 1
# menores_a_uno=[] #creo la lista de numeros menores a 1
# for num in numeros: #por cada numero en la lista de numeros 
#     if num>1: #si es mayor a uno va a agregarse a la lista de numeros mayores a 1
#         mayores_a_uno.append(num) 
#     if num<1: #si es menor a uno va a agregarse a la lista de numeros menores a 1
#         menores_a_uno.append(num)
# #muestro ambas listas en pantalla.
# print(mayores_a_uno)
# print(menores_a_uno) 


# Ejercicio 4 (opcional)
# Modificar el siguiente ejercicio para contemplar las siguientes situaciones:
# * Detectar el máximo valor, y mostrarlo por pantalla al finalizar el ciclo
# * Calcular el promedio, y mostrarlo por pantalla al finalizar el ciclo

#Profe
# total_ventas = 0
# maximo = 0
# ventas = [15000, 22000, 18000, 19500, 10000]
# for venta in ventas:
#     total_ventas += venta
#     if venta > maximo:
#         maximo = venta
# promedio = total_ventas/len(ventas)

#Alumno
# total_ventas = 0
# max_venta = ventas[0] 
# ventas = [15000, 22000, 18000, 19500, 10000]
# for venta in ventas:
#     total_ventas += venta
#     if venta > max_venta:
#         max_venta = venta
# promedio = total_ventas / len(ventas)
# print("Venta máxima:", max_venta)
# print("Promedio de ventas:", promedio)