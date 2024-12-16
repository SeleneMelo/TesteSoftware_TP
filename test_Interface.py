import unittest
from unittest.mock import patch
import os
from Interface_Visual import InterfaceVisual


class TestInterfaceVisual(unittest.TestCase):

    def setUp(self):
        # Cria uma instância da classe InterfaceVisual para os testes
        self.interface = InterfaceVisual()

    @patch('builtins.input', side_effect=['3000', '500', '200', '100'])  # Mock para coletar dados de salário
    def test_coletar_dados_salario(self, mock_input):
        # Testa a função coletar_dados_salario
        self.interface.coletar_dados_salario()

        # Verifica se os dados coletados são corretos
        self.assertEqual(self.interface.dados_salario, {
            "Salário Base": '3000',
            "Bonificação por Tempo de Serviço": '500',
            "Bonificação por Formação": '200',
            "Adicional de Periculosidade": '100',
        })

    @patch('builtins.input', side_effect=['01', '2022', '12', '2022'])  # Mock para coletar dados de período
    def test_coletar_dados_periodo(self, mock_input):
        # Testa a função coletar_dados_periodo
        self.interface.coletar_dados_periodo()

        # Verifica se o período foi coletado corretamente
        self.assertEqual(self.interface.dados_periodo, {
            "Início": '01/2022',
            "Fim": '12/2022',
        })

    @patch('builtins.input', side_effect=['2', '1000', '300'])  # Mock para coletar dados de descontos
    def test_coletar_dados_descontos(self, mock_input):
        # Testa a função coletar_dados_descontos
        self.interface.coletar_dados_descontos()

        # Verifica se os dados coletados estão corretos
        self.assertEqual(self.interface.dados_descontos, {
            "Dependentes": '2',
            "Pensão Alimentícia": '1000',
            "Outras Deduções": '300',
        })

    


if __name__ == '__main__':
    unittest.main()
