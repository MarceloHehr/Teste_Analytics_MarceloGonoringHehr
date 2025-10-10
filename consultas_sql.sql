-- Consulta 1: Listar o nome do produto, categoria e a soma total de vendas (Quantidade * Preço) para cada produto. Ordene o resultado pelo valor total de vendas em ordem decrescente.
-- Assumindo que a tabela se chama 'vendas' e contém as colunas 'Produto', 'Categoria', 'Quantidade', 'Preco'.

SELECT
    Produto_ID,
    Produto,
    Categoria,
    SUM(Quantidade * Preco) AS TotalVendasPorProduto
FROM
    vendas
GROUP BY
    Produto_ID, Produto, Categoria
ORDER BY
    TotalVendasPorProduto DESC;


-- Consulta 2: Identificar os produtos que venderam menos no mês de junho de 2023.
-- Nota: O dataset simulado é de 2023, então a consulta foi ajustada para 2023, não 2024 como no prompt original.
-- Assumindo que a tabela se chama 'vendas' e contém as colunas 'Data', 'Produto', 'Quantidade', 'Preco'.

SELECT
    Produto,
    SUM(Quantidade * Preco) AS TotalVendasJunho2023
FROM
    vendas
WHERE
    strftime('%Y-%m', Data) = '2023-06'
GROUP BY
    Produto
ORDER BY
    TotalVendasJunho2023 ASC
LIMIT 1;

