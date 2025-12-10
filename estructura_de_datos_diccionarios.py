# # ---------------------------------------------------------------------------------------
# # Ejemplo de uso de diccionarios para almacenar información de personas

# personas = []

# # Agregar personas
# personas.append({"nombre": "Juan", "apellido": "Pérez", "edad": 30})
# personas.append({"nombre": "María", "apellido": "Gómez", "edad": 25})
# personas.append({"nombre": "Lucía", "apellido": "Ramírez", "edad": 40})

# # Mostrar la lista completa
# print("Lista de personas:")
# for p in personas:
#     print(f"{p['nombre']} {p['apellido']} - {p['edad']} años")


# # ---------------------------------------------------------------------------------------
# # Ejemplo de carga de datos por teclado

# personas = []

# for i in range(3):  # cargar 3 personas
#     print(f"\nPersona {i+1}")
#     nombre = input("Nombre: ")
#     apellido = input("Apellido: ")
#     edad = int(input("Edad: "))

#     persona = {
#         "nombre": nombre,
#         "apellido": apellido,
#         "edad": edad
#     }

#     personas.append(persona)

# # Mostrar resultados
# print("\nPersonas cargadas:")
# for p in personas:
#     print(f"{p['nombre']} {p['apellido']} - {p['edad']} años")


# # Ejemplo de acceso a datos específicos. Mostrar el nombre, apellido y edad de la primera persona cargada.
# print("\nDatos de la primera persona cargada:")
# print(personas[0]["nombre"])
# print(personas[0]["apellido"])
# print(personas[0]["edad"])


# # ---------------------------------------------------------------------------------------
# # Ejemplo de búsqueda y modificación
# buscar = "Gómez"

# for p in personas:
#     if p["apellido"] == buscar:
#         print("Encontrado:", p)

