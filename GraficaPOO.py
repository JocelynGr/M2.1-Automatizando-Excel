# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx" y crea un
# gráfico de barras con las calificaciones en "Mat_ProgramacionOOP".

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df['Nombre'], df['Mat_ProgramacionOOP'])
plt.xlabel('Nombre')
plt.ylabel('Calificación Programación OOP')
plt.title('Calificaciones en Programación OOP')
plt.xticks(rotation=90)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
