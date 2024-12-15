import pytest
import os
import matplotlib.pyplot as plt
from LogicaCalculadora import LogicaCalculadora

@pytest.fixture
def calculadora():
    return LogicaCalculadora(
        salario_base=3000,
        bonus_tempo=500,
        bonus_formacao=200,
        bonus_periculosidade=100,
        mes_inicio=1,
        ano_inicio=2022,
        mes_fim=12,
        ano_fim=2022,
        numero_dependentes=2,
        pensao_alimenticia=200,
        outros_descontos=50,
        tipooferta='CLT'
    )

def test_calculo_bonus_e_salario_bruto(calculadora):
    calculadora.calculo_bonus_e_salario_bruto()
    assert calculadora.bonus == 800
    assert calculadora.salario_bruto == 3800

def test_definir_anos_vigencia(calculadora):
    calculadora.definir_anos_vigencia()
    assert calculadora.anos_vigencia == ['2022']

def test_preparar_graficos(calculadora):
    calculadora.calculo_bonus_e_salario_bruto()
    calculadora.calculo_deducoes_e_salario_base()
    calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
    graficos = calculadora.preparar_graficos(
        calculadora.salario_liquido,
        calculadora.irrf_recolhido,
        calculadora.salario_base,
        calculadora.bonus_tempo + calculadora.bonus_formacao + calculadora.bonus_periculosidade,
        calculadora.salario_base_de_calculo,
        calculadora.total_deducoes
    )
    assert len(graficos) == 6

def test_preparar_relatorio(calculadora):
    calculadora.calculo_bonus_e_salario_bruto()
    calculadora.calculo_deducoes_e_salario_base()
    calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
    relatorio = calculadora.preparar_relatorio(
        calculadora.salario_base,
        calculadora.salario_bruto,
        calculadora.salario_base_de_calculo,
        calculadora.salario_liquido,
        calculadora.irrf_recolhido
    )
    assert len(relatorio) == 6

def test_enviardadosparagrafico(calculadora):
    dados_grafico = calculadora.enviardadosparagrafico()
    assert len(dados_grafico) == 7

def test_enviardadospararelatorio(calculadora):
    dados_relatorio = calculadora.enviardadospararelatorio()
    assert len(dados_relatorio) == 7

def test_bonus_zero():
    calculadora = LogicaCalculadora(
        salario_base=3000,
        bonus_tempo=0,
        bonus_formacao=0,
        bonus_periculosidade=0,
        mes_inicio=1,
        ano_inicio=2022,
        mes_fim=12,
        ano_fim=2022,
        numero_dependentes=2,
        pensao_alimenticia=200,
        outros_descontos=50,
        tipooferta='CLT'
    )
    calculadora.calculo_bonus_e_salario_bruto()
    assert calculadora.bonus == 0
    assert calculadora.salario_bruto == 3000

def test_dependentes_maximos(calculadora):
    calculadora.numero_dependentes = 10
    calculadora.calculo_bonus_e_salario_bruto()
    calculadora.calculo_deducoes_e_salario_base()
    calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
    assert calculadora.salario_liquido > 0

def test_pensao_alta(calculadora):
    calculadora.pensao_alimenticia = 2900
    calculadora.calculo_deducoes_e_salario_base()
    calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
    assert calculadora.salario_liquido >= 0

def test_periodo_invalido(calculadora):
    calculadora.mes_inicio = 12
    calculadora.mes_fim = 1
    with pytest.raises(ValueError):
        calculadora.definir_anos_vigencia()

def test_tipooferta_invalido(calculadora):
    calculadora.tipooferta = 'PJ'
    with pytest.raises(ValueError):
        calculadora.calculo_bonus_e_salario_bruto()

def test_bonus_negativo(calculadora):
    calculadora.bonus_tempo = -500
    calculadora.bonus_formacao = -200
    calculadora.bonus_periculosidade = -100
    calculadora.calculo_bonus_e_salario_bruto()
    assert calculadora.bonus == 0
    assert calculadora.salario_bruto == calculadora.salario_base

def test_periodo_mesmo_ano(calculadora):
    calculadora.mes_inicio = 6
    calculadora.ano_inicio = 2023
    calculadora.mes_fim = 6
    calculadora.ano_fim = 2023
    calculadora.definir_anos_vigencia()
    assert calculadora.anos_vigencia == ['2023']

def test_irrf_faixa_minima(calculadora):
    calculadora.salario_base_de_calculo = 2112.00
    calculadora.salario_bruto = 3000
    calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
    assert calculadora.irrf_recolhido == 0
    assert calculadora.salario_liquido == 2112.00
    assert calculadora.aliquota_ == 0

def test_irrf_salario_extremo(calculadora):
    calculadora.salario_base_de_calculo = 100000
    calculadora.salario_bruto = 120000
    calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
    assert calculadora.irrf_recolhido > 20000
    assert calculadora.aliquota_ > 0.2

def test_periodo_ano_invalido(calculadora):
    calculadora.ano_inicio = 2025
    calculadora.ano_fim = 2023
    with pytest.raises(ValueError):
        calculadora.definir_anos_vigencia()

def test_irrf_limite_superior(calculadora):
    calculadora.salario_base_de_calculo = 4664.68
    calculadora.salario_bruto = 5000
    calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
    assert pytest.approx(calculadora.irrf_recolhido, 0.01) == 397.82
    assert pytest.approx(calculadora.salario_liquido, 0.01) == 4266.86
    assert pytest.approx(calculadora.aliquota_, 0.01) == 397.82 / 5000

def test_irrf_faixa_isenta(calculadora):
    calculadora.salario_base_de_calculo = 2100
    calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
    assert calculadora.irrf_recolhido == 0

def test_anos_vigencia_multiplos_anos(calculadora):
    calculadora.ano_inicio = 2020
    calculadora.ano_fim = 2023
    calculadora.definir_anos_vigencia()
    assert calculadora.anos_vigencia == ['2020', '2021', '2022', '2023']

def test_salario_liquido_com_descontos_altos(calculadora):
    calculadora.salario_base_de_calculo = 3000
    calculadora.irrf_recolhido = 500
    calculadora.salario_liquido = calculadora.salario_base_de_calculo - calculadora.irrf_recolhido
    assert calculadora.salario_liquido == 2500



