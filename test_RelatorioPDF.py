import unittest
from RelatorioPDF import RelatorioPDF
import os

class TestRelatorioPDF(unittest.TestCase):

    def test_gerar_relatorio(self):
        # Inicializa a classe
        relatorio = RelatorioPDF(
            salario_base=3000, 
            salario_bruto=3800, 
            salario_base_de_calculo=2500,
            anos_vigencia=['2021', '2022', '2023'],
            salario_liquido=3400, 
            irrf_recolhido=400, 
            aliquota=0.1,
            nome_contribuinte="Teste", 
            cpf_contribuinte="123.456.789-00"
        )

        # Chame o método gerarrelatorio
        relatorio.gerarrelatorio()

        # Verifique se o arquivo PDF foi criado
        nome_arquivo = "Relatório de desconto de Teste.pdf"
        self.assertTrue(os.path.isfile(nome_arquivo))

        # Limpeza: remova o arquivo PDF após o teste
        if os.path.isfile(nome_arquivo):
            os.remove(nome_arquivo)

    def test_gerar_relatorio_valores_extremos(self):
        relatorio = RelatorioPDF(
            salario_base=0, 
            salario_bruto=0, 
            salario_base_de_calculo=0,
            anos_vigencia=['2021'], 
            salario_liquido=0, 
            irrf_recolhido=0, 
            aliquota=0,
            nome_contribuinte="Extremo", 
            cpf_contribuinte="000.000.000-00"
        )

        # Chame o método gerarrelatorio
        relatorio.gerarrelatorio()

        # Verifique se o arquivo foi criado
        nome_arquivo = "Relatório de desconto de Extremo.pdf"
        self.assertTrue(os.path.isfile(nome_arquivo))

        # Limpeza
        if os.path.isfile(nome_arquivo):
            os.remove(nome_arquivo)

    def test_gerar_relatorio_periodo_longo(self):
        anos = [str(2000 + i) for i in range(50)]  # 50 anos de vigência
        relatorio = RelatorioPDF(
            salario_base=3000, 
            salario_bruto=5000, 
            salario_base_de_calculo=4000,
            anos_vigencia=anos, 
            salario_liquido=3500, 
            irrf_recolhido=500, 
            aliquota=0.125,
            nome_contribuinte="Longo Período", 
            cpf_contribuinte="987.654.321-00"
        )

        relatorio.gerarrelatorio()

        nome_arquivo = "Relatório de desconto de Longo Período.pdf"
        self.assertTrue(os.path.isfile(nome_arquivo))

        if os.path.isfile(nome_arquivo):
            os.remove(nome_arquivo)

    def test_gerar_relatorio_nome_com_caracteres_especiais(self):
        relatorio = RelatorioPDF(
            salario_base=3200, 
            salario_bruto=4000, 
            salario_base_de_calculo=3000,
            anos_vigencia=['2022', '2023'], 
            salario_liquido=2800, 
            irrf_recolhido=200, 
            aliquota=0.0667,
            nome_contribuinte="Téstê@123", 
            cpf_contribuinte="123.456.789-00"
        )

        relatorio.gerarrelatorio()

        nome_arquivo = "Relatório de desconto de Téstê@123.pdf"
        self.assertTrue(os.path.isfile(nome_arquivo))

        if os.path.isfile(nome_arquivo):
            os.remove(nome_arquivo)

    def test_gerar_relatorio_anos_invalidos(self):
        relatorio = RelatorioPDF(
            salario_base=3000, 
            salario_bruto=3500, 
            salario_base_de_calculo=2800,
            anos_vigencia=['202A', '20B2', '2023'], 
            salario_liquido=3100, 
            irrf_recolhido=400, 
            aliquota=0.1,
            nome_contribuinte="Teste Anos", 
            cpf_contribuinte="123.456.789-00"
        )

        relatorio.gerarrelatorio()

        nome_arquivo = "Relatório de desconto de Teste Anos.pdf"
        self.assertTrue(os.path.isfile(nome_arquivo))

        if os.path.isfile(nome_arquivo):
            os.remove(nome_arquivo)

    def test_gerar_relatorio_formatacao_cpf(self):
        relatorio = RelatorioPDF(
            salario_base=2800, 
            salario_bruto=3400, 
            salario_base_de_calculo=2900,
            anos_vigencia=['2021', '2022'], 
            salario_liquido=2500, 
            irrf_recolhido=400, 
            aliquota=0.1379,
            nome_contribuinte="CPF Formatado", 
            cpf_contribuinte="12345678900"  # CPF sem pontuação
        )

        relatorio.gerarrelatorio()

        nome_arquivo = "Relatório de desconto de CPF Formatado.pdf"
        self.assertTrue(os.path.isfile(nome_arquivo))

        if os.path.isfile(nome_arquivo):
            os.remove(nome_arquivo)

    def test_gerar_relatorio_minimo(self):
        relatorio = RelatorioPDF(
            salario_base=1000, 
            salario_bruto=1000, 
            salario_base_de_calculo=1000,
            anos_vigencia=['2021'], 
            salario_liquido=1000, 
            irrf_recolhido=0, 
            aliquota=0,
            nome_contribuinte="Simples", 
            cpf_contribuinte="111.222.333-44"
        )

        relatorio.gerarrelatorio()

        nome_arquivo = "Relatório de desconto de Simples.pdf"
        self.assertTrue(os.path.isfile(nome_arquivo))

        if os.path.isfile(nome_arquivo):
            os.remove(nome_arquivo)

if __name__ == '__main__':
    unittest.main()

