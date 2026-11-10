# Automação de Relatórios de Vendas

Projeto de portfólio desenvolvido em Python básico, com foco na leitura, validação e análise de dados de vendas em arquivos CSV. Utiliza somente a biblioteca padrão do Python, sem dependências externas.

## Objetivo

Automatizar a consolidação de registros de vendas e gerar relatórios com indicadores gerais, desempenho por produto e faturamento mensal.

## Funcionalidades

- Importação de dados de um arquivo CSV.
- Validação de colunas, datas, quantidades, preços e nomes de produtos.
- Cálculo do faturamento total, unidades vendidas e ticket médio por registro.
- Agrupamento de faturamento por produto e por mês.
- Geração de dois relatórios CSV e um relatório TXT.
- Testes automatizados básicos.

## Tecnologias

- Python 3.10 ou superior (não utiliza recursos exclusivos dessa versão).
- Biblioteca padrão: `csv`, `collections`, `datetime`, `pathlib` e `unittest`.
- Git e GitHub para versionamento.

## Estrutura

```text
automacao-relatorios-python/
├── dados/
│   └── vendas_exemplo.csv
├── docs/
│   ├── DOCUMENTACAO_TECNICA.md
│   └── DICIONARIO_DE_DADOS.md
├── relatorios/
│   └── (arquivos gerados na execução)
├── src/
│   └── relatorios.py
├── tests/
│   └── test_relatorios.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar no IntelliJ IDEA

1. Instale o Python 3 e o plugin Python do IntelliJ IDEA, se necessário e disponível na sua edição.
2. Abra a pasta do projeto no IntelliJ.
3. Configure o interpretador Python do projeto.
4. Abra o terminal integrado e execute:

```bash
python src/relatorios.py
```

No Windows, caso o comando `python` não funcione, tente `py src/relatorios.py`.

Os relatórios serão criados na pasta `relatorios/`.

## Como executar os testes

Na raiz do projeto:

```bash
python -m unittest discover -s tests -v
```

## Formato do arquivo de entrada

O arquivo CSV deve utilizar cabeçalho e conter as colunas:

| Coluna | Tipo esperado | Exemplo |
|---|---|---|
| data | AAAA-MM-DD | 2026-01-05 |
| produto | Texto | Teclado |
| quantidade | Inteiro positivo | 2 |
| preco_unitario | Número decimal | 89.90 |

Use ponto como separador decimal. O programa interrompe o processamento e informa a linha quando encontra um registro inválido.

## Saídas geradas

- `relatorios/relatorio_geral.txt`: indicadores consolidados.
- `relatorios/resumo_por_produto.csv`: unidades e faturamento por produto.
- `relatorios/resumo_mensal.csv`: faturamento por mês.

## Escopo e limitações

Esta versão é uma aplicação local e didática. Não possui interface gráfica, autenticação, integração bancária ou conexão com banco de dados. O ticket médio é calculado por registro de venda, pois o CSV de exemplo não possui identificador de pedido. Essas funcionalidades podem ser consideradas em versões futuras.

## Próximas melhorias

- Adicionar identificador de pedido para calcular ticket médio por pedido.
- Permitir informar os caminhos de entrada e saída pela linha de comando.
- Persistir os dados em MySQL.
- Criar gráficos e exportação para Excel.
- Adicionar logs e relatórios de erros sem interromper toda a importação.

## Autor

Maria Clara Rodrigues de Oliveira, https://github.com/mcro28.