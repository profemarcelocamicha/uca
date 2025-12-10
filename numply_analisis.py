import numpy as np
import matplotlib.pyplot as plt
import statistics

#array1 = np.array([1,2,3])
# print(array1)

# array2 = np.array([1,2,3], dtype='int32')
# print(array2)

# array3 = np.array([1,2,3], dtype='float')
# print(array3)

# print (array3[0])

# longitud = array1.size
# print("El tamaño del array es",longitud)

# array_zeros = np.zeros(5)
# print(array_zeros)

# array_unos = np.ones(5)
# print(array_unos)

# array_azar = np.random.rand(5) # Crea un array de 5 números aleatorios entre 0 y 1
# print(array_azar)
# array_azar2 = np.random.rand(2, 3) # matriz 2x3 con valores entre 0 y 1.
# print(array_azar2)
# array_azar3 = np.random.randint(1, 10, size=5) # 5 enteros aleatorios entre 1 y 9.
# print(array_azar3)


# #array1 = np.array([1,2,3])
# array_suma1 = array1 + 2
# print(array_suma1)

# #array1 = np.array([1,2,3])
# array_resta1 = array1 - 2
# print(array_resta1)

# #array1 = np.array([1,2,3])
# array_multiplicacion1=array1 * 2
# print(array_multiplicacion1)

#Suma de listas
# lista1 = [1,2,3,4,5,6,7,8,9,10]
# lista2 = [10,9,8,7,6,5,4,3,2,1]
# lista_result = lista1 + lista2
# print(lista_result)

#Suma de arrays
# array_suma1 = np.array([1,2,3,4,5,6,7,8,9,10])
# array_suma2 = np.array([10,9,8,7,6,5,4,3,2,1])
# array_result_suma = array_suma1 + array_suma2
# print(array_result_suma)

# #Multiplicación de listas
# lista_mult = [1,2,3,4,5,6,7,8,9,10]*2
# print(lista_mult)

# #Multiplicación de arrays
# array_mult1 = np.array([1,2,3,4,5,6,7,8,9,10])
# array_resultado_mult_numpy = array_mult1*2
# print(array_resultado_mult_numpy)

# #Minimo de una lista
# #lista1 = [1,2,3,4,5,6,7,8,9,10]
# print(min(lista1))

# #Minimo de un array
# #array1 = np.array([1,2,3])
# print(np.min(array1))

# #Maximo de una lista
# #lista1 = [1,2,3,4,5,6,7,8,9,10]
# print(max(lista1))

# #Maximo de un array
# #array1 = np.array([1,2,3])
# print(np.max(array1))

# #Promedio de una lista
# #lista1 = [1,2,3,4,5,6,7,8,9,10]
# # Es necesario: import statistics
# print(statistics.mean(lista1))

# #Promedio de un array
# #array1 = np.array([1,2,3])
# print(np.mean(array1))

#suma el contenido de una lista
# lista1 = [1,2,3,4,5,6,7,8,9,10]
# print(sum(lista1))

# #suma el contenido de un array
# #array1 = np.array([1,2,3])
# print(np.sum(array1))


# print("np.arrange--------------")
# # Crear un array con datos del 0 al 10 (el 10 no lo tiene en cuenta)
# # Sintaxis: np.arange(inicio, fin, paso)
# print(np.arange(0,10))          #[0 1 2 3 4 5 6 7 8 9]
# # Crear un array con datos del 0 al 10 (el 10 no lo tiene en cuenta) con pasos de a 2
# # Sintaxis: np.arange(inicio, fin, paso)
# print(np.arange(0,10,2))        #[0 2 4 6 8]
# print(np.arange(5))             #[0 1 2 3 4]
# print(np.arange(2, 10, 2))      #[2, 4, 6, 8]
# print(np.arange(0, 1, 0.2))     #[0. , 0.2, 0.4, 0.6, 0.8]

# print("np.linspace--------------")
# print(np.linspace(0, 100, 5))


# print("Ejercicios--------------")
# x_funcion1 = np.array([1,2,3,4,5]) 
# print(x_funcion1)                   #[1 2 3 4 5]
# print(x_funcion1**2)                #[ 1  4  9 16 25]

# function1_paso1 = 3*x_funcion1**2   
# print(function1_paso1)              #[ 3 12 27 48 75]

# function1_paso1 = x_funcion1**2*3
# print(function1_paso1)              #[ 3 12 27 48 75] (El orden de los factores no altera el producto)

# function1_paso2 = 0.5*x_funcion1**2
# print(function1_paso2)              #[ 0.5  2.   4.5  8.  12.5]


# #function1_paso1 [ 3    12    27     48     75]
# #function1_paso2 [ 0.5   2.    4.5    8.    12.5]
# #function1_paso3 [ 3.5  14.   31.5   56.    87.5]
# function1_paso3 = function1_paso1+function1_paso2
# print(function1_paso3) 

# y_funcion1 = function1_paso3+0.5
# print(y_funcion1)       #[ 4.  14.5 32.  56.5 88. ]

