import requests
import pandas as pd

url = "https://puntajes.admision.uni.edu.pe.deployedpe.com/api/pub_2025_2_dia1.json"

res = requests.get(url)
res.raise_for_status()

data = res.json()
df = pd.DataFrame(data)

print(df.head())

df.to_csv("resultados_dia1.csv", index=False, encoding="utf-8-sig")
print("Archivo guardado como resultados_dia1.csv")
