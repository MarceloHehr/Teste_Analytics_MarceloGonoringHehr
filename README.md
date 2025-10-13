# Teste_Analytics_MarceloGonoringHehr
Como Executar os Scripts

Para executar os scripts e reproduzir as análises, siga os passos abaixo:

1.Clone o Repositório:


2.Crie e Ative um Ambiente Virtual


3.Instale as Dependências:


4.Execute o Script de Simulação e Limpeza de Dados: Este script irá gerar o arquivo data_clean.csv com exatamente 50 registros e Produto_IDs fixos.


5.Crie o Banco de Dados e Insira os Dados (SQLite): Este script irá criar um banco de dados SQLite (sales_database.db) e popular a tabela vendas com os dados limpos


6.Execute o Script de Análise e Visualização de Dados: Este script irá gerar os arquivos de imagem dos gráficos (.png).


7.Visualize as Consultas SQL e o Relatório de Insights: Os arquivos consultas_sql.sql e relatorio_insights.md podem ser abertos e visualizados diretamente com qualquer editor de texto.



Dependências Necessárias

Os scripts Python dependem das seguintes bibliotecas:

•pandas

•numpy

•matplotlib

•seaborn

•Todas podem ser instaladas via pip conforme o passo 3 acima.


Suposições Feitas

Durante a simulação dos dados, as seguintes suposições foram feitas:

•
Período dos Dados: Os dados de vendas foram simulados para o período de 01/01/2023 a 31/12/2023.

•
Nomes de Produtos e Categorias: Foram utilizadas classes Product com IDs fixos para cada tipo de produto, garantindo consistência e rastreabilidade. Os nomes e categorias são fixos (e.g., "Notebook", "Eletrônicos").

•
Quantidade de Registros: O dataset final data_clean.csv contém exatamente 50 registros únicos após a simulação e limpeza.

•
Valores Faltantes: Para simular dados "sujos", aproximadamente 5% dos valores de Quantidade e Preco foram definidos como NaN. No processo de limpeza, os NaNs em Quantidade foram preenchidos com 0 (indicando nenhuma venda), enquanto os NaNs em Preco foram preenchidos com a média da respectiva Categoria (ou média geral se a categoria fosse totalmente NaN). Para Produto e Categoria, NaNs foram preenchidos com "Desconhecido".

•
Cálculo de Vendas: O TotalVendas é calculado como Quantidade * Preco. Foi garantido que, se a Quantidade for 0, o TotalVendas também será 0. O preço do produto é fixo (base_price) e não possui variação aleatória.

•
Duplicatas: A introdução intencional de duplicatas foi removida para garantir que o número de registros gerados seja mais próximo do solicitado. A remoção de duplicatas ainda é realizada na função de limpeza, caso existam duplicatas orgânicas nos dados simulados.

•
Consultas SQL: As consultas SQL foram escritas assumindo que o dataset limpo (data_clean.csv) seria importado para um banco de dados relacional sob uma tabela chamada vendas. A consulta para o mês de junho foi ajustada para junho de 2023, pois o dataset simulado abrange apenas o ano de 2023, diferentemente do prompt original que mencionava 2024. O strftime foi usado para compatibilidade com SQLite, mas pode ser adaptado para outras sintaxes de banco de dados (e.g., EXTRACT(MONTH FROM Data) para PostgreSQL, MONTH(Data) para MySQL).

•
Criação do Banco de Dados: O script create_database.py cria um banco de dados SQLite (sales_database.db) e uma tabela vendas com base na estrutura do data_clean.csv.

