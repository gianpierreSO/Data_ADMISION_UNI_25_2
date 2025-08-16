import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de resultados para Juliaca
url = "https://admision.uni.edu.pe/resultados-cepre-uni"
response = requests.get(url)
response.raise_for_status()

# Parsear el contenido HTML
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar la tabla correspondiente a Juliaca
tabla_juliaca = soup.find_all("table")[1]  # La segunda tabla corresponde a Juliaca

# Lista para almacenar los datos
datos_juliaca = []

# Recorrer las filas de la tabla
for fila in tabla_juliaca.find_all("tr")[1:]:  # Saltar el encabezado
    columnas = fila.find_all("td")
    if len(columnas) >= 3:
        nombre = columnas[0].get_text(strip=True)
        puntaje = columnas[1].get_text(strip=True)
        especialidad = columnas[2].get_text(strip=True)
        datos_juliaca.append({
            "Nombre": nombre,
            "Puntaje": puntaje,
            "Especialidad": especialidad
        })

# Crear un DataFrame con los datos
df_juliaca = pd.DataFrame(datos_juliaca)

# Guardar el DataFrame en un archivo CSV
df_juliaca.to_csv("resultados_cepre_uni_juliaca.csv", index=False, encoding="utf-8-sig")

# Mostrar los primeros registros
print(df_juliaca.head(10))
