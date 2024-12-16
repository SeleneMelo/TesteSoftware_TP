# -*- coding: utf-8 -*-
import os

class InterfaceVisual:
    def __init__(self):
        self.dados_salario = {}
        self.dados_periodo = {}
        self.dados_descontos = {}

    def coletar_dados_salario(self):
        print("=== Dados sobre o Salário ===")
        salario_base = input("Salário base: ").strip()
        bonus_tempo = input("Bonificação por tempo de serviço: ").strip()
        bonus_formacao = input("Bonificação por formação: ").strip()
        bonus_periculosidade = input("Adicional de periculosidade: ").strip()
        self.dados_salario = {
            "Salário Base": salario_base,
            "Bonificação por Tempo de Serviço": bonus_tempo,
            "Bonificação por Formação": bonus_formacao,
            "Adicional de Periculosidade": bonus_periculosidade,
        }

    def coletar_dados_periodo(self):
        print("\n=== Período de Cálculo ===")
        mes_inicio = input("Mês de início (MM): ").strip()
        ano_inicio = input("Ano de início (AAAA): ").strip()
        mes_fim = input("Mês de fim (MM): ").strip()
        ano_fim = input("Ano de fim (AAAA): ").strip()
        self.dados_periodo = {
            "Início": f"{mes_inicio}/{ano_inicio}",
            "Fim": f"{mes_fim}/{ano_fim}",
        }

    def coletar_dados_descontos(self):
        print("\n=== Descontos no Cálculo do IRRF ===")
        dependentes = input("Número de dependentes: ").strip()
        pensao_alimenticia = input("Pensão alimentícia: ").strip()
        outras_deducoes = input("Outras deduções: ").strip()
        self.dados_descontos = {
            "Dependentes": dependentes,
            "Pensão Alimentícia": pensao_alimenticia,
            "Outras Deduções": outras_deducoes,
        }

    def salvar_relatorio_em_arquivo(self):
        relatorio = "\n=== Relatório de Dados ===\n\n"
        relatorio += "=== Dados do Salário ===\n"
        for key, value in self.dados_salario.items():
            relatorio += f"{key}: {value}\n"

        relatorio += "\n=== Período de Cálculo ===\n"
        for key, value in self.dados_periodo.items():
            relatorio += f"{key}: {value}\n"

        relatorio += "\n=== Descontos no IRRF ===\n"
        for key, value in self.dados_descontos.items():
            relatorio += f"{key}: {value}\n"

        caminho = "relatorio_irrf.txt"
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(relatorio)

        print(f"\nRelatório salvo com sucesso no arquivo '{os.path.abspath(caminho)}'!")

    def menu_principal(self):
        while True:
            print("\n=== Calculadora de IRRF ===")
            print("1. Entrar com seus dados via terminal")
            print("2. Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.coletar_dados_salario()
                self.coletar_dados_periodo()
                self.coletar_dados_descontos()

                self.salvar_relatorio_em_arquivo()

            elif opcao == "2":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente!")
