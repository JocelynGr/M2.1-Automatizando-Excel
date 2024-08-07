# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx" que contiene
# las calificaciones de los alumnos en distintas materias. Luego, crea un gráfico
# de barras para cada alumno mostrando sus calificaciones en las materias
# Mat_CalculoIntegral, Mat_ProgramacionOOP y Mat_EstructuraDatos.
# El programa se asegura de que las etiquetas en el eje X no se encimen usando un
# ajuste automático.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Crear una lista de nombres de alumnos
alumnos = df['Nombre']

# Crear una matriz de calificaciones
calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']]

# Definir las etiquetas y la posición en el eje X
x = np.arange(len(alumnos))  # Posiciones en el eje X

# Configuración de la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Definir el ancho de las barras
width = 0.25

# Crear las barras para cada materia
rects1 = ax.bar(x - width, calificaciones['Mat_CalculoIntegral'], width, label='Cálculo Integral')
rects2 = ax.bar(x, calificaciones['Mat_ProgramacionOOP'], width, label='Programación OOP')
rects3 = ax.bar(x + width, calificaciones['Mat_EstructuraDatos'], width, label='Estructura de Datos')

# Añadir etiquetas y título
ax.set_xlabel('Alumnos')
ax.set_ylabel('Calificaciones')
ax.set_title('Calificaciones de Alumnos por Materia')
ax.set_xticks(x)
ax.set_xticklabels(alumnos, rotation=45, ha='right')
ax.legend()

# Ajustar el espaciado para que las etiquetas no se encimen
plt.tight_layout()

# Mostrar el gráfico
plt.show()
