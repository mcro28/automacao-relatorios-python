import tempfile
import unittest
from pathlib import Path

from src.relatorios import carregar_vendas, calcular_indicadores, salvar_relatorios


class TestRelatorios(unittest.TestCase):
    def test_calculo_indicadores(self):
        vendas = [
            {"data": __import__("datetime").date(2026, 1, 10),
             "produto": "Teclado", "quantidade": 2,
             "preco_unitario": 50.0, "total": 100.0},
            {"data": __import__("datetime").date(2026, 1, 11),
             "produto": "Mouse", "quantidade": 1,
             "preco_unitario": 30.0, "total": 30.0},
        ]
        resultado = calcular_indicadores(vendas)
        self.assertEqual(resultado["faturamento_total"], 130.0)
        self.assertEqual(resultado["unidades_vendidas"], 3)
        self.assertEqual(resultado["quantidade_vendas"], 2)

    def test_csv_com_colunas_invalidas(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = Path(pasta) / "invalido.csv"
            arquivo.write_text("nome,valor\nTeste,10\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                carregar_vendas(arquivo)

    def test_gera_arquivos(self):
        indicadores = calcular_indicadores([])
        with tempfile.TemporaryDirectory() as pasta:
            caminhos = salvar_relatorios(indicadores, pasta)
            self.assertEqual(len(caminhos), 3)
            self.assertTrue(all(caminho.exists() for caminho in caminhos))


if __name__ == "__main__":
    unittest.main()
