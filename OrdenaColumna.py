# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx" que contiene
# las calificaciones de los alumnos en distintas materias. Luego, agrega una columna
# llamada "Mat_Fisica" con valores aleatorios entre 0 y 100 con un decimal, ordena
# la tabla por el campo "Nombre" y guarda el archivo modificado.

import pandas as pd
import numpy as np

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Generar valores aleatorios entre 0 y 100 con un decimal para la nueva columna "Mat_Fisica"
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, df.shape[0]), 1)

# Ordenar el DataFrame por la columna "Nombre"
df = df.sort_values(by='Nombre')

# Guardar el DataFrame modificado en un nuevo archivo Excel
df.to_excel('calificaciones_alumnos_modificado.xlsx', index=False)

print("Se ha agregado la columna 'Mat_Fisica' con valores aleatorios, se ha ordenado por 'Nombre' y se ha guardado el archivo modificado.")
