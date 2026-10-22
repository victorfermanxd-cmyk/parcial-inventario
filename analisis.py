"""
Análisis exploratorio del inventario con Pandas.
Ejecutar: python analisis.py
"""
import pandas as pd

df = pd.read_csv("datos.csv")

print("\n=== PRIMERAS FILAS ===")
print(df.head())
print("\n=== ESTRUCTURA Y TIPOS DE DATOS ===")
df.info()
print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(df.describe(include="all"))
print("\n=== VALORES FALTANTES POR COLUMNA ===")
print(df.isnull().sum())
print("\n=== PRODUCTOS POR SUCURSAL ===")
print(df.groupby("Sucursal")["ID_Producto"].count().sort_values(ascending=False))
print("\n=== UNIDADES Y VALOR POR SUCURSAL ===")
resumen = df.groupby("Sucursal").agg(
    Unidades=("Cantidad", "sum"),
    Valor_USD=("Valor_Inventario_USD", "sum"),
    Productos=("ID_Producto", "count")
).sort_values("Valor_USD", ascending=False)
print(resumen.round(2))
print("\n=== VALOR POR CATEGORÍA ===")
print(df.groupby("Categoria")["Valor_Inventario_USD"].sum().sort_values(ascending=False).round(2))