# print("np.linspace--------------")
# # np.linspace(inicio, fin, muestras)
# x_funcion2 = np.linspace(0, 4, 5)
# print(x_funcion2)       #[0. 1. 2. 3. 4.]

# y_funcion2 = 2 * x_funcion2**3 + 3 * x_funcion2**2 + 0.5
# print(y_funcion2)       #[  0.5   5.5  28.5  81.5 176.5]

# # x_funcion2 contiene los valores de x_funcion1
# # y_funcion2 contiene los valores de f(x), es decir, y
# # Con estos dos datos ya se puede graficar la funcion

# # plt.plot(x_funcion2,y_funcion2)
# # plt.xlabel("x")
# # plt.ylabel("y")
# # plt.title("y(x)")
# # plt.show()

# def f1(x):
#   y=2 * x + 0.5 * x**2 + 0.5
#   return y

# x1_fucionf1 = np.linspace(0, 50, 10)
# x2_fucionf1 = np.linspace(-50, 0, 10)
# print("x1_fucionf1")
# print(x1_fucionf1)
# print("x2_fucionf1")
# print(x2_fucionf1)

# y1 = f1(x1_fucionf1)
# y2 = f1(x2_fucionf1)
# print("y1")
# print(y1)
# print("y2")
# print(y2)


# # plt.figure(figsize=(15,5)) #Para cambiar el tamaño
# # plt.plot(x1_fucionf1,y1, color="blue",linestyle = "dotted")
# # plt.plot(x2_fucionf1,y2, color="green",linestyle = 'dashed')
# # plt.xlabel("x")
# # plt.ylabel("y")
# # plt.title("y(x)")
# # plt.legend(["x1","x2"])
# # plt.grid()
# # plt.show()


# x3_fucionf1 = np.linspace(-5, 5, 5)
# print("x3_funcionf1")
# print (x3_fucionf1)

# y3 = f1(x3_fucionf1)
# y4 = y3+100

# print("y3")
# print (y3)
# print("y4")
# print (y4)


# plt.figure(figsize=(15,5)) #Para cambiar el tamaño
# plt.plot(x3_fucionf1,y3, color="blue")
# plt.plot(x3_fucionf1,y4, color="green",linestyle = 'dashed')
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("y(x)")
# plt.legend(["y3","y4"])
# plt.grid()
# plt.show()

# La linea ptl.fill pinta el área entre las dos funciones

# plt.figure(figsize=(15,5)) #Para cambiar el tamaño
# plt.plot(x3_fucionf1,y3, color="blue",linestyle = 'dashed')
# plt.plot(x3_fucionf1,y4, color="green",linestyle = 'dashed')
# plt.fill_between(x3_fucionf1,y3, y4, alpha=.15, linewidth=0)
# plt.grid()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("y(x)")
# plt.legend(["y3","y4"])
# plt.show()





#import matplotlib.pyplot as plt
# x1=[1,2,3,4,5]
# y1=[1,2,3,4,5]
# plt.plot(x1,y1)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("y(x)")
# plt.show()


# x1=[1,2,3,4,5]
# y1=[1,2,2,2,3]
# plt.plot(x1,y1)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("y(x)")
# plt.show()


# x1=[1,2,5,7,10]
# y1=[1,3,6,7,20]
# plt.plot(x1,y1,linestyle = 'dashed') #linea discontinua
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("y(x)")
# plt.show()


# x1=[1,2,5,7,10]
# y1=[1,3,6,7,20]
# plt.plot(x1,y1,linestyle = 'dotted',color='red') #linea punteada y roja
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("y(x)")
# plt.show()


# x2=np.array([1,2,3,4,5,6,7,8,9,10])
# y2=x2*10+50           #primero multiplica todos los elementos por 10 y despues les suma 50
# plt.plot(x2,y2)
# plt.xlabel("x2")
# plt.ylabel("y2")
# plt.title("y2(x)")
# plt.show()



# x3=np.arange(-10,10)
# print(x3)
# y3=x3**2+5
# print(y3)
# plt.plot(x3,y3)
# plt.xlabel("x3")
# plt.ylabel("y3")
# plt.title("y3(x)")
# plt.show()


# x4=np.linspace(0, 5*np.pi, 100)
# y4=np.cos(x4)

# plt.plot(x4,y4)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("cos(x)")
# plt.show()


# x4=np.linspace(0, 5*np.pi, 100)
# y4=np.cos(x4)
# plt.figure(figsize=(20,5)) #Para cambiar el tamaño
# plt.plot(x4,y4)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("cos(x)")
# plt.legend(["coseno"])
# plt.show()


# x5=np.linspace(0, 5*np.pi, 10)
# y5_coseno = np.cos(x5)   
# y5_seno = np.sin(x5)

# plt.figure(figsize=(10,5)) #Para cambiar el tamaño
# plt.plot(x5,y5_coseno)
# plt.plot(x5,y5_seno)


# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("coseno(x) y seno(x)")
# plt.legend(["coseno","seno"])
# plt.show()
