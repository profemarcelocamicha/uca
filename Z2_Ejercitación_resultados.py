# # Enunciado 1
# # Ingresar números enteros positivos uno por uno.
# # El proceso debe continuar hasta que la suma acumulada de los valores ingresados supere 500.
# # Al finalizar, mostrar cuántos números fueron necesarios para superar el límite.

suma = 0
contador = 0

while suma <= 500:
    num = int(input("Ingrese un número positivo: "))
    suma += num
    contador += 1

print(f"Se superó el límite con {contador} números ingresados.")


# # Enunciado 2
# # Solicitar al usuario que ingrese una contraseña.
# #  Mientras la contraseña no tenga al menos 8 caracteres o no contenga un dígito,
# #  seguir pidiendo que la reingrese.
# #  Cuando sea válida, mostrar un mensaje de confirmación.

contraseña = input("Ingrese una contraseña: ")

def tiene_digito(cadena):
    for c in cadena:
        if c.isdigit():
            return True
    return False

while len(contraseña) < 8 or not tiene_digito(contraseña):
    print("Contraseña inválida. Debe tener al menos 8 caracteres y contener un número.")
    contraseña = input("Ingrese nuevamente la contraseña: ")

print("Contraseña registrada con éxito.")


# # Enunciado 3
# # Ingresar la temperatura promedio de cada uno de los 12 meses del año.
# # Al finalizar, calcular y mostrar la temperatura media anual.

suma_temp = float(0)

for mes in range(1, 13):
    temp = float(input(f"Ingrese la temperatura del mes {mes}: "))
    suma_temp = suma_temp + temp   

promedio = suma_temp / 12
print(f"La temperatura media anual es: {promedio:.2f}°C.")


# # Enunciado 4
# # Solicitar al usuario que ingrese 5 palabras.
# # Luego, mostrar cuántas vocales tiene cada palabra.

vocales = "aeiouAEIOU"
for i in range(1, 6):
    palabra = input(f"Ingrese la palabra {i}: ")
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    print(f"La palabra '{palabra}' tiene {contador} vocal(es).")