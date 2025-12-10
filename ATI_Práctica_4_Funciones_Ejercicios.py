# 1.- Hacer un programa que reciba dos números desde el teclado y responda 
# "El número xxx divide (no divide) a yyy" ejecutando una función que devuelva 
# verdadero si el primero divide al segundo.


"""
# Ejercicio 1 - funcion
def divide_a(x,y): 
  if y%x == 0:         # MODULO
    return True
  else:
    return False

# Ejercicio 1 - programa
x=int(input("Ingrese entero x="))
y=int(input("Ingrese entero y="))

if divide_a(x,y):
  print ("x=",x," divide a ","y=",y)
else:
  print ("x=",x," NO divide a ","y=",y)
"""
  
"""
# 2.- Hacer un programa que responda:
# "El número xxx divide (no divide) a yyy" o
# "El número yyy divide (no divide) a xxx" o
# "Ninguno de los dos números divide al otro"
# utilizando la función anterior

def divide_a(a,b):    #Cambio los valores de x e y por a y b para no confundir
  if b%a == 0:        # MODULO
    return True
  else:
    return False

x=int(input("Ingrese entero x="))
y=int(input("Ingrese entero y="))

x_divide_y = divide_a(x, y)
y_divide_x = divide_a(y, x)

if x_divide_y:
  print (x," divide a ", y)
else:
  print (x," NO divide a ",y)

if y_divide_x:
  print (y," divide a ",x)
else:
  print (y," NO divide a ",x)

if (not x_divide_y) and (not y_divide_x):
  print ("Ninguno de los dos números divide al otro")
"""

"""
#3.- Hacer un programa que reciba un número desde el teclado y ejecutando la función anterior, 
# devuelva la lista de los divisores del número ingresado.

def divide_a(a,b):    #Cambio los valores de x e y por a y b para no confundir
  if b%a == 0:        # MODULO
    return True
  else:
    return False

# Ingreso de número
n = int(input("Ingrese un número: "))

# Construcción de lista de divisores
divisores = []

for i in range(1, n + 1):
    if divide_a(i, n):  # Si i divide a n
        divisores.append(i)

# Resultado
print(f"Los divisores de {n} son: {divisores}")
"""


"""
# 4.- Utilizando la función anterior hacer otra que devuelva verdadero 
# si el número recibido por parámetro es primo.

def divide_a(a,b):    #Cambio los valores de x e y por a y b para no confundir
  if b%a == 0:        # MODULO
    return True
  else:
    return False

def es_primo(n):
  i=2
  while not divide_a(i,n) and i<n:
    i+=1
  if i==n:
    return True
  else:
    return False

nro=int(input("Ingrese entero nro="))

if es_primo(nro):
  print ("nro=",nro," es primo")
else:
  print ("nro=",nro," NO es primo")
"""



"""
#5.- Utilizar las dos funciones anteriores ( "divide_a" y "es_primo" ) 
# para hacer un programa que reciba un número por teclado y 
# devuelva todos los números primos que lo dividen.

def divide_a(a,b):    #Cambio los valores de x e y -> por a y b para no confundir
  if b%a == 0:        # MODULO
    return True
  else:
    return False

def es_primo(n):
  i=2
  while not divide_a(i,n) and i<n:
    i+=1
  if i==n:
    return True
  else:
    return False

num=[]
n=int(input("Ingrese un número entero: "))

for i in range(1, n + 1):
  if divide_a(i,n) and es_primo(i):
    num.append(i)
print(num)
"""


"""
# 6.- Utilizando las funciones desarrolladas hasta ahora, 
# hacer un programa que reciba dos números desde el teclado y devuelva si son coprimos.

def divide_a(a,b):    #Cambio los valores de x e y -> por a y b para no confundir
  if b%a == 0:        # MODULO
    return True
  else:
    return False

def es_primo(n):
  i=2
  while not divide_a(i,n) and i<n:
    i+=1
  if i==n:
    return True
  else:
    return False

#**************************************************************
num1=[]
num2=[]
n1=int(input("Ingrese un número entero: "))
n2=int(input("Ingrese un número entero: "))

for i in range(1, n1 + 1):
  if divide_a(i,n1) and es_primo(i):
    num1.append(i)

for i in range(1, n2 + 1):
  if divide_a(i,n2) and es_primo(i):
    num2.append(i)

comunes = set(num1) & set(num2)
if len(comunes) == 0:
  print("Son coprimos")
else:
  print("NO son coprimos")
"""




"""
# 7.-
# Hacer una función que calcule el interés de una inversión recibiendo por parámetro 
# el capital, la TNA y la cantidad de días.

def calcular_interes(capital, tna, dias):
    return (capital * tna * dias) / (365 * 100)

# Hacer un programa que reciba los tres parámetros de una inversión por teclado devuelva el interés.

capital = float(input("Ingrese el capital: "))
tna = float(input("Ingrese la TNA (%): "))
dias = int(input("Ingrese la cantidad de días: "))

interes = calcular_interes(capital, tna, dias)
print(f"El interés generado es: ${interes:.2f}")

# Hacer un programa que reciba los parámetros de dos inversiones y 
# devuelva cuál es la más conveniente (paga más interés)

print("Ingrese los datos de la primera inversión:")
capital1 = float(input("Capital: "))
tna1 = float(input("TNA (%): "))
dias1 = int(input("Días: "))

print("\nIngrese los datos de la segunda inversión:")
capital2 = float(input("Capital: "))
tna2 = float(input("TNA (%): "))
dias2 = int(input("Días: "))

interes1 = calcular_interes(capital1, tna1, dias1)
interes2 = calcular_interes(capital2, tna2, dias2)

print(f"\nInterés de la primera inversión: ${interes1:.2f}")
print(f"Interés de la segunda inversión: ${interes2:.2f}")

if interes1 > interes2:
    print("La primera inversión es más conveniente.")
elif interes2 > interes1:
    print("La segunda inversión es más conveniente.")
else:
    print("Ambas inversiones generan el mismo interés.")
"""

"""
# 8.- Hacer una función FdeX que calcule 3*X+2 y otra función GdeX que calcule -X+5. 
# Luego hacer un programa que utilizando estas dos funciones, 
# reciba por teclado un valor de X y devuelva FdeX compuesta con GdeX para el valor ingresado y 
# 10 valores de X más, incrementados de a dos en cada iteración.

def f(x):
  return 3 * x + 2

def g(x):
  return -x + 5

def FcompuestaG(x):
    return f(g(x))

#**********************************************************************
nro=int(input("ingrese un número: "))

print(f"\nLos 10 resultados de F(G(x)) comenzando en {nro} son:\n")

for i in range(10):  
    valor = nro + 2 * i
    resultado = FcompuestaG(valor)
    print(f"{i+1} - F(G({valor})) = {resultado}")
"""    