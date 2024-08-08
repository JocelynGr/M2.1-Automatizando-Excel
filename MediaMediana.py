# Este script genera un informe en Excel con estadísticas básicas (media, mediana, desviación estándar)
# para cada materia y guarda el informe como `informe_estadisticas.xlsx`.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Calcular estadísticas básicas por materia
estadisticas = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].describe()

# Guardar el informe en un nuevo archivo Excel
estadisticas.to_excel('informe_estadisticas.xlsx')
