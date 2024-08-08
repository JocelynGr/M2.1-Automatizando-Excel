# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx" y calcula
# estadísticas básicas de los campos numéricos en el DataFrame resultante.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Calcular estadísticas básicas
estadisticas = df.describe()

# Imprimir estadísticas básicas
print(estadisticas)
