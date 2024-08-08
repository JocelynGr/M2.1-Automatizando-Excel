# Este script añade una columna llamada `Rango_Calificacion` al archivo `calificaciones_alumnos.xlsx`,
# clasificando a los alumnos en 'Bajo', 'Medio' o 'Alto' según su promedio de calificaciones.
# El archivo modificado se guarda como `calificaciones_alumnos_rangos.xlsx`.

import pandas as pd

# Leer el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo)

# Calcular el promedio de las calificaciones
df['Promedio'] = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].mean(axis=1)

# Clasificar los rangos de calificación
def clasificar_rango(promedio):
    if promedio < 60:
        return 'Bajo'
    elif promedio < 80:
        return 'Medio'
    else:
        return 'Alto'

df['Rango_Calificacion'] = df['Promedio'].apply(clasificar_rango)

# Guardar el archivo modificado
df.to_excel('calificaciones_alumnos_rangos.xlsx', index=False)
