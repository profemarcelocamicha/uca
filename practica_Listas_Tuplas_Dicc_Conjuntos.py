import os
os.system('cls')



# LISTAS 
# CARACTERÍSTICAS: Ordenadas - Mutables - Permite Duplicados - No usa clave:valor

frutas = ["manzana", "banana", "naranja", "banana", "pera"]
# 1-Imprime la variable frutas
print ("1-", frutas)

# 2-Imprime lo que esta en la posición 0
print("2-",frutas[0])  

# 3-Imprime lo que esta en la posición 1
print("3-",frutas[1])  

# 4-Imprime lo que esta en la última posición
print("4-",frutas[-1])  

# 5-Agregar "uva" a la lista
frutas.append("uva")

# 5-Imprimo la variable frutas para ver que se agrego uva
print ("5-",frutas)

# 6-Eliminar "banana" de la lista
# 6-El método remove() borra el primer elemento de la lista con el valor especificado.
frutas.remove("banana")

# 6-Imprimo la variable frutas para ver que se elimino "banana"
print ("6-",frutas)

# 7-Eliminar "banana" de la lista e informar el elemento borrado
# 7-El método pop() borra un ítem de una ubicación específica y nos devuelve el valor del ítem eliminado.
# 7-Elimino la fruta de la posición 1 (banana)
elemento_eliminado=frutas.pop(0)
print("7- Elemento eliminado:", elemento_eliminado)

# 8-Imprimo la variable frutas para ver que se elimino "banana"
print ("8-",frutas)

# 9-Eliminar un elemento por índice (Equivalente a pop(1), pero del no devuelve el valor eliminado).
del frutas[1]
print ("9-",frutas)

# 10-Eliminar varios elementos (rebanado o slice)
del frutas[0:2]
print ("10-",frutas)

# Eliminar toda la lista
del frutas  # Ahora 'frutas' ya no existe

# 11-Vuelvo a crear la lista
frutas = ["manzana", "banana", "naranja", "banana", "pera"]
# 11-Imprime la variable frutas
print ("11-", frutas)

# 12-Revierte el orden de la lista
frutas.reverse()
print("12-",frutas)

# 13-Ordeno la lista
frutas.sort()
print("13-",frutas)

# 14-Cuenta los elementos de una lista
cantidad=len(frutas)
print("14-Cantidad de frutas: ", cantidad)

# 15-Selecciona un rango de la lista
seleccion=frutas[0:2]
print("15-Selección de frutas: ", seleccion)

# 16-Agrego un elemento a la lista con un operador de suma
verduras=["lechuga","zanahoria"]
verduras=verduras+["zapallo"]
print("16-Verduras: ", verduras)

# 17-Uno dos listas
listas_unidas=frutas+verduras
print("17-Listas unidas: ", listas_unidas)





###########################################################################################################
#TUPLAS
# CARACTERÍSTICAS: Ordenadas - NO Mutables - Permite Duplicados - No usa clave:valor
# NO MUTABLES SIGNIFICA QUE NO LA PODEMOS MODIFICAR. EJ: TUPLA[5]="8" DARIA ERROR
# Para acceder a los elementos se hace de la misma manera que con listas

# Se puede convertir una lista en tupla:
frutas = ["manzana", "banana", "naranja", "banana", "pera"]
tupla=tuple(frutas)
print("18-tupla:",tupla)

# Se puede convertir una tupla a una lista:
lista_de_frutas=list(tupla)
print("19-lista",lista_de_frutas)






###########################################################################################################
# DICCIONARIOS
# CARACTERÍSTICAS: NO Ordenados - Mutables - NO Permite Duplicados (claves únicas) - Se accede por clave
# Cada elemento se compone de un par clave-valor.
# Para su definición es necesario encerrar los elementos entre llaves.
# Se accede a un valor utilizando su clave. Por este motivo, no se pueden repetir las claves para elementos distintos.
# Es posible agregar, eliminar o modificar valores (son mutables).

# 20-Creo un diccionario
diccionario = {"nombre":"Santiago","edad":25}
print("20-", diccionario)


# 21-Creo un diccionario con claves de distintos tipos
diccionario = {"nombre":"Santiago", "edad":25, (1,2):"valor de indice tupla", 10:"valor de indice numérico"}
print("21-", diccionario)


# 22-Accedemos al diccionario por las claves
print("22-", diccionario[("nombre")])
print("22-",diccionario[("edad")])
print("22-",diccionario[(1,2)])
print("22-",diccionario[(10)])
#print(diccionario[ "25" ])


# 23-El diccionario es mutable
diccionario_a = {"nombre":"Santiago","edad":42}
diccionario_a[ "nombre" ] = "Pepe"
print("23-",diccionario_a)


# 24-Agregamos claves y valores
diccionario_b = {"nombre":"Mariano","edad":42}
diccionario_b["direccion"] = "Av Montes de Oca 1234"
diccionario_b["localidad"]="CABA"
print("24-",diccionario_b)


# 25-Borramos un elemento
diccionario_c = {"nombre":"Karina","edad":25}
print("25-",diccionario_c)
diccionario_c.pop("edad")
print("25-",diccionario_c)


# 26-Ejemplos combinados
diccionario_a = {"nombre":"Mariano","edad":42}
diccionario_b = {"direccion":"Av Montes de Oca 1234","codigoPostal":1712}
diccionario_c={"datos":diccionario_a,"direccion":diccionario_b}
print("26-",diccionario_c)
print("26-",diccionario_c["datos"])
print("26-",diccionario_c["direccion"])


# 27-Ejemplos combinados
lista_a=[1,2,3,4]
diccionario_d={ "dic a":diccionario_a,"dic b":diccionario_b,"lista":lista_a}
print("27-",diccionario_d)
print("27-",diccionario_d["dic a"])
print("27-",diccionario_d["dic b"])
print("27-",diccionario_d["lista"])
print("27-",diccionario_d["lista"][2])




###########################################################################################################
# CONJUNTOS -- SET
# CARACTERÍSTICAS: NO Ordenados - Mutables - NO muestra Duplicados - No se Se accede por indice

# 28-Creo un conjunto
conjunto = {3, 2, 2, 1, 2, 0}
print("28-",conjunto)  

# 29-Agrego un elemeno al conjunto
conjunto.add(4)
print("29-",conjunto)

# Esta linea da error porque en los conjuntos no se puede asignar valores por indices
#numeros[0]=5

# 30-Elimino un elemento
conjunto.remove(2)
print("30-",conjunto)

# 31-creo un conjunto con elementos de varios tipos
conjunto={ 1 , 2.5,"A",(1,2,3),"A","Mi conjunto variado"}
print("31-",conjunto)

# 32-diferencia con elementos repetidos
lista_igual=[1,1,1,1]
print("32-",lista_igual)

conjunto_igual={1,1,1,1}
print("32-",conjunto_igual)

# 33-averiguamos el tipo de dato de la variable
tipo=type(conjunto_igual)
print("33-",tipo)

# 34-agregamos un elemento al conjunto
conjunto.add("B")
print("34-",conjunto)

# 35-descartamos un elemento
conjunto.discard("A")
print("35-",conjunto)

# 36-transformamos un lista en conjuntos
lista_a=[1,2,2,3,3,3,3,4,5,6,7,8,9,10]
print("36-",lista_a)
conjunto_lista_a=set(lista_a)
print("36-",conjunto_lista_a)