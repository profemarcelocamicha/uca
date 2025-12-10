# pip install pandas

# *******************************************************************
# Series (pd.Series)
import pandas as pd
import matplotlib.pyplot as plt

archivo="c:/uca/datos.csv"

ds_acciones = pd.read_csv(archivo)

print(ds_acciones.shape) #(100, 13) 100 filas, 13 columnas

print(ds_acciones.columns)
columnas = ds_acciones.columns.to_list()
print(columnas)

print(ds_acciones.head())
print(ds_acciones.tail())
print(ds_acciones.sample())
print(ds_acciones.sample(10))

print(ds_acciones.iloc[0])
print(ds_acciones.iloc[0:5])

print(ds_acciones.loc[3,"Edad"])

print(ds_acciones.loc[3,["Edad","Nombre"]])

print(ds_acciones.loc[1:3,["Edad","Nombre"]])

print(ds_acciones[["Edad","Nombre"]])

print(ds_acciones["Apellido"])
print(ds_acciones["Apellido"]=="Molina")
print(ds_acciones.loc[ds_acciones["Apellido"]=="Molina"])
print(ds_acciones.loc[ds_acciones["Apellido"]=="Molina",["Nombre","Edad"]])

cond1 = ds_acciones["Apellido"]=="Molina"
ds_filtro1 = ds_acciones.loc[cond1,["Nombre","Edad"]]
print(ds_filtro1)

cond2 = ds_acciones["Edad"]>=95
ds_filtro2 = ds_acciones.loc[cond2,["Nombre","Apellido"]]
cant_filas_filtro2 = ds_filtro2.shape[0]
print("Cantidad de filas con Edad>=95:",cant_filas_filtro2)






"""
s = pd.Series([10, 20, 40], index=['a', 'b', 'c'])
print(s)

# *******************************************************************
# DataFrames (pd.DataFrame)
data = {
    'Nombre': ['Ana', 'Luis', 'María'],
    'Edad': [25, 30, 22]
}
df = pd.DataFrame(data)
print(df)

# *******************************************************************
# Lectura y escritura de archivos
df = pd.read_csv('datos.csv')        # Leer CSV
df.to_excel('salida.xlsx')           # Guardar en Excel
df.to_json('datos.json')             # Guardar en JSON


# *******************************************************************
# Algunas operaciones comunes
df.head()                   # Primeras filas
df.describe()               # Estadísticas básicas
df['Edad'].mean()          # Promedio de una columna
df[df['Edad'] > 25]        # Filtrado de filas
df.sort_values('Edad')     # Ordenar por una columna
df.groupby('Nombre').sum() # Agrupar por nombre

print("primeras filas")
print(df.head())
print("primeras y ultimas filas")
print(df.describe)
print("promedio de edad")
print(df['Edad'].mean() )
print("filtrado de edad")
print(df['Edad']>25 )
print("ordenado por edad")
print(df.sort_values('Edad'))
print("agrupado por nombre")
print(df.groupby('Nombre').sum())

# *******************************************************************
print("shape")
print(df.shape)

print("# filas")
print(df.shape[0])

print("# columnas")
print(df.shape[1])

cant_filas , cant_columnas = df.shape

print("Cantidad de filas:" , cant_filas)
print("Cantidad de columnas:" ,cant_columnas)

# *******************************************************************
print("Lista de columnas:")
print(df.columns.to_list())
print("\n")

print("head")
print(df.head)
print("\n")

print("tail")
print(df.tail)
print("\n")

print("sample")
print(df.sample)
print("\n")

print("Sample of 10")
print(df.sample(10))
print("\n")

print("iloc 0")
print(df.iloc[0])
print("iloc 1")
print(df.iloc[1])
print("\n")

print("iloc Filas 0:3, columna 0")
print(df.iloc[0, 0])
print(df.iloc[1, 0])
print(df.iloc[2, 0])
print(df.iloc[3, 0])
print("\n")

print("iloc de fila 0 a 2 y de columna 0 a 5")
print(df.iloc[0:2, 0:5])
print("\n")


# df.iloc[0]           # Primera fila completa
# df.iloc[1, 0]        # Fila 1, columna 0 → 'Luis'
# df.iloc[:, 1]        # Todas las filas, columna 1 (Edad)
# df.iloc[0:2, 0:2]    # Filas 0 y 1, columnas 0 y 1
# df.iloc[-1]          # Última fila

# *******************************************************************

print("loc por Nombre")
print(df.loc[1, 'Nombre'])    # Accede por etiqueta
print("\n")

print("loc por Nombre y Edad")
print(df.loc[1,["Nombre","Edad"]])
print("\n")

print("loc por Nombre y Edad - filas 0:3")
print(df.loc[0:3,["Nombre","Edad"]])
print("\n")

print("imprime todos los nombres con sus edades")
print(df[["Nombre","Edad"]])
print("\n")

print("imprime todos los nombres")
print(df["Nombre"])
print("\n")

print("Filtra todos los nombres Sofía")
print(df["Nombre"]=="Sofía")
print("\n")

print("nombres Sofía")
print(df.loc[df["Nombre"]=="Sofía"])
print("\n")

print("nombres Sofía")
print(df.loc[df["Nombre"]=="Sofía"])
print("\n")

print("nombres Sofía, Edad, Apellido")
print(df.loc[df["Nombre"]=="Sofía",["Edad","Apellido"]])
print("\n")


print("nombres Sofía, Edad, DNI")
cond1=df["Nombre"]=="Sofía"
df_filtro1=df.loc[cond1,["Edad","DNI"]]
print(df_filtro1)



cond2=df["Edad"]>=19
df_filtro2 = df.loc[cond2,["Nombre","Apellido"]]
cant_filas_filtro2=df_filtro2.shape[0]
print("Cantidad de filas con Edade>=19:",cant_filas_filtro2)



# filtro_tsla=df["Nombre"]=="Sofía"

filtro_tsla=df["Nombre"]=="Sofía"
ds_acciones_tsla=df.loc[filtro_tsla,["Edad","Apellido"]]

plt.figure(figsize=(20,6))

plt.plot(df.Edad, df.Apellido)

plt.rc('xtick', labelsize=10)
plt.title("Precio de cierre de los últimos 60 días")
plt.ylabel('Precio de cierre')  # Leyenda en el eje y
plt.xticks(rotation=90)
plt.xlabel('Fecha')  # Leyenda en el eje x

plt.show()


"""
