# Este script cuenta cuántos alumnos aprobaron cada materia (calificación >= 70) y muestra el conteo.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Contar cuántos alumnos aprobaron cada materia
aprobados_calculo = df[df['Mat_CalculoIntegral'] >= 70].shape[0]
aprobados_programacion = df[df['Mat_ProgramacionOOP'] >= 70].shape[0]
aprobados_estructuras = df[df['Mat_EstructuraDatos'] >= 70].shape[0]

# Mostrar el conteo de aprobados por materia
print(f'Alumnos aprobados en Calculo Integral: {aprobados_calculo}')
print(f'Alumnos aprobados en Programación OOP: {aprobados_programacion}')
print(f'Alumnos aprobados en Estructura de Datos: {aprobados_estructuras}')
