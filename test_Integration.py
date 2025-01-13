import unittest
import os
from unittest.mock import patch
from Grafico import Grafico
from LogicaCalculadora import LogicaCalculadora
from Interface_Visual import InterfaceVisual

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.salario_base = 5000.0
        self.bonus_tempo = 1000.0
        self.bonus_formacao = 500.0
        self.bonus_periculosidade = 300.0
        self.dependentes = 2
        self.pensao_alimenticia = 200.0
        self.outros_descontos = 300.0
        self.tipooferta = "CLT"

        self.calculadora = LogicaCalculadora(
            salario_base=self.salario_base,
            bonus_tempo=self.bonus_tempo,
            bonus_formacao=self.bonus_formacao,
            bonus_periculosidade=self.bonus_periculosidade,
            mes_inicio=1,
            ano_inicio=2022,
            mes_fim=12,
            ano_fim=2023,
            numero_dependentes=self.dependentes,
            pensao_alimenticia=self.pensao_alimenticia,
            outros_descontos=self.outros_descontos,
            tipooferta=self.tipooferta,
        )

    def test_calculo_irrf_basico(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()

        self.assertGreater(self.calculadora.irrf_recolhido, 0)
        self.assertGreater(self.calculadora.salario_liquido, 0)

    def test_geracao_graficos(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()

        grafico = Grafico(
            salario_liquido=[self.calculadora.salario_liquido],
            irrf_recolhido=[self.calculadora.irrf_recolhido],
            anos_vigencia=["2022", "2023"],
            numero_de_graficos=2,
            salario_base=[self.calculadora.salario_base],
            aditivos=[self.bonus_tempo + self.bonus_formacao + self.bonus_periculosidade],
            salario_base_de_calculo=[self.calculadora.salario_base_de_calculo],
            deducoes=[self.calculadora.total_deducoes],
            nome_contribuinte="João Silva",
        )

        grafico.criargrafico1()
        grafico.criargrafico2()
        grafico.criargrafico3()

        self.assertTrue(os.path.exists('Grafico 1 do contribuinte João Silva.png'))
        self.assertTrue(os.path.exists('Grafico 2 do contribuinte João Silva.png'))
        self.assertTrue(os.path.exists('grafico do contribuinte João Silva.png'))

        os.remove('Grafico 1 do contribuinte João Silva.png')
        os.remove('Grafico 2 do contribuinte João Silva.png')
        os.remove('grafico do contribuinte João Silva.png')

    @patch("builtins.input", side_effect=["5000", "1000", "500", "300", "01", "2022", "12", "2023", "2", "200", "300"])
    def test_criacao_interface(self, mock_input):
        interface = InterfaceVisual()
        interface.coletar_dados_salario()
        interface.coletar_dados_periodo()
        interface.coletar_dados_descontos()

        self.assertEqual(interface.dados_salario["Salário Base"], "5000")
        self.assertEqual(interface.dados_periodo["Início"], "01/2022")
        self.assertEqual(interface.dados_descontos["Dependentes"], "2")

    def test_definir_anos_vigencia(self):
        self.calculadora.definir_anos_vigencia()
        self.assertEqual(self.calculadora.anos_vigencia, ['2022', '2023'])

    def test_geracao_relatorio(self):
        interface = InterfaceVisual()
        interface.dados_salario = {
            "Salário Base": "5000",
            "Bonificação por Tempo de Serviço": "1000",
            "Bonificação por Formação": "500",
            "Adicional de Periculosidade": "300",
        }
        interface.dados_periodo = {
            "Início": "01/2022",
            "Fim": "12/2023",
        }
        interface.dados_descontos = {
            "Dependentes": "2",
            "Pensão Alimentícia": "200",
            "Outras Deduções": "300",
        }

        interface.salvar_relatorio_em_arquivo()

        relatorio_path = "relatorio_irrf.txt"
        self.assertTrue(os.path.exists(relatorio_path))
        os.remove(relatorio_path)

    def test_salario_extremo(self):
        self.calculadora.salario_base = 1_000_000
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        self.assertGreater(self.calculadora.irrf_recolhido, 0)

    def test_tipo_oferta_invalido(self):
        self.calculadora.tipooferta = 'PJ'
        with self.assertRaises(ValueError):
            self.calculadora.calculo_bonus_e_salario_bruto()

    def test_dependentes_maximos(self):
        self.calculadora.numero_dependentes = 10
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        self.assertGreater(self.calculadora.salario_liquido, 0)

    def test_preparar_graficos(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        dados = self.calculadora.preparar_graficos(
            self.calculadora.salario_liquido,
            self.calculadora.irrf_recolhido,
            self.calculadora.salario_base,
            self.bonus_tempo + self.bonus_formacao + self.bonus_periculosidade,
            self.calculadora.salario_base_de_calculo,
            self.calculadora.total_deducoes,
        )
        self.assertEqual(len(dados), 6)

    def test_bonus_zero(self):
        self.calculadora.bonus_tempo = 0
        self.calculadora.bonus_formacao = 0
        self.calculadora.bonus_periculosidade = 0
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.assertEqual(self.calculadora.bonus, 0)

    def test_fluxo_completo(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()

        self.calculadora.definir_anos_vigencia()
        anos_vigencia = self.calculadora.anos_vigencia

        grafico = Grafico(
            salario_liquido=[3000, 3200],
            irrf_recolhido=[200, 250],
            anos_vigencia=anos_vigencia,
            numero_de_graficos=2,
            salario_base=[5000, 5200],
            aditivos=[1000, 1200],
            salario_base_de_calculo=[4000, 4200],
            deducoes=[500, 600],
            nome_contribuinte="Teste Completo",
        )

        grafico.criargrafico1()
        grafico.criargrafico2()
        grafico.criargrafico3()

        interface = InterfaceVisual()
        interface.salvar_relatorio_em_arquivo()

        self.assertTrue(os.path.exists("Grafico 1 do contribuinte Teste Completo.png"))
        self.assertTrue(os.path.exists("Grafico 2 do contribuinte Teste Completo.png"))
        self.assertTrue(os.path.exists("grafico do contribuinte Teste Completo.png"))
        self.assertTrue(os.path.exists("relatorio_irrf.txt"))

        os.remove("Grafico 1 do contribuinte Teste Completo.png")
        os.remove("Grafico 2 do contribuinte Teste Completo.png")
        os.remove("grafico do contribuinte Teste Completo.png")
        os.remove("relatorio_irrf.txt")

if __name__ == "__main__":
    unittest.main()
