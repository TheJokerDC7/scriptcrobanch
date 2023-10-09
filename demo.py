import pandas as pd
import pingouin as pg

# Convertir respuestas en números
scale_likert = {'Siempre': 5, 'Casi Siempre': 4, 'Algunas Veces': 3, 'Casi nunca': 2, 'Nunca': 1}
scale_agreement = {'Totalmente de acuerdo': 5, 'De acuerdo': 4, 'Indiferente': 3, 'En desacuerdo': 2, 'Totalmente en desacuerdo': 1}

# Definir los datos para cada pregunta
questions_data = {
    'Pregunta1': [40, 60, 60, 1, 0],
    'Pregunta2': [50, 50, 60, 1, 0],
    'Pregunta3': [40, 70, 51, 0, 0],
    'Pregunta4': [51, 100, 10, 0, 0],
    'Pregunta5': [51, 100, 10, 0, 0],
    'Pregunta6': [50, 81, 30, 0, 0],
    'Pregunta7': [70, 40, 51, 0, 0],
    'Pregunta8': [61, 65, 35, 0, 0],
    'Pregunta9': [45, 55, 35,26, 0],
    'Pregunta10': [85, 52, 15, 9, 0],
    'Pregunta11': [40, 100, 21, 0, 0],
    'Pregunta12': [21, 120, 20, 0, 0],
    'Pregunta13': [50, 91, 20, 0, 0],
    'Pregunta14': [50, 80, 31, 0, 0],
    'Pregunta15': [20, 90, 51, 0, 0],
    'Pregunta16': [60, 90, 11, 0, 0],
    'Pregunta17': [40, 100, 21, 0, 0],
    'Pregunta18': [40, 100, 21, 0, 0],
    'Pregunta19': [30, 80, 51, 0, 0],
    'Pregunta20': [30, 80, 51, 0, 0],
    'Pregunta21': [40, 71, 50, 0, 0],
    'Pregunta22': [50, 100, 11, 0, 0],
    'Pregunta23': [70, 70, 21, 0, 0],
    'Pregunta24': [60, 80, 21, 0, 0],
    'Pregunta25': [80, 71, 10, 0, 0],
    'Pregunta26': [70, 80, 11, 0, 0],
    'Pregunta27': [80, 60, 21, 0, 0],
    'Pregunta28': [70, 50, 41, 0, 0],
    'Pregunta29': [70, 40, 51, 0, 0],
    'Pregunta30': [45, 55, 35, 26, 0]
}

# Función para expandir los datos basados en las frecuencias
def expand_data(data, scale):
    expanded = []
    for key, value in scale.items():
        expanded.extend([value] * data[key])
    return expanded

# Expandir todos los datos
expanded_data = {}
for question, frequencies in questions_data.items():
    if "Indiferente" in question:  # Usar escala de acuerdo
        expanded_data[question] = expand_data(dict(zip(scale_agreement.keys(), frequencies)), scale_agreement)
    else:  # Usar escala Likert
        expanded_data[question] = expand_data(dict(zip(scale_likert.keys(), frequencies)), scale_likert)

df_expanded = pd.DataFrame(expanded_data)

# Calcular el alfa de Cronbach para el conjunto completo de preguntas
alpha = pg.cronbach_alpha(df_expanded)[0]

print(f"Alfa de Cronbach para el conjunto de preguntas: {alpha:.2f}")

