import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar datos
df = pd.read_csv("gastos.csv", parse_dates=["fecha"])
df = df.drop_duplicates()

# 2. Análisis en consola
print("Total gastado:", df["monto"].sum())
print("\nPor categoría:")
print(df.groupby("categoria")["monto"].sum().sort_values(ascending=False))
print("\nTop 3 gastos más grandes:")
print(df.nlargest(3, "monto")[["fecha", "descripcion", "monto"]])

# 3. Gráfico por categoría
por_categoria = df.groupby("categoria")["monto"].sum().sort_values(ascending=False)
por_categoria.plot(kind="bar", title="Gastos por categoría")
plt.ylabel("Monto ($)")
plt.tight_layout()
plt.show()

