import requests
import pandas as pd

# URL directa al JSON (debes poner la ruta completa)
url = "https://puntajes.admision.uni.edu.pe.deployedpe.com/api/pub_2025_2_traslado.json"

# Obtener datos
response = requests.get(url)
data = response.json()

# Pasar a DataFrame
df = pd.DataFrame(data)

# Mostrar primeras filas
print(df.head())

# Guardar a CSV
df.to_csv("resultados_traslado.csv", index=False, encoding="utf-8-sig")
print("Archivo CSV guardado como resultados_traslado.csv")
