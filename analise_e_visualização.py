import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset limpo
try:
    df = pd.read_csv("data_clean.csv")
except FileNotFoundError:
    print("Erro: O arquivo data_clean.csv não foi encontrado. Certifique-se de que o script simulate_and_clean_data.py foi executado primeiro.")
    exit()

# Converter a coluna 'Data' para datetime, se ainda não estiver
df["Data"] = pd.to_datetime(df["Data"])

# Calcular o total de vendas por produto (já feito no script anterior, mas repetido para garantir)
df["TotalVendas"] = df["Quantidade"] * df["Preço"]

# 1. Gráfico de linha mostrando a tendência de vendas ao longo do tempo (mensalmente)
print("Gerando gráfico de tendência de vendas mensais...")
df["MesAno"] = df["Data"].dt.to_period("M")
vendas_mensais = df.groupby("MesAno")["TotalVendas"].sum().reset_index()
vendas_mensais["MesAno"] = vendas_mensais["MesAno"].astype(str)

plt.figure(figsize=(12, 6))
sns.lineplot(x="MesAno", y="TotalVendas", data=vendas_mensais, marker="o")
plt.title("Tendência de Vendas Mensais (2023)")
plt.xlabel("Mês/Ano")
plt.ylabel("Total de Vendas")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("tendencia_vendas_mensais.png")
plt.close()
print("Gráfico 'tendencia_vendas_mensais.png' salvo.")

# 2. Identificar e descrever pelo menos dois padrões ou insights interessantes

# Insight 1: Vendas por Categoria
print("Gerando gráfico de vendas por categoria...")
vendas_por_categoria = df.groupby("Categoria")["TotalVendas"].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x="TotalVendas", y="Categoria", data=vendas_por_categoria, palette="viridis")
plt.title("Total de Vendas por Categoria")
plt.xlabel("Total de Vendas")
plt.ylabel("Categoria")
plt.tight_layout()
plt.savefig("vendas_por_categoria.png")
plt.close()
print("Gráfico 'vendas_por_categoria.png' salvo.")

# Insight 2: Distribuição de Preços dos Produtos
print("Gerando histograma de preços...")
plt.figure(figsize=(10, 6))
sns.histplot(df["Preço"], bins=15, kde=True)
plt.title("Distribuição de Preços dos Produtos")
plt.xlabel("Preço")
plt.ylabel("Frequência")
plt.tight_layout()
plt.savefig("distribuicao_precos.png")
plt.close()
print("Gráfico 'distribuicao_precos.png' salvo.")

print("Análises e visualizações concluídas.")
