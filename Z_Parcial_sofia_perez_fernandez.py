# # Pedir al usuario el ingreso de dos palabras
# palabra1 = input("Ingresá tu apellido: ") #input para pedirle al usuario que nos de los datos pedidos
# palabra2 = input("Ingresá tu nombre: ")
# # Crea el hashtag uniendo ambas palabras con un _
# hashtag = "#" + palabra1 + "_" + palabra2
# # Muestra el resultado
# print("El hashtag generado es:", hashtag)


# Le pedimos al usuario los siguentes datos como pide la consigna
hora = int(input("Ingresá la hora (0 a 24): ")) #int indicicando qe es numero entero 
minutos = int(input("Ingresá los minutos (0 a 59): ")) # input para pedirle al usuario los datos 

# Validamos la hora y los minutos de la siguente manera
if hora < 0 or hora > 24: 
    print("Error: la hora ingresada no es válida.")
elif minutos < 0 or minutos > 59:
    print("Error: los minutos ingresados no son válidos.")
else:
    print("El horario ingresado es correcto.")