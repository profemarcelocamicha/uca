# ## 1. Crear una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 20, 15, 14, 16]
print (numeros)

# ## 2. Acceder a elementos (indexación)

# numeros[0]    # primer elemento
print (numeros[0])

# numeros[2]    # tercer elemento
print (numeros[2])

# ## 3. Modificar un elemento

numeros[1] = 10   # reemplaza el 2 por 10
print (numeros)

# ## 4. Agregar elementos

# ### append() : agrega al final

numeros.append(5)
print (numeros)


numeros.insert(1, 50)  # en índice 1
print (numeros)

# ## 5. Eliminar elementos

# ### remove) : eliina un valor específico

numeros.remove(3)  # borra el 3
print (numeros)

ultimo = numeros.pop()      # quita el último
print ("se eliminó:", ultimo)
print (numeros)

primero = numeros.pop(0)    # quita el primero
print ("se eliminó:", primero)
print (numeros)


del numeros[2]
print (numeros)


# ## 6. Obtener la cantidad de elementos

len(numeros)
print (len(numeros))

# ## 7. Buscar elementos

# numeros.index(10)   # devuelve la posición del 10
print (numeros.index(10))

# ## 8. Contar cuántas veces aparece un valor

# numeros.count(4)
print (numeros.count(10))


# ## 9. Ordenar la lista

# ### sort() : ordena la lista

numeros.sort()
print (numeros)


numeros.sort(reverse=True)
print (numeros)

# ## 10. Invertir el orden

numeros.reverse()
print (numeros)

# ## 11. Concatenar listas

numeros_pares = [2, 4, 6, 8]
numeros_impares = [1, 3, 5, 7]

numeros = numeros_pares + numeros_impares
print (numeros)


# ## 12. Rebanado (slicing)

sub = numeros[1:4]   # desde índice 1 hasta 3
print (sub)

# ## 13. Copiar una lista

copia = numeros[:]       # copia completa
# copia = numeros.copy()   # es lo mismo que la línea anterior
print (copia)