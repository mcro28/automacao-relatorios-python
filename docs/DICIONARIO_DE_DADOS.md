# Dicionário de dados

## Arquivo de entrada: `dados/vendas_exemplo.csv`

| Campo | Tipo lógico | Obrigatório | Regra |
|---|---|---:|---|
| data | Data | Sim | Formato AAAA-MM-DD |
| produto | Texto | Sim | Não pode estar vazio |
| quantidade | Inteiro | Sim | Maior que zero |
| preco_unitario | Decimal | Sim | Maior ou igual a zero |

## Arquivos de saída

### `resumo_por_produto.csv`

| Campo | Descrição |
|---|---|
| produto | Nome do produto |
| quantidade_vendida | Soma das unidades vendidas |
| faturamento | Soma dos totais dos registros do produto |

### `resumo_mensal.csv`

| Campo | Descrição |
|---|---|
| mes | Mês no formato AAAA-MM |
| faturamento | Soma do faturamento no mês |

### `relatorio_geral.txt`

Contém quantidade de registros, unidades vendidas, faturamento total, ticket médio por registro e faturamento agrupado por mês.
