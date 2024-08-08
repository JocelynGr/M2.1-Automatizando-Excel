# Este script identifica a los alumnos que tienen una calificación perfecta (100) en cualquier materia y
# muestra sus nombres. Si no hay alumnos con calificación perfecta, muestra un mensaje indicando esto.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Identificar alumnos con calificaciones perfectas
alumnos_excelente = df[(df['Mat_CalculoIntegral'] == 100) | (df['Mat_ProgramacionOOP'] == 100) | (df['Mat_EstructuraDatos'] == 100)]

# Verificar si hay alumnos con calificaciones perfectas y mostrar el resultado
if not alumnos_excelente.empty:
    print("Alumnos con calificación perfecta:")
    print(alumnos_excelente['Nombre'])
else:
    print("No hay alumnos con calificación perfecta.")

