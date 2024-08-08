# Este script encuentra la calificación mínima y máxima para cada materia y las muestra.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Encontrar la calificación mínima y máxima por materia
min_calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].min()
max_calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].max()

# Mostrar las calificaciones mínimas y máximas
print('Calificaciones Mínimas:')
print(min_calificaciones)
print('Calificaciones Máximas:')
print(max_calificaciones)
