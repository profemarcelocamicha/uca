# # Las tuplas son inmutables
# # Una tupla no se puede cambiar una vez creada.

t = (1, 2, 3)
print(t[0])

# Intentar hacer estas operaciones da error:
# t.append(4)     # Error
# t.remove(2)     # Error
# t[0] = 10       # Error
# del t[1]        # Error


# # Una lista sí se puede modificar:
# l = [1, 2, 3]
# l[0] = 10  # permitido

# # Si los datos no deberían cambiar, una tupla es más segura.
# # Ejemplo: coordenadas, fechas, claves, configuraciones fijas.

# # Las tuplas ocupan menos memoria
# # Las tuplas son más livianas internamente.
# # Esto las hace ideales para:
# #    grandes cantidades de datos fijos
# #    almacenar registros inmutables
# #    optimizar rendimiento
# # En general, una tupla equivale a una lista pero **más compacta**.
# # Las tuplas son un poco más rápidas

# Ejemplo:

# persona = ("Juan", "Pérez", 30)
# persona[0] = "Carlos"  # Recordar que no lo permite

# # Las tuplas pueden ser claves de diccionarios. Las listas no.

# diccionario = {}
# diccionario[(1, 2)] = "coordenada"  # ✔ permitido
# diccionario[[1, 2]] = "coordenada"  # Error: las listas no son hashables

# # Ejemplo de cuando devolvés múltiples valores en una función:

# def dividir(a, b):
#     return a // b, a % b  # devuelve una tupla

# # Resumen

# # | Característica                    | Lista                 | Tupla       |
# # | --------------------------------- | --------------------- | ----------- |
# # | ¿Se puede modificar?              | ✔ Sí                  | No        |
# # | Tamaño en memoria                 | Mayor                 | Menor       |
# # | Velocidad                         | Ligeramente más lenta | Más rápida  |
# # | ¿Sirve como clave de diccionario? | No                    | Sí        |
# # | Casos típicos                     | Datos cambiantes      | Datos fijos |

