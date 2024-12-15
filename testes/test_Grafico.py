import unittest
import os
import matplotlib.pyplot as plt
from Grafico import Grafico

class TestGrafico(unittest.TestCase):

    def setUp(self):

        self.grafico = Grafico(
            salario_liquido=[1000, 1200, 1500],
            irrf_recolhido=[50, 60, 75],
            anos_vigencia=[2021, 2022, 2023],
            numero_de_graficos=1,
            salario_base=[800, 1000, 1200],
            aditivos=[50, 20, 30],
            salario_base_de_calculo=[750, 900, 1100],
            deducoes=[20, 30, 40],
            nome_contribuinte="Teste"
        )

    def test_criar_grafico1(self):
        self.grafico.criargrafico1()
        self.assertTrue(os.path.isfile('Grafico 1 do contribuinte Teste.png'))

    def test_criar_grafico2(self):
        self.grafico.criargrafico2()
        self.assertTrue(os.path.isfile('Grafico 2 do contribuinte Teste.png'))

    def test_criar_grafico3(self):
        self.grafico.criargrafico3()
        self.assertTrue(os.path.isfile('grafico do contribuinte Teste.png'))



    def tearDown(self):
        # Limpar os arquivos de teste após os testes
        if os.path.isfile('Grafico 1 do contribuinte Teste.png'):
            os.remove('Grafico 1 do contribuinte Teste.png')
        if os.path.isfile('Grafico 2 do contribuinte Teste.png'):
            os.remove('Grafico 2 do contribuinte Teste.png')
        if os.path.isfile('grafico do contribuinte Teste.png'):
            os.remove('grafico do contribuinte Teste.png')


if __name__ == '__main__':
    unittest.main()
