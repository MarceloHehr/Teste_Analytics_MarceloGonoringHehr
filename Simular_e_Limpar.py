import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class produtos():
    def __init__(self, id_prod, nome, categoria, preço):
        self.id_prod = id_prod
        self.nome = nome
        self.categoria = categoria
        self.preço = preço

    def __repr__(self):
        # Corrigindo a formatação da string f-string para evitar erros de sintaxe com aspas
        return f"Produto(id={self.id_prod}, nome='{self.nome}', categoria='{self.categoria}', preço={self.preço})"

# Lista fixa de produtos usando a classe Produto
Produtos = [
    produtos(1, "Notebook", "Eletrônicos", 800.00),
    produtos(2, "Smartphone", "Eletrônicos", 500.00),
    produtos(3, "Tablet", "Eletrônicos", 300.00),
    produtos(4, "Smartwatch", "Acessórios", 150.00),
    produtos(5, "Fone de Ouvido", "Acessórios", 80.00),
    produtos(6, "Teclado", "Periféricos", 60.00),
    produtos(7, "Mouse", "Periféricos", 30.00),
    produtos(8, "Monitor", "Informática", 250.00),
    produtos(9, "Webcam", "Informática", 70.00),
    produtos(10, "Roteador", "Informática", 90.00),
    produtos(11, "Impressora", "Informática", 180.00),
    produtos(12, "HD Externo", "Armazenamento", 120.00),
    produtos(13, "SSD Portátil", "Armazenamento", 200.00),
    produtos(14, "Câmera Digital", "Áudio e Vídeo", 350.00),
    produtos(15, "Caixa de Som", "Áudio e Vídeo", 100.00),
]



def geração_de_dados_das_vendas(num_minimo_vendas, id_inicial):
    data = []
    data_inicial = datetime(2023, 1, 1)
    data_final = datetime(2023, 12, 31)

    for i in range(id_inicial, id_inicial + num_minimo_vendas):
        data_registro = data_inicial + timedelta(days=random.randint(0, (data_final - data_inicial).days))

        produto_escolhido = random.choice(Produtos)
        id_prod = produto_escolhido.id_prod 
        nome = produto_escolhido.nome
        categoria = produto_escolhido.categoria
        quantidade = random.randint(1,2)

        preço = produto_escolhido.preço


        data.append(
             {
                  'ID_temporario':i,
                  'Data': data_registro.strftime('%Y-%m-%d'),
                  'ID do produto': id_prod,
                  'Produto': nome,
                  'Categoria':categoria,
                  'Quantidade': quantidade,
                  'Preço': preço

             }
        )
        df = pd.DataFrame(data)
        
        return df


def Limpeza_de_dados(df):
     df["Quantidade"].fillna(0, inplace = True)
     df["Preço"] = df.groupby("Categoria")["Preço"].transform(lambda x: x.fillna(x.mean()))
     df["Preço"].fillna(df["Preço"].mean(), inplace=True)
     df["Produto"].fillna('Desconhecido', inplace=True)
     df["Categoria"].fillna('Desconhecido', inplace=True)
     df.drop_duplicates(subset=['Data', 'ID do produto', 'Quantidade', 'Preço'], inplace=True)
     df["Data"] = pd.to_datetime(df["Data"])
     df["Quantidade"] = df["Quantidade"].astype(int)
     df["Preço"] = df["Preço"].astype(float)

     return df


if __name__ == "__main__":
     registros_min=50
     todos_registros = pd.DataFrame()
     id_vendas_geradas = 1


     print("Simulando dataset de vendas...")
     tamanho_lote = registros_min*5

     while len(todos_registros) < registros_min:
          lote_df=geração_de_dados_das_vendas(tamanho_lote, id_vendas_geradas)
          id_vendas_geradas += tamanho_lote

          limpar_lote_df  = Limpeza_de_dados(lote_df.copy())


          todos_registros = pd.concat([todos_registros, limpar_lote_df], ignore_index=True)
          todos_registros.drop_duplicates(subset=["Data", "ID do produto", "Quantidade", "Preço"], inplace=True)

          print(f"Registros únicos de vendas gerados até agora: {len(todos_registros)}")
     df_limpo = todos_registros.head(registros_min).copy()
     df_limpo['ID'] = range(1, registros_min + 1) # Redefinir IDs de venda de 1 a 50
     df_limpo.drop(columns=['ID_temporario'], inplace=True, errors='ignore') # Remover o ID temporário da venda
     cols = ['ID', 'ID do produto', 'Data', 'Produto', 'Categoria', 'Quantidade', 'Preço']
     df_limpo= df_limpo[cols]

     print("Dataset limpo (primeiras 5 linhas):")
     print(df_limpo.head())
     print("\nInformações do dataset (depois da limpeza):")
     print(df_limpo.info())

     print(f"\nVERIFICAÇÃO: O dataset limpo tem {len(df_limpo)} registros.")
     assert len(df_limpo) == registros_min, f"Erro: O dataset limpo não tem {registros_min} registros. Encontrado: {len(df_limpo)}"

     caminho_output = 'data_clean.csv'
     df_limpo.to_csv(caminho_output, index=False)
     print(f"\nDataset limpo salvo em {caminho_output}")


     df_limpo['TotalVendas'] = df_limpo['Quantidade'] * df_limpo['Preço']


     zero_vendas = df_limpo[df_limpo['Quantidade'] == 0]
     if not zero_vendas.empty:
        print("\nVERIFICAÇÃO: Registros com Quantidade 0 e seus TotalVendas:")
        print(zero_vendas[['Produto', 'Quantidade', 'Preço', 'TotalVendas']].head())
        assert (zero_vendas['TotalVendas'] == 0).all(), "Erro: Produtos com Quantidade 0 possuem TotalVendas diferente de 0."
     else:
        print("\nVERIFICAÇÃO: Nenhum registro com Quantidade 0 encontrado (o que é esperado se todos os registros gerados tiverem quantidade > 0 e nenhum NaN foi introduzido para quantidade).")

     vendas_por_produto = df_limpo.groupby('Produto')['TotalVendas'].sum().reset_index()
     vendas_por_produto = vendas_por_produto.sort_values(by='TotalVendas', ascending=False)
     print("\nTotal de vendas por produto:")
     print(vendas_por_produto.head())

     produto_mais_vendido = vendas_por_produto.iloc[0]
     print(f"\nProduto com o maior número de vendas totais: {produto_mais_vendido['Produto']} com R$ {produto_mais_vendido['TotalVendas']:.2f}")



     

