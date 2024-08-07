# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx" y muestra
# las primeras 5 filas del DataFrame resultante.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Mostrar las primeras 5 filas
print(df.head())
