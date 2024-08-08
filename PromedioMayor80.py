# Este script filtra y muestra los nombres de los alumnos que tienen un promedio mayor a 80.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Calcular el promedio de las calificaciones
df['Promedio'] = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].mean(axis=1)

# Filtrar alumnos con promedio mayor a 80
alumnos_promedio_alto = df[df['Promedio'] > 80]

# Mostrar los nombres de los alumnos con promedio mayor a 80
print(alumnos_promedio_alto['Nombre'])
