import pandas as pd
caminho_arquivo = "vendas_loja_roupas.xlsx"

df = pd.read_excel(caminho_arquivo)

print("Prévia de dados")
print(df.head())

df["Total da venda "] = df["Quantidade"] * df["Preço Unitário"]

print("\nInformações no dataframe: ")
print(df.info())

print("\nDados com a coluna Total de Venda: ")
print(df.head())