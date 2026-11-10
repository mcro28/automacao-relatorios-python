"""
Automação de Relatórios de Vendas
Projeto de portfólio - Python, utilizando apenas a biblioteca padrão.
"""

import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


CAMPOS_OBRIGATORIOS = {"data", "produto", "quantidade", "preco_unitario"}


def carregar_vendas(caminho_csv):
    """Lê um CSV e devolve uma lista de vendas validadas."""
    vendas = []
    caminho = Path(caminho_csv)

    with caminho.open("r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        if not leitor.fieldnames or not CAMPOS_OBRIGATORIOS.issubset(leitor.fieldnames):
            raise ValueError(
                "O CSV deve conter as colunas: data, produto, quantidade, preco_unitario."
            )

        for numero_linha, linha in enumerate(leitor, start=2):
            try:
                data = datetime.strptime(linha["data"], "%Y-%m-%d").date()
                produto = linha["produto"].strip()
                quantidade = int(linha["quantidade"])
                preco_unitario = float(linha["preco_unitario"])

                if not produto:
                    raise ValueError("produto vazio")
                if quantidade <= 0:
                    raise ValueError("quantidade deve ser maior que zero")
                if preco_unitario < 0:
                    raise ValueError("preço não pode ser negativo")

                vendas.append({
                    "data": data,
                    "produto": produto,
                    "quantidade": quantidade,
                    "preco_unitario": preco_unitario,
                    "total": quantidade * preco_unitario,
                })
            except (ValueError, TypeError, KeyError) as erro:
                raise ValueError(f"Erro na linha {numero_linha}: {erro}") from erro

    return vendas


def calcular_indicadores(vendas):
    """Calcula indicadores gerais e agrupamentos por produto e mês."""
    faturamento = sum(venda["total"] for venda in vendas)
    unidades = sum(venda["quantidade"] for venda in vendas)
    quantidade_vendas = len(vendas)

    por_produto = defaultdict(lambda: {"quantidade": 0, "faturamento": 0.0})
    por_mes = defaultdict(float)

    for venda in vendas:
        produto = venda["produto"]
        mes = venda["data"].strftime("%Y-%m")
        por_produto[produto]["quantidade"] += venda["quantidade"]
        por_produto[produto]["faturamento"] += venda["total"]
        por_mes[mes] += venda["total"]

    return {
        "faturamento_total": faturamento,
        "unidades_vendidas": unidades,
        "quantidade_vendas": quantidade_vendas,
        "ticket_medio": faturamento / quantidade_vendas if quantidade_vendas else 0.0,
        "por_produto": dict(por_produto),
        "por_mes": dict(sorted(por_mes.items())),
    }


def salvar_relatorios(indicadores, pasta_saida):
    """Gera arquivos CSV e TXT com os resultados da análise."""
    pasta = Path(pasta_saida)
    pasta.mkdir(parents=True, exist_ok=True)

    caminho_produtos = pasta / "resumo_por_produto.csv"
    with caminho_produtos.open("w", encoding="utf-8", newline="") as arquivo:
        campos = ["produto", "quantidade_vendida", "faturamento"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        for produto, dados in sorted(indicadores["por_produto"].items()):
            escritor.writerow({
                "produto": produto,
                "quantidade_vendida": dados["quantidade"],
                "faturamento": f'{dados["faturamento"]:.2f}',
            })

    caminho_mensal = pasta / "resumo_mensal.csv"
    with caminho_mensal.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["mes", "faturamento"])
        escritor.writeheader()
        for mes, valor in indicadores["por_mes"].items():
            escritor.writerow({"mes": mes, "faturamento": f"{valor:.2f}"})

    caminho_txt = pasta / "relatorio_geral.txt"
    with caminho_txt.open("w", encoding="utf-8") as arquivo:
        arquivo.write("RELATÓRIO DE VENDAS\n")
        arquivo.write("=" * 35 + "\n")
        arquivo.write(f'Quantidade de vendas: {indicadores["quantidade_vendas"]}\n')
        arquivo.write(f'Unidades vendidas: {indicadores["unidades_vendidas"]}\n')
        arquivo.write(f'Faturamento total: R$ {indicadores["faturamento_total"]:.2f}\n')
        arquivo.write(f'Ticket médio por registro: R$ {indicadores["ticket_medio"]:.2f}\n')
        arquivo.write("\nFATURAMENTO POR MÊS\n")
        for mes, valor in indicadores["por_mes"].items():
            arquivo.write(f"{mes}: R$ {valor:.2f}\n")

    return [caminho_produtos, caminho_mensal, caminho_txt]


def executar(caminho_entrada, pasta_saida):
    vendas = carregar_vendas(caminho_entrada)
    indicadores = calcular_indicadores(vendas)
    arquivos = salvar_relatorios(indicadores, pasta_saida)
    return indicadores, arquivos


if __name__ == "__main__":
    raiz = Path(__file__).resolve().parent.parent
    entrada = raiz / "dados" / "vendas_exemplo.csv"
    saida = raiz / "relatorios"

    try:
        indicadores, arquivos_gerados = executar(entrada, saida)
        print("Relatórios gerados com sucesso!")
        print(f'Faturamento total: R$ {indicadores["faturamento_total"]:.2f}')
        print("Arquivos:")
        for arquivo in arquivos_gerados:
            print(f"- {arquivo}")
    except (OSError, ValueError) as erro:
        print(f"Não foi possível gerar os relatórios: {erro}")
