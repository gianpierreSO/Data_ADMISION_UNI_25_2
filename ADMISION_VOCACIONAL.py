import requests
from bs4 import BeautifulSoup
import csv

# 1. URL de la página
url = "https://admision.uni.edu.pe/resultados-vocacional"

# 2. Hacer la solicitud HTTP
response = requests.get(url)
response.encoding = "utf-8"  # Aseguramos que los acentos se lean bien

# 3. Parsear el HTML
soup = BeautifulSoup(response.text, "html.parser")

# 4. Buscar todas las filas de la tabla (<tr>)
rows = soup.find_all("tr")

# 5. Extraer nombre y puntaje
data = []
for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 2:  # Verificamos que haya al menos 2 columnas
        nombre = cols[0].get_text(strip=True)
        puntaje = cols[1].get_text(strip=True)
        data.append({
            "nombre": nombre,
            "puntaje": puntaje
        })

# 6. Mostrar resultados
for item in data:
    print(f"{item['nombre']} — {item['puntaje']}")

# Mostrar la cantidad total de filas (alumnos)
print(f"\nTotal de alumnos: {len(data)}")

# Opcional: Guardar en CSV
with open("resultados_vocacional.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre", "puntaje"])
    writer.writeheader()
    writer.writerows(data)

print("\nDatos guardados en resultados_vocacional.csv")
