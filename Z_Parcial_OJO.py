# Ejercicios Agustina

"""
# Ejercicio1
# Espacios o : al final de los inputs (un tema estetico)
# Concatenación de String: str(código_cliente) + "-" + apellido[:3]
# Tener presente la selección de parte de un string - apellido[:3]


mensaje_código_cliente="Ingresar el código de cliente:" #asigno la variable del mensaje para pedir el código
código_cliente= int(input(mensaje_código_cliente)) #a la variable código_cliente le asigno pedir al usuario un mensaje en número, por lo cual le asigno int al input que es una variable de typo str
mensaje_apellido="Ingresar apellido del cliente:" #asigno la variable del mensaje para pedir el apellido
apellido= input(mensaje_apellido) #a la variable apellido le asigno pedir al usuario un mensaje

identificador= str(código_cliente) + "-" + apellido[2:] #uno las variables del código en str en lugar de número int, y del apellido selecciono los primeros tres elementos de apellido
print(identificador) #me muestra el resultado en pantalla

#print(str(código_cliente) + "-" + apellido[2:])

"""




"""
# Ejercicio2
# Mal manejo de la variable bono
# Además esta linea es incorrecta: nuevo_salario= salario, + bono
bono=int(0)
mensaje_antiguedad= "ingrese su antiguedad en años completados" #asigno la variable del mensaje para pedir la antiguedad
antiguedad= int(input(mensaje_antiguedad)) #a la variable antiguedad, le asigno pedir al usuario un mensaje en número, por lo cual le asigno int al input que es una variable de typo str
mensaje_evaluación= "ingrese su evaluación de desempeño" #asigno la variable del mensaje para pedir la evaluación
evaluación= int(input(mensaje_evaluación)) #a la variable antiguedad, le asigno pedir al usuario un mensaje en número, por lo cual le asigno int al input que es una variable de typo str
mensaje_salario= "ingrese su salario mensual actual" #asigno la variable del mensaje para pedir el salario
salario= float(input(mensaje_salario)) #a la variable salario, le asigno pedir al usuario un mensaje en número, por lo cual le asigno float (ya que el salario puede tener comas) al input que es una variable de typo st
if antiguedad<1: 
    print("requisito mínimo no cumplido")
elif evaluación==1 or evaluación==2:
    print("desempeño insuficiente")
else:
    if antiguedad>=10 and evaluación==4 or evaluación==5:
        bono= (evaluación/5)*10
    else:
        bono= evaluación/5
nuevo_salario= salario + bono

print("salario", salario)
print("antiguedad", antiguedad)
print(evaluación)
print(bono)
print(nuevo_salario)



# Ejercicio3
# Se solicita un input de un numero que nunca se usa. Mal manejo de condición de while
# tener presente el uso de .append para agregar elementos a una lista
# Como resultado del ejercicio se imprimen las listas y lo que se pide es la cantidad
numeros = [] #creo la lista numeros
num=int(input("Ingrese un número")) #le pido al usuario que ingrese un mensaje y lo transformo a un número
while num!=0: #mientras que el numero sea diferente a 0
    num=int(input("Ingrese un número")) #va a volver a pedir que ingrese un numero
    numeros.append(num) #y va a agregar el numero ya ingresado a la lista
mayores_a_uno=[] #creo la lista de numeros mayores a 1
menores_a_uno=[] #creo la lista de numeros menores a 1
for num in numeros: #por cada numero en la lista de numeros 
    if num>1: #si es mayor a uno va a agregarse a la lista de numeros mayores a 1
        mayores_a_uno.append(num) 
    if num<1: #si es menor a uno va a agregarse a la lista de numeros menores a 1
        menores_a_uno.append(num)
#muestro ambas listas en pantalla.
print(len(mayores_a_uno))
print(len(menores_a_uno)) 

"""
numeros=[]
numeros.append(3)
numeros.append(4)
numeros.append(5)
numeros.append(1)
print(numeros) #[3, 4, 5, 1]

for num in numeros:
    print(num)

print("cantidad de elementos:", len(numeros))




"""

# Ejercicio3
# Se solicita un input de un numero que nunca se usa. Mal manejo de condición de while
# tener presente el uso de .append para agregar elementos a una lista
# Esta asignación no tiene sentido: max_venta = ventas[0], es mejor poner directamente max_venta = 0
# tener presente el uso de la función len() para saber la cantidad de elementos en la lista

total_ventas = 0
ventas = [15000, 22000, 18000, 19500, 10000]
max_venta = ventas[0] 

for venta in ventas:
    total_ventas += venta
    if venta > max_venta:
        max_venta = venta

promedio = total_ventas / len(ventas)

print("Venta máxima:", max_venta)
print("Promedio de ventas:", promedio)



# Ejercicios Sofi
# Ejercicio1 OK.
# Tener presente que si se ingresan 2 apellidos queda un especio en blanco
# Pedir al usuario el ingreso de dos palabras
palabra1 = input("Ingresá tu apellido: ") #input para pedirle al usuario que nos de los datos pedidos
palabra2 = input("Ingresá tu nombre: ")
# Crea el hashtag uniendo ambas palabras con un _
hashtag = "#" + palabra1 + "_" + palabra2
# Muestra el resultado
print("El hashtag generado es:", hashtag)


# Ejercicio2.a
# Buscamos de crear una lista vacia para ahi poder poner los resultados
# Tener en cuanta el uso del for. En esta caso se pone un solo parámetro, por lo que se asume que empieza en 0
# y cuando llega a 20 sale

valores = []
# Generamos los 20 valores de x, a partir del 0 hasta el 19 porque el 20 no lo incluye
for x in range(20):
    # Calculamos la función f(x)
    y = 0.75 + 0.3 * x + (0.25 * x) ** 4 #Para multiplicar usamos el * y para la potencia usamos ** el parentesis indica que a 0,25X lo queremos elevar a la cuarta, por eso usamos el parentesis
    # Como pide guardar los valores lo hacemos de la siguente forma 
    valores.append(y)
    # Siempre que queremos ver los resultados cada vez que ejecutamos ponemos print 
    print("f(", x, "):", y)



# Ejercicio2.b
# Definimos la función f que recibe "x" como argumento
def f(x):
    return 0.75 + 0.3 * x + (0.25 * x) ** 4

# Lista para guardar los valores
valores = []

# Recorremos los 20 valores de x desde 0 hasta 19
for x in range(20):
    y = f(x)  # Asi llamamos a la función que nos pide que devolvamos 
    valores.append(y)  # Guardamos los resultados como pide la consigna
    print(f"f({x}): {y}")  # Y mostramos el resultado con el print




# Ejercicio3
# Le pedimos al usuario los siguentes datos como pide la consigna
# Acá creo que se equivocó el profe en el enunciado. Debería ser la hora entre 0 y 23
# Es decir, la condición debería ser: if hora < 0 or hora > 23: 

hora = int(input("Ingresá la hora (0 a 24): ")) #int indicicando qe es numero entero 
minutos = int(input("Ingresá los minutos (0 a 59): ")) # input para pedirle al usuario los datos 

# Validamos la hora y los minutos de la siguente manera
if hora < 0 or hora > 24: 
    print("Error: la hora ingresada no es válida.")
elif minutos < 0 or minutos > 59:
    print("Error: los minutos ingresados no son válidos.")
else:
    print("El horario ingresado es correcto.")

"""