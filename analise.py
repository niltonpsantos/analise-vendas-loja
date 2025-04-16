import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar dados
df = pd.read_csv("analise.csv", encoding="latin1")

# 2. Ver as 5 primeiras linhas
print("Visualização inicial:")
print(df.head())

# 3. Criar coluna de Total da Venda
df["TotalVenda"] = df["Quantidade"] * df["PrecoUnitario"]

# 4. Vendas por produto
vendas_produto = df.groupby("Produto")["TotalVenda"].sum().sort_values(ascending=False)
print("\nTotal de vendas por produto:")
print(vendas_produto)

# 5. Vendas por loja
vendas_loja = df.groupby("Loja")["TotalVenda"].sum().sort_values(ascending=False)
print("\nTotal de vendas por loja:")
print(vendas_loja)

# 6. Gráfico de vendas por produto
plt.figure(figsize=(8, 4))
vendas_produto.plot(kind="bar", color="skyblue")
plt.title("Total de Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("R$ em vendas")
plt.tight_layout()
plt.savefig("grafico_produto.png")
plt.show()

# 7. Gráfico de vendas por loja
plt.figure(figsize=(6, 4))
vendas_loja.plot(kind="bar", color="lightgreen")
plt.title("Total de Vendas por Loja")
plt.xlabel("Loja")
plt.ylabel("R$ em vendas")
plt.tight_layout()
plt.savefig("grafico_loja.png")
plt.show()
