import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.patches as mpatches
import numpy as np

class Grafico:

    def __init__(self, salario_liquido, irrf_recolhido, anos_vigencia, numero_de_graficos,
                 salario_base, aditivos,
                 salario_base_de_calculo, deducoes,
                 nome_contribuinte):

        self.salario_liquido = salario_liquido
        self.irrf_recolhido = irrf_recolhido
        self.anos_vigencia = anos_vigencia
        self.numero_de_graficos = numero_de_graficos + 1

        self.salario_base = salario_base
        self.aditivos = aditivos

        self.salario_base_de_calculo = salario_base_de_calculo
        self.deducoes = deducoes

        self.nome_contribuinte = nome_contribuinte

    @staticmethod
    def formatar_texto_da_barra_de_baixo_do_grafico(x, y):
        for i in range(len(x)):
            plt.text(i, y[i]/2, 'R${:,.2f}'.format(y[i]).replace(",", "X").replace(".", ",").replace("X", "."), ha='center', rotation=90)

    @staticmethod
    def formatar_texto_da_barra_de_cima_do_grafico(x, yp, y):
        for i in range(len(x)):
            plt.text(i, 1.1*yp[i], 'R${:,.2f}'.format(y[i]).replace(",", "X").replace(".", ",").replace("X", "."), ha='center', rotation=0, wrap=True)

    def criargrafico1(self):
        plt.rc('font', **{'sans-serif': 'Arial', 'family': 'sans-serif'})

        fig1, ax1 = plt.subplots()

        plt.title('Valor do salário base e dos aditivos em X anos')
        plt.xlabel('Anos de contribuição')
        plt.ylabel('Valores anuais')

        plt.bar(self.anos_vigencia, self.salario_base, color=(.078, .55, .455))
        plt.bar(self.anos_vigencia, self.aditivos, color=(.502, .780, .228), bottom=np.array(self.salario_base))

        salario_base_patch = mpatches.Patch(color=(.078, .55, .455), label='Salário Base')
        aditivos_patch = mpatches.Patch(color=(.502, .780, .228), label='Aditivos')

        ax1.legend(handles=[salario_base_patch, aditivos_patch])

        fmt = "R${x:.0f}"
        tick = mtick.StrMethodFormatter(fmt)
        ax1.yaxis.set_major_formatter(tick)

        plt.gcf()
        plt.gca()
        plt.show()
        fig1.savefig('Grafico 1 do contribuinte ' + str(self.nome_contribuinte) + '.png', format='png')

    def criargrafico2(self):
        plt.rc('font', **{'sans-serif': 'Arial', 'family': 'sans-serif'})

        fig2, ax2 = plt.subplots()

        plt.title('Valor do salário base de cálculo para o IRRF e das deduçoes em cima do salário bruto em X anos')
        plt.xlabel('Anos de contribuição')
        plt.ylabel('Valores anuais')

        plt.bar(self.anos_vigencia, self.salario_base_de_calculo, color=(.078, .55, .455))
        plt.bar(self.anos_vigencia, self.deducoes, color=(.502, .780, .228), bottom=np.array(self.salario_base_de_calculo))

        salario_base_de_calculo_patch = mpatches.Patch(color=(.078, .55, .455), label='Salário Base de Cálculo do IRRF')
        deducoes_patch = mpatches.Patch(color=(.502, .780, .228), label='Deduções feitas no salário bruto')

        ax2.legend(handles=[salario_base_de_calculo_patch, deducoes_patch])

        fmt = "R${x:.0f}"
        tick = mtick.StrMethodFormatter(fmt)
        ax2.yaxis.set_major_formatter(tick)

        plt.gcf()
        plt.gca()
        plt.show()
        fig2.savefig('Grafico 2 do contribuinte ' + str(self.nome_contribuinte) + '.png', format='png')

    def criargrafico3(self):
        plt.rc('font', **{'sans-serif': 'Arial', 'family': 'sans-serif'})

        fig3, ax3 = plt.subplots()

        plt.title('Valor do salário líquido e do IRRF em X anos')
        plt.xlabel('Anos de contribuição')
        plt.ylabel('Valores anuais')

        plt.bar(self.anos_vigencia, self.salario_liquido, color=(.078, .55, .455))
        plt.bar(self.anos_vigencia, self.irrf_recolhido, color=(.502, .780, .228), bottom=np.array(self.salario_liquido))

        red_patch = mpatches.Patch(color=(.078, .55, .455), label='Salário Líquido')
        blue_patch = mpatches.Patch(color=(.502, .780, .228), label='Imposto de Renda Retido na Fonte')

        ax3.legend(handles=[red_patch, blue_patch])

        fmt = "R${x:.0f}"
        tick = mtick.StrMethodFormatter(fmt)
        ax3.yaxis.set_major_formatter(tick)

        plt.gcf()
        plt.gca()
        plt.show()
        fig3.savefig('grafico do contribuinte ' + str(self.nome_contribuinte) + '.png', format='png')