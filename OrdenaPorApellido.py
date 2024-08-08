# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx", ordena
# el DataFrame por la columna "Nombre" y guarda el archivo modificado.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Ordenar el DataFrame por la columna "Nombre"
df = df.sort_values(by='ApellidoAlumno')

# Guardar el archivo modificado
df.to_excel('calificaciones_alumnos_modificado.xlsx', index=False)

print("Se ha ordenado el archivo por 'ApellidoAlumno' y se ha guardado el archivo modificado.")
