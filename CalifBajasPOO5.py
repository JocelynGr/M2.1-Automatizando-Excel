# Este script encuentra a los alumnos con las 5 calificaciones más bajas en `Mat_ProgramacionOOP`
# y muestra sus nombres y calificaciones.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Encontrar los alumnos con las 5 calificaciones más bajas en Programación OOP
alumnos_bajas_programacion = df.nsmallest(5, 'Mat_ProgramacionOOP')

# Mostrar los nombres y las calificaciones de estos alumnos
print("Alumnos con las 5 calificaciones más bajas en Programación OOP:")
print(alumnos_bajas_programacion[['Nombre', 'Mat_ProgramacionOOP']])
