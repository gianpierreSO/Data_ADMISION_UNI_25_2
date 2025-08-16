import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de resultados
url = "https://admision.uni.edu.pe/resultados-cepre-uni"

# Obtener HTML de la página
response = requests.get(url)
response.raise_for_status()

# Parsear con BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Buscar la tabla
tabla = soup.find("table")  # La página tiene una tabla de resultados

# Lista para guardar datos
datos = []

# Recorrer filas (saltando el encabezado)
for fila in tabla.find_all("tr")[1:]:
    columnas = fila.find_all("td")
    
    if len(columnas) >= 2:
        nombre = columnas[0].get_text(strip=True)
        puntaje = columnas[1].get_text(strip=True)
        carrera = columnas[2].get_text(strip=True) if len(columnas) > 2 else ""
        
        datos.append({
            "Nombre": nombre,
            "Puntaje": puntaje,
            "Carrera": carrera
        })

# Convertir a DataFrame
df = pd.DataFrame(datos)

# Guardar en CSV
df.to_csv("resultados_cepre_uni.csv", index=False, encoding="utf-8-sig")

print("CSV generado correctamente. Aquí algunos registros:")
print(df.head(10))
