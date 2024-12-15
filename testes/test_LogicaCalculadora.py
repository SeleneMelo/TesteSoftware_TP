import unittest
from LogicaCalculadora import LogicaCalculadora

class TestLogicaCalculadora(unittest.TestCase):

    def setUp(self):
        # Configuração comum para os testes
        self.calculadora = LogicaCalculadora(salario_base=3000, bonus_tempo=500, bonus_formacao=200, bonus_periculosidade=100,
                                             mes_inicio=1, ano_inicio=2022, mes_fim=12, ano_fim=2022,
                                             numero_dependentes=2, pensao_alimenticia=200, outros_descontos=50, tipooferta='CLT')

    def test_calculo_bonus_e_salario_bruto(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.assertEqual(self.calculadora.bonus, 800)
        self.assertEqual(self.calculadora.salario_bruto, 3800)

    def test_definir_anos_vigencia(self):
        self.calculadora.definir_anos_vigencia()
        self.assertEqual(self.calculadora.anos_vigencia, ['2022'])

    def test_preparar_graficos(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        graficos = self.calculadora.preparar_graficos(self.calculadora.salario_liquido, self.calculadora.irrf_recolhido,
                                                      self.calculadora.salario_base, (self.calculadora.bonus_tempo + self.calculadora.bonus_formacao + self.calculadora.bonus_periculosidade),
                                                      self.calculadora.salario_base_de_calculo, self.calculadora.total_deducoes)
        self.assertEqual(len(graficos), 6)

    def test_preparar_relatorio(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        relatorio = self.calculadora.preparar_relatorio(self.calculadora.salario_base, self.calculadora.salario_bruto,
                                                        self.calculadora.salario_base_de_calculo, self.calculadora.salario_liquido,
                                                        self.calculadora.irrf_recolhido)
        self.assertEqual(len(relatorio), 6)

    def test_enviardadosparagrafico(self):
        dados_grafico = self.calculadora.enviardadosparagrafico()
        self.assertEqual(len(dados_grafico), 7)

    def test_enviardadospararelatorio(self):
        dados_relatorio = self.calculadora.enviardadospararelatorio()
        self.assertEqual(len(dados_relatorio), 7)

    def test_bonus_zero(self):
        calculadora = LogicaCalculadora(salario_base=3000, bonus_tempo=0, bonus_formacao=0, bonus_periculosidade=0,
                                        mes_inicio=1, ano_inicio=2022, mes_fim=12, ano_fim=2022,
                                        numero_dependentes=2, pensao_alimenticia=200, outros_descontos=50, tipooferta='CLT')
        calculadora.calculo_bonus_e_salario_bruto()
        self.assertEqual(calculadora.bonus, 0)
        self.assertEqual(calculadora.salario_bruto, 3000)

    def test_dependentes_maximos(self):
        self.calculadora.numero_dependentes = 10
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        self.assertGreater(self.calculadora.salario_liquido, 0)

    def test_pensao_alta(self):
        self.calculadora.pensao_alimenticia = 2900
        self.calculadora.calculo_deducoes_e_salario_base()
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        self.assertGreaterEqual(self.calculadora.salario_liquido, 0)

    def test_periodo_invalido(self):
        self.calculadora.mes_inicio = 12
        self.calculadora.mes_fim = 1
        with self.assertRaises(ValueError):
            self.calculadora.definir_anos_vigencia()

    def test_tipooferta_invalido(self):
        self.calculadora.tipooferta = 'PJ'
        with self.assertRaises(ValueError):
            self.calculadora.calculo_bonus_e_salario_bruto()

    def test_bonus_negativo(self):
        self.calculadora.bonus_tempo = -500
        self.calculadora.bonus_formacao = -200
        self.calculadora.bonus_periculosidade = -100
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.assertEqual(self.calculadora.bonus, 0)
        self.assertEqual(self.calculadora.salario_bruto, self.calculadora.salario_base)

    def test_periodo_mesmo_ano(self):
        self.calculadora.mes_inicio = 6
        self.calculadora.ano_inicio = 2023
        self.calculadora.mes_fim = 6
        self.calculadora.ano_fim = 2023
        self.calculadora.definir_anos_vigencia()
        self.assertEqual(self.calculadora.anos_vigencia, ['2023'])

    def test_irrf_faixa_minima(self):
        self.calculadora.salario_base_de_calculo = 2112.00
        self.calculadora.salario_bruto = 3000
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        self.assertEqual(self.calculadora.irrf_recolhido, 0)
        self.assertEqual(self.calculadora.salario_liquido, 2112.00)
        self.assertEqual(self.calculadora.aliquota_, 0)

    def test_tipooferta_invalido_2(self):
        self.calculadora.tipooferta = 'PJ'
        with self.assertRaises(ValueError):
            self.calculadora.calculo_bonus_e_salario_bruto()

    def test_irrf_salario_extremo(self):
        self.calculadora.salario_base_de_calculo = 100000
        self.calculadora.salario_bruto = 120000
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        self.assertGreater(self.calculadora.irrf_recolhido, 20000)  # Cheque o valor aproximado
        self.assertGreater(self.calculadora.aliquota_, 0.2)  # Verifica se a alíquota é maior que 20%

    def test_periodo_ano_invalido(self):
        self.calculadora.ano_inicio = 2025
        self.calculadora.ano_fim = 2023
        with self.assertRaises(ValueError):
            self.calculadora.definir_anos_vigencia()

    def test_irrf_limite_superior(self):
        self.calculadora.salario_base_de_calculo = 4664.68
        self.calculadora.salario_bruto = 5000
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        self.assertAlmostEqual(self.calculadora.irrf_recolhido, 397.82, places=2)  
        self.assertAlmostEqual(self.calculadora.salario_liquido, 4266.86, places=2)  
        self.assertAlmostEqual(self.calculadora.aliquota_, 397.82 / 5000, places=2)  

    def test_irrf_faixa_isenta(self):
        self.calculadora.salario_base_de_calculo = 2100
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        self.assertEqual(self.calculadora.irrf_recolhido, 0)

    def test_bonus_zero(self):
        self.calculadora.bonus_tempo = 0
        self.calculadora.bonus_formacao = 0
        self.calculadora.bonus_periculosidade = 0
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.assertEqual(self.calculadora.bonus, 0)
        self.assertEqual(self.calculadora.salario_bruto, self.calculadora.salario_base)

    def test_anos_vigencia_multiplos_anos(self):
        self.calculadora.ano_inicio = 2020
        self.calculadora.ano_fim = 2023
        self.calculadora.definir_anos_vigencia()
        self.assertEqual(self.calculadora.anos_vigencia, ['2020', '2021', '2022', '2023'])

    def test_salario_liquido_com_descontos_altos(self):
        self.calculadora.salario_base_de_calculo = 3000
        self.calculadora.irrf_recolhido = 500
        self.calculadora.salario_liquido = self.calculadora.salario_base_de_calculo - self.calculadora.irrf_recolhido
        self.assertEqual(self.calculadora.salario_liquido, 2500)

    def test_periodo_invalido_mes_fim_menor_inicio(self):
        self.calculadora.mes_inicio = 12
        self.calculadora.mes_fim = 1
        with self.assertRaises(ValueError):
            self.calculadora.definir_anos_vigencia()

    def test_tipo_oferta_invalido(self):
        self.calculadora.tipooferta = 'FREELANCER'
        with self.assertRaises(ValueError):
            self.calculadora.calculo_bonus_e_salario_bruto()


if __name__ == '__main__':
    unittest.main()



