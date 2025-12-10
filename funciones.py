def multiplicar_numeros(numero1,numero2):
    resultado = numero1 * numero2
    return resultado

#programa princial

num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese un numero"))

resul = multiplicar_numeros(num1,num2)
print(resul)

"""

#resultado_devuelto_3 = multiplicar_numeros(multiplicar_numeros(5,2),2)






def multiplicar_numeros(numero1,numero2):
    resultado=numero1*numero2
    return resultado

resultado_devuelto_3 = multiplicar_numeros(multiplicar_numeros(5,2),2)

print("Resultado devuelto final: "+str(resultado_devuelto_3))



# ****************************************************************************************

def sumar_numeros(numero1,numero2):
    resultado = numero1+numero2
    return resultado

def operaciones(numero1,numero2):
    resultado1 =sumar_numeros(numero1,numero2)
    resultado2= multiplicar_numeros(resultado1,2)
    return resultado2

#Programa principal
print("Resultado devuelto: "+str(resultado_operaciones))
"""

# ****************************************************************************************

"""
def saludo_horario(horario):
    saludo=""
    if horario>5 and horario<=12:
        saludo="Buen día"
    else:
        if horario>12 and horario<20:
            saludo="Buenas tardes"
        else:
            saludo="Buenas noches"
    return saludo

print(saludo_horario(21))

# ****************************************************************************************

def sumar_lista(lista):
    resultado=0
    for i in lista:
        resultado=resultado+i
        # print(resultado)
    return resultado

#Programa principal
lista_1=[1,2,3,4,5,6,7,8]

resultado_suma=sumar_lista(lista_1)

print("Resultado de sumar los elementos de la lista: "+str(resultado_suma))


# ****************************************************************************************

def funcion_args_opcionales(arg1, arg2=0.5):
    resultado=arg1+arg2
    return resultado

resultado_1=funcion_args_opcionales(5,1)
print(resultado_1)

resultado_1=funcion_args_opcionales(5)
print(resultado_1)

"""