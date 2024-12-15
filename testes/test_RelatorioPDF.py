import os
import matplotlib.pyplot as plt

import pytest

from RelatorioPDF import RelatorioPDF

# Fixture para limpar os arquivos gerados após cada teste
@pytest.fixture
def cleanup_files():
    arquivos_criados = []
    yield arquivos_criados
    for arquivo in arquivos_criados:
        if os.path.isfile(arquivo):
            os.remove(arquivo)

# Função auxiliar para adicionar arquivos para limpeza
def adicionar_arquivo_para_limpeza(arquivos_criados, nome_arquivo):
    arquivos_criados.append(nome_arquivo)

def test_gerar_relatorio(cleanup_files):
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

    nome_arquivo = "Relatório de desconto de Teste.pdf"
    relatorio.gerarrelatorio()
    adicionar_arquivo_para_limpeza(cleanup_files, nome_arquivo)
    assert os.path.isfile(nome_arquivo)

def test_gerar_relatorio_valores_extremos(cleanup_files):
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

    nome_arquivo = "Relatório de desconto de Extremo.pdf"
    relatorio.gerarrelatorio()
    adicionar_arquivo_para_limpeza(cleanup_files, nome_arquivo)
    assert os.path.isfile(nome_arquivo)

def test_gerar_relatorio_periodo_longo(cleanup_files):
    anos = [str(2000 + i) for i in range(50)]
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

    nome_arquivo = "Relatório de desconto de Longo Período.pdf"
    relatorio.gerarrelatorio()
    adicionar_arquivo_para_limpeza(cleanup_files, nome_arquivo)
    assert os.path.isfile(nome_arquivo)

def test_gerar_relatorio_nome_com_caracteres_especiais(cleanup_files):
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

    nome_arquivo = "Relatório de desconto de Téstê@123.pdf"
    relatorio.gerarrelatorio()
    adicionar_arquivo_para_limpeza(cleanup_files, nome_arquivo)
    assert os.path.isfile(nome_arquivo)

def test_gerar_relatorio_anos_invalidos(cleanup_files):
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

    nome_arquivo = "Relatório de desconto de Teste Anos.pdf"
    relatorio.gerarrelatorio()
    adicionar_arquivo_para_limpeza(cleanup_files, nome_arquivo)
    assert os.path.isfile(nome_arquivo)

def test_gerar_relatorio_formatacao_cpf(cleanup_files):
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

    nome_arquivo = "Relatório de desconto de CPF Formatado.pdf"
    relatorio.gerarrelatorio()
    adicionar_arquivo_para_limpeza(cleanup_files, nome_arquivo)
    assert os.path.isfile(nome_arquivo)

def test_gerar_relatorio_minimo(cleanup_files):
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

    nome_arquivo = "Relatório de desconto de Simples.pdf"
    relatorio.gerarrelatorio()
    adicionar_arquivo_para_limpeza(cleanup_files, nome_arquivo)
    assert os.path.isfile(nome_arquivo)


