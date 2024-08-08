# Este script filtra las filas del archivo Excel `calificaciones_alumnos.xlsx`
# donde la calificación en `Mat_CalculoIntegral` es mayor a 70 y
# muestra las filas resultantes, limitando las columnas mostradas a `Nombre` y `Mat_CalculoIntegral`.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Filtrar filas donde la calificación en Mat_CalculoIntegral es mayor a 70
df_filtrado = df[df['Mat_CalculoIntegral'] > 70]

# Seleccionar las columnas que se desean mostrar
df_filtrado = df_filtrado[['Nombre', 'Mat_CalculoIntegral']]

# Mostrar las filas filtradas
print(df_filtrado)
