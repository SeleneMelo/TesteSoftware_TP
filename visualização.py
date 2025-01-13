import tkinter as tk
from tkinter import messagebox
from LogicaCalculadora import LogicaCalculadora
from Grafico import Grafico

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora IRRF")
        
        # Criação de widgets para os inputs do usuário
        tk.Label(root, text="Salário Base:").grid(row=0, column=0, sticky="w")
        self.salario_base = tk.Entry(root)
        self.salario_base.grid(row=0, column=1)

        tk.Label(root, text="Bonificação por Tempo de Serviço:").grid(row=1, column=0, sticky="w")
        self.bonus_tempo = tk.Entry(root)
        self.bonus_tempo.grid(row=1, column=1)

        tk.Label(root, text="Bonificação por Formação:").grid(row=2, column=0, sticky="w")
        self.bonus_formacao = tk.Entry(root)
        self.bonus_formacao.grid(row=2, column=1)

        tk.Label(root, text="Adicional de Periculosidade:").grid(row=3, column=0, sticky="w")
        self.bonus_periculosidade = tk.Entry(root)
        self.bonus_periculosidade.grid(row=3, column=1)

        tk.Label(root, text="Mês de Início (MM):").grid(row=4, column=0, sticky="w")
        self.mes_inicio = tk.Entry(root)
        self.mes_inicio.grid(row=4, column=1)

        tk.Label(root, text="Ano de Início (AAAA):").grid(row=5, column=0, sticky="w")
        self.ano_inicio = tk.Entry(root)
        self.ano_inicio.grid(row=5, column=1)

        tk.Label(root, text="Mês de Fim (MM):").grid(row=6, column=0, sticky="w")
        self.mes_fim = tk.Entry(root)
        self.mes_fim.grid(row=6, column=1)

        tk.Label(root, text="Ano de Fim (AAAA):").grid(row=7, column=0, sticky="w")
        self.ano_fim = tk.Entry(root)
        self.ano_fim.grid(row=7, column=1)

        tk.Label(root, text="Número de Dependentes:").grid(row=8, column=0, sticky="w")
        self.dependentes = tk.Entry(root)
        self.dependentes.grid(row=8, column=1)

        tk.Label(root, text="Pensão Alimentícia:").grid(row=9, column=0, sticky="w")
        self.pensao_alimenticia = tk.Entry(root)
        self.pensao_alimenticia.grid(row=9, column=1)

        tk.Label(root, text="Outras Deduções:").grid(row=10, column=0, sticky="w")
        self.outros_descontos = tk.Entry(root)
        self.outros_descontos.grid(row=10, column=1)

        tk.Label(root, text="Tipo de Oferta (CLT ou PJ):").grid(row=11, column=0, sticky="w")
        self.tipooferta = tk.Entry(root)
        self.tipooferta.grid(row=11, column=1)

        # Botão para processar os dados
        tk.Button(root, text="Calcular e Gerar Gráficos", command=self.processar_dados).grid(row=12, columnspan=2)

    def processar_dados(self):
        try:
            # Obtendo os valores dos campos
            salario_base = float(self.salario_base.get())
            bonus_tempo = float(self.bonus_tempo.get())
            bonus_formacao = float(self.bonus_formacao.get())
            bonus_periculosidade = float(self.bonus_periculosidade.get())
            mes_inicio = int(self.mes_inicio.get())
            ano_inicio = int(self.ano_inicio.get())
            mes_fim = int(self.mes_fim.get())
            ano_fim = int(self.ano_fim.get())
            dependentes = int(self.dependentes.get())
            pensao_alimenticia = float(self.pensao_alimenticia.get())
            outros_descontos = float(self.outros_descontos.get())
            tipooferta = self.tipooferta.get()

            # Processamento dos dados com LogicaCalculadora
            calculadora = LogicaCalculadora(
                salario_base, bonus_tempo, bonus_formacao, bonus_periculosidade,
                mes_inicio, ano_inicio, mes_fim, ano_fim,
                dependentes, pensao_alimenticia, outros_descontos, tipooferta
            )
            calculadora.calculo_bonus_e_salario_bruto()
            calculadora.calculo_deducoes_e_salario_base()
            calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()

            # Gerar gráficos
            grafico = Grafico(
                salario_liquido=[calculadora.salario_liquido],
                irrf_recolhido=[calculadora.irrf_recolhido],
                anos_vigencia=["2021", "2022", "2023"],  # Substituir com anos reais
                numero_de_graficos=3,
                salario_base=[salario_base],
                aditivos=[bonus_tempo + bonus_formacao + bonus_periculosidade],
                salario_base_de_calculo=[calculadora.salario_base_de_calculo],
                deducoes=[calculadora.total_deducoes],
                nome_contribuinte="Usuário"
            )

            grafico.criargrafico1()
            grafico.criargrafico2()
            grafico.criargrafico3()

            messagebox.showinfo("Sucesso", "Cálculo realizado e gráficos gerados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar os dados: {e}")

# Inicializando a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
